"""
Calibration module for gaze tracking system.
"""

import numpy as np


class Calibrator:
    """
    Handles the 5-point calibration process for gaze tracking.
    
    The calibration uses 5 points: 4 corners and the center of the screen
    to establish the mapping between eye position and screen coordinates.
    """
    
    # Standard 5-point calibration targets (normalized 0-1 coordinates)
    CALIBRATION_TARGETS = [
        (0.1, 0.1),   # Top-left
        (0.9, 0.1),   # Top-right
        (0.1, 0.9),   # Bottom-left
        (0.9, 0.9),   # Bottom-right
        (0.5, 0.5)    # Center
    ]
    
    def __init__(self):
        """Initialize the calibrator."""
        self.calib_points = []
        self.calib_index = 0
        self.calibrated = False
    
    def reset(self):
        """Reset calibration state."""
        self.calib_points = []
        self.calib_index = 0
        self.calibrated = False
    
    def add_point(self, iris_x, iris_y):
        """
        Add a calibration point.
        
        Args:
            iris_x: Normalized X coordinate of iris position
            iris_y: Normalized Y coordinate of iris position
            
        Returns:
            bool: True if calibration is complete
        """
        self.calib_points.append((iris_x, iris_y))
        self.calib_index += 1
        
        if self.calib_index >= len(self.CALIBRATION_TARGETS):
            self.calibrated = True
            return True
        
        return False
    
    def get_calibration_range(self):
        """
        Calculate the calibration range from collected points.
        
        Returns:
            tuple: (min_x, max_x, min_y, max_y) or None if not calibrated
        """
        if not self.calibrated:
            return None
        
        points = np.array(self.calib_points)
        min_x, min_y = np.min(points, axis=0)
        max_x, max_y = np.max(points, axis=0)
        
        return min_x, max_x, min_y, max_y
    
    def get_current_target(self):
        """
        Get the current calibration target.
        
        Returns:
            tuple: (x, y) normalized coordinates of current target, or None if done
        """
        if self.calib_index < len(self.CALIBRATION_TARGETS):
            return self.CALIBRATION_TARGETS[self.calib_index]
        return None
    
    def get_progress(self):
        """
        Get calibration progress.
        
        Returns:
            tuple: (current_point, total_points)
        """
        return self.calib_index, len(self.CALIBRATION_TARGETS)
    
    def is_complete(self):
        """Check if calibration is complete."""
        return self.calibrated
