"""
Eye tracking module for extracting eye and iris positions.
"""

import numpy as np


class EyeTracker:
    """
    Eye tracking using MediaPipe facial landmarks.
    
    Tracks iris positions (landmarks 468, 473) and eye regions for
    both left and right eyes.
    """
    
    # MediaPipe Face Mesh landmark indices for eye regions
    LEFT_EYE = [362, 382, 381, 380, 374, 373, 390, 249, 263, 466, 388, 387, 386, 385, 384, 398]
    RIGHT_EYE = [33, 7, 163, 144, 145, 153, 154, 155, 133, 173, 157, 158, 159, 160, 161, 246]
    
    # Iris landmark indices
    LEFT_IRIS = 468
    RIGHT_IRIS = 473
    
    # Eye landmark indices for aspect ratio calculation
    # These represent the top and bottom points of the eye
    EYE_TOP_INDEX = 12    # Top of eye (from eye landmark array)
    EYE_BOTTOM_INDEX = 4  # Bottom of eye (from eye landmark array)
    
    def __init__(self):
        """Initialize the eye tracker."""
        pass
    
    def get_iris_position(self, landmarks):
        """
        Get the average iris position from both eyes.
        
        Args:
            landmarks: Face mesh landmarks from MediaPipe
            
        Returns:
            tuple: (x, y) normalized coordinates of average iris position
        """
        l_iris = landmarks[self.LEFT_IRIS]
        r_iris = landmarks[self.RIGHT_IRIS]
        
        avg_x = (l_iris.x + r_iris.x) / 2
        avg_y = (l_iris.y + r_iris.y) / 2
        
        return avg_x, avg_y
    
    def get_eye_ratio(self, landmarks, eye_indices):
        """
        Calculate the aspect ratio of an eye (for blink detection).
        
        The ratio is calculated as the vertical distance between top and bottom
        landmarks. A lower ratio indicates a more closed eye.
        
        Args:
            landmarks: Face mesh landmarks from MediaPipe
            eye_indices: List of landmark indices for the eye region
            
        Returns:
            float: Eye aspect ratio (vertical distance)
        """
        top = landmarks[eye_indices[self.EYE_TOP_INDEX]]
        bottom = landmarks[eye_indices[self.EYE_BOTTOM_INDEX]]
        
        dist = np.linalg.norm(
            np.array([top.x, top.y]) - np.array([bottom.x, bottom.y])
        )
        
        return dist
