"""
Gaze to cursor mapping module with smoothing and calibration.
"""

import numpy as np


class GazeToCursor:
    """
    Maps gaze coordinates to screen cursor position.
    
    Includes calibration, normalization, and smoothing via moving average filter.
    """
    
    def __init__(self, screen_width, screen_height, buffer_size=8):
        """
        Initialize the gaze-to-cursor mapper.
        
        Args:
            screen_width: Width of the screen in pixels
            screen_height: Height of the screen in pixels
            buffer_size: Size of smoothing buffer (higher = smoother but less responsive)
        """
        self.screen_w = screen_width
        self.screen_h = screen_height
        self.buffer_size = buffer_size
        
        # Smoothing buffers using moving average
        self.smooth_x = []
        self.smooth_y = []
        
        # Calibration ranges (will be set during calibration)
        self.min_x = 0.4
        self.max_x = 0.6
        self.min_y = 0.4
        self.max_y = 0.6
        self.calibrated = False
    
    def set_calibration(self, min_x, max_x, min_y, max_y):
        """
        Set calibration parameters.
        
        Args:
            min_x, max_x: Minimum and maximum X coordinates from calibration
            min_y, max_y: Minimum and maximum Y coordinates from calibration
        """
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.calibrated = True
    
    def map_to_screen(self, gaze_x, gaze_y):
        """
        Map gaze coordinates to screen coordinates with smoothing.
        
        Args:
            gaze_x: Normalized gaze X coordinate (0-1 range from face mesh)
            gaze_y: Normalized gaze Y coordinate (0-1 range from face mesh)
            
        Returns:
            tuple: (screen_x, screen_y) pixel coordinates, or None if not calibrated
        """
        if not self.calibrated:
            return None
        
        # Normalize based on calibration range
        norm_x = (gaze_x - self.min_x) / (self.max_x - self.min_x)
        norm_y = (gaze_y - self.min_y) / (self.max_y - self.min_y)
        
        # Clamp to 0-1 range
        norm_x = max(0, min(1, norm_x))
        norm_y = max(0, min(1, norm_y))
        
        # Apply moving average smoothing
        self.smooth_x.append(norm_x)
        self.smooth_y.append(norm_y)
        
        if len(self.smooth_x) > self.buffer_size:
            self.smooth_x.pop(0)
            self.smooth_y.pop(0)
        
        # Calculate smoothed position
        target_x = sum(self.smooth_x) / len(self.smooth_x)
        target_y = sum(self.smooth_y) / len(self.smooth_y)
        
        # Convert to screen coordinates
        screen_x = int(target_x * self.screen_w)
        screen_y = int(target_y * self.screen_h)
        
        return screen_x, screen_y
    
    def reset_smoothing(self):
        """Clear smoothing buffers (useful when starting tracking)."""
        self.smooth_x = []
        self.smooth_y = []
    
    def is_calibrated(self):
        """Check if the mapper has been calibrated."""
        return self.calibrated
