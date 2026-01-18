"""
Visual feedback overlay for the MOSE interface.
"""

import cv2


class FeedbackOverlay:
    """
    Provides visual feedback on the camera feed.
    
    Shows calibration targets, iris positions, click indicators,
    and instructions to the user.
    """
    
    def __init__(self):
        """Initialize the feedback overlay."""
        self.show_click_feedback = False
        self.click_feedback_frames = 0
        self.click_feedback_duration = 10  # frames
    
    def draw_calibration_target(self, image, target_x, target_y, current, total):
        """
        Draw a calibration target on the image.
        
        Args:
            image: OpenCV image to draw on
            target_x: X coordinate (normalized 0-1)
            target_y: Y coordinate (normalized 0-1)
            current: Current calibration point number (1-indexed)
            total: Total number of calibration points
        """
        h, w, _ = image.shape
        
        # Draw target circle
        center = (int(target_x * w), int(target_y * h))
        cv2.circle(image, center, 20, (0, 255, 255), -1)
        cv2.circle(image, center, 25, (255, 255, 255), 2)
        
        # Draw instruction text
        text = f"Point {current}/{total}: Look here and press SPACE"
        cv2.putText(image, text, (50, h - 50), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    def draw_iris_markers(self, image, landmarks, left_iris_idx=468, right_iris_idx=473):
        """
        Draw markers on iris positions.
        
        Args:
            image: OpenCV image to draw on
            landmarks: Face mesh landmarks from MediaPipe
            left_iris_idx: Landmark index for left iris
            right_iris_idx: Landmark index for right iris
        """
        h, w, _ = image.shape
        
        for idx in [left_iris_idx, right_iris_idx]:
            p = landmarks[idx]
            center = (int(p.x * w), int(p.y * h))
            cv2.circle(image, center, 3, (0, 255, 0), -1)
    
    def draw_eye_regions(self, image, landmarks, left_eye_indices, right_eye_indices):
        """
        Draw polygons around eye regions.
        
        Note: Currently disabled by default to avoid cluttering the display.
        Enable by uncommenting the code below if needed.
        
        Args:
            image: OpenCV image to draw on
            landmarks: Face mesh landmarks
            left_eye_indices: List of landmark indices for left eye
            right_eye_indices: List of landmark indices for right eye
        """
        pass  # Optional visualization feature - can be enabled in future config
    
    def trigger_click_feedback(self):
        """Trigger visual feedback for a click event."""
        self.show_click_feedback = True
        self.click_feedback_frames = 0
    
    def draw_click_indicator(self, image):
        """
        Draw click indicator if recently clicked.
        
        Args:
            image: OpenCV image to draw on
        """
        if self.show_click_feedback:
            cv2.putText(image, "CLICK!", (50, 50), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
            
            self.click_feedback_frames += 1
            if self.click_feedback_frames >= self.click_feedback_duration:
                self.show_click_feedback = False
    
    def draw_status_text(self, image, text, position=(50, 100)):
        """
        Draw status text on the image.
        
        Args:
            image: OpenCV image to draw on
            text: Text to display
            position: (x, y) position for the text
        """
        cv2.putText(image, text, position, 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
    def draw_instructions(self, image):
        """
        Draw usage instructions on the image.
        
        Args:
            image: OpenCV image to draw on
        """
        h, w, _ = image.shape
        instructions = [
            "Controls:",
            "  'c' - Start/restart calibration",
            "  'q' - Quit",
            "  Blink rapidly to click"
        ]
        
        y_offset = 30
        for i, line in enumerate(instructions):
            cv2.putText(image, line, (w - 350, y_offset + i * 25),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)
