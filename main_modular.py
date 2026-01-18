"""
MOSE - Mouse by Eye System
Modular version using refactored components
"""

import cv2
import pyautogui

from mose.core.face_detection import FaceDetector
from mose.core.eye_tracking import EyeTracker
from mose.core.blink_detector import BlinkDetector
from mose.core.gaze_to_cursor import GazeToCursor
from mose.ui.calibration import Calibrator
from mose.ui.feedback_overlay import FeedbackOverlay
from mose.config import Config


class OcularisMose:
    """
    Main MOSE application class.
    
    Integrates all components: face detection, eye tracking, blink detection,
    gaze-to-cursor mapping, calibration, and visual feedback.
    """
    
    def __init__(self, config_file='config.ini'):
        """
        Initialize MOSE with all components.
        
        Args:
            config_file: Path to configuration file
        """
        # Load configuration
        self.config = Config(config_file)
        
        # Get screen dimensions
        screen_w, screen_h = pyautogui.size()
        
        # Initialize core components
        self.face_detector = FaceDetector(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=self.config.get_float('detection', 'min_detection_confidence'),
            min_tracking_confidence=self.config.get_float('detection', 'min_tracking_confidence')
        )
        self.eye_tracker = EyeTracker()
        self.blink_detector = BlinkDetector(
            threshold=self.config.get_float('blink', 'threshold'),
            cooldown=self.config.get_float('blink', 'cooldown')
        )
        self.gaze_mapper = GazeToCursor(
            screen_w, screen_h, 
            buffer_size=self.config.get_int('gaze', 'smoothing_buffer_size')
        )
        
        # Initialize UI components
        self.calibrator = Calibrator()
        self.feedback = FeedbackOverlay()
        
        # Camera setup
        camera_index = self.config.get_int('camera', 'camera_index')
        self.cap = cv2.VideoCapture(camera_index)
        
        # UI settings
        self.show_iris_markers = self.config.get_bool('ui', 'show_iris_markers')
        self.show_instructions = self.config.get_bool('ui', 'show_instructions')
    
    def run(self):
        """Main application loop."""
        print("=" * 50)
        print("🧿 MOSE - Mouse by Eye System")
        print("=" * 50)
        print("\nControls:")
        print("  'c' - Start/restart calibration")
        print("  Blink rapidly to click (after calibration)")
        print("  'q' - Quit")
        print("\nStarting camera...")
        
        while self.cap.isOpened():
            success, image = self.cap.read()
            if not success:
                print("Failed to read from camera")
                break
            
            # Flip image horizontally for mirror effect
            image = cv2.flip(image, 1)
            h, w, _ = image.shape
            
            # Convert to RGB for MediaPipe
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = self.face_detector.process(rgb_image)
            
            if results.multi_face_landmarks:
                landmarks = results.multi_face_landmarks[0].landmark
                
                # Get iris position
                iris_x, iris_y = self.eye_tracker.get_iris_position(landmarks)
                
                # Handle calibration or tracking
                if not self.calibrator.is_complete():
                    self._handle_calibration_mode(image, iris_x, iris_y, w, h, landmarks)
                else:
                    self._handle_tracking_mode(image, iris_x, iris_y, landmarks)
                
                # Draw iris markers
                if self.show_iris_markers:
                    self.feedback.draw_iris_markers(image, landmarks)
            
            # Draw click indicator if active
            self.feedback.draw_click_indicator(image)
            
            # Draw instructions
            if self.show_instructions:
                self.feedback.draw_instructions(image)
            
            # Show the window
            cv2.imshow('MOSE Control Panel', image)
            
            # Handle keyboard input
            key = cv2.waitKey(5) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('c'):
                self._restart_calibration()
        
        # Cleanup
        self.cap.release()
        cv2.destroyAllWindows()
        self.face_detector.close()
        print("\n🧿 MOSE closed. Goodbye!")
    
    def _handle_calibration_mode(self, image, iris_x, iris_y, w, h, landmarks):
        """Handle calibration mode logic."""
        target = self.calibrator.get_current_target()
        if target:
            current, total = self.calibrator.get_progress()
            self.feedback.draw_calibration_target(
                image, target[0], target[1], current + 1, total
            )
        
        # Check for spacebar to capture calibration point
        key = cv2.waitKey(1) & 0xFF
        if key == ord(' '):
            is_complete = self.calibrator.add_point(iris_x, iris_y)
            
            if is_complete:
                # Get calibration range and configure gaze mapper
                calib_range = self.calibrator.get_calibration_range()
                if calib_range:
                    min_x, max_x, min_y, max_y = calib_range
                    self.gaze_mapper.set_calibration(min_x, max_x, min_y, max_y)
                    print("\n✓ Calibration complete!")
                    print(f"  Range: X[{min_x:.3f}-{max_x:.3f}], Y[{min_y:.3f}-{max_y:.3f}]")
                    print("\n🎯 You can now control the cursor with your eyes!")
                    print("   Blink rapidly to click.\n")
            else:
                current, total = self.calibrator.get_progress()
                print(f"  Point {current}/{total} captured")
    
    def _handle_tracking_mode(self, image, iris_x, iris_y, landmarks):
        """Handle cursor tracking mode logic."""
        # Map gaze to cursor position
        cursor_pos = self.gaze_mapper.map_to_screen(iris_x, iris_y)
        
        if cursor_pos:
            screen_x, screen_y = cursor_pos
            pyautogui.moveTo(screen_x, screen_y)
            
            # Check for blink (click)
            l_eye_ratio = self.eye_tracker.get_eye_ratio(
                landmarks, self.eye_tracker.LEFT_EYE
            )
            
            if self.blink_detector.detect_blink(l_eye_ratio):
                pyautogui.click()
                self.feedback.trigger_click_feedback()
                print("👁️ Click!")
    
    def _restart_calibration(self):
        """Restart the calibration process."""
        self.calibrator.reset()
        self.gaze_mapper.calibrated = False
        self.gaze_mapper.reset_smoothing()
        print("\n🔄 Calibration reset. Press 'c' again and follow instructions.")


if __name__ == "__main__":
    app = OcularisMose()
    app.run()
