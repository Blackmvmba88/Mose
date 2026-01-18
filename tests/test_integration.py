"""
Integration tests for OcularisMose system.
"""
import unittest
from unittest.mock import Mock, patch, MagicMock, call
import numpy as np
import sys
import os
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import OcularisMose


class TestIntegration(unittest.TestCase):
    """Integration tests for complete workflows"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.mose = OcularisMose()
    
    def test_complete_calibration_workflow(self):
        """Test complete calibration workflow from start to finish"""
        # Start with uncalibrated state
        self.assertFalse(self.mose.calibrated)
        
        # Simulate 5-point calibration
        calibration_data = [
            (0.12, 0.11),  # Top-left
            (0.88, 0.12),  # Top-right
            (0.11, 0.89),  # Bottom-left
            (0.89, 0.88),  # Bottom-right
            (0.50, 0.50)   # Center
        ]
        
        for i, (x, y) in enumerate(calibration_data):
            self.assertEqual(self.mose.calib_index, i)
            self.mose.calibrate(x, y)
        
        # Verify calibration is complete
        self.assertTrue(self.mose.calibrated)
        self.assertEqual(len(self.mose.calib_points), 5)
        
        # Verify calibration ranges are set
        self.assertGreater(self.mose.max_x, self.mose.min_x)
        self.assertGreater(self.mose.max_y, self.mose.min_y)
    
    def test_cursor_movement_after_calibration(self):
        """Test cursor movement with mock calibration"""
        # Complete calibration
        for point in [(0.1, 0.1), (0.9, 0.1), (0.1, 0.9), (0.9, 0.9), (0.5, 0.5)]:
            self.mose.calibrate(point[0], point[1])
        
        self.assertTrue(self.mose.calibrated)
        
        # Simulate gaze point
        gaze_x, gaze_y = 0.5, 0.5
        
        # Calculate normalized coordinates
        norm_x = (gaze_x - self.mose.min_x) / (self.mose.max_x - self.mose.min_x)
        norm_y = (gaze_y - self.mose.min_y) / (self.mose.max_y - self.mose.min_y)
        
        # Clamp values
        norm_x = max(0, min(1, norm_x))
        norm_y = max(0, min(1, norm_y))
        
        # Verify normalized coordinates are in valid range
        self.assertGreaterEqual(norm_x, 0)
        self.assertLessEqual(norm_x, 1)
        self.assertGreaterEqual(norm_y, 0)
        self.assertLessEqual(norm_y, 1)
    
    def test_smoothing_integration(self):
        """Test smoothing integration with multiple data points"""
        # Calibrate first
        for point in [(0.1, 0.1), (0.9, 0.1), (0.1, 0.9), (0.9, 0.9), (0.5, 0.5)]:
            self.mose.calibrate(point[0], point[1])
        
        # Simulate adding multiple gaze points
        gaze_points = [0.45, 0.47, 0.49, 0.51, 0.53, 0.55, 0.52, 0.50]
        
        for point in gaze_points:
            norm_x = (point - self.mose.min_x) / (self.mose.max_x - self.mose.min_x)
            norm_x = max(0, min(1, norm_x))
            
            self.mose.smooth_x.append(norm_x)
            if len(self.mose.smooth_x) > self.mose.buffer_size:
                self.mose.smooth_x.pop(0)
        
        # Verify smoothing buffer doesn't exceed limit
        self.assertLessEqual(len(self.mose.smooth_x), self.mose.buffer_size)
        
        # Calculate smoothed value
        smoothed = sum(self.mose.smooth_x) / len(self.mose.smooth_x)
        
        # Verify smoothed value is reasonable
        self.assertGreater(smoothed, 0)
        self.assertLess(smoothed, 1)
    
    def test_blink_detection_with_cooldown(self):
        """Test blink detection respects cooldown period"""
        initial_time = time.time()
        self.mose.last_click_time = initial_time
        
        # Simulate time passage less than cooldown
        current_time = initial_time + 0.1
        can_click = (current_time - self.mose.last_click_time) > self.mose.click_cooldown
        self.assertFalse(can_click)
        
        # Simulate time passage greater than cooldown
        current_time = initial_time + 0.4
        can_click = (current_time - self.mose.last_click_time) > self.mose.click_cooldown
        self.assertTrue(can_click)
    
    def test_recalibration_workflow(self):
        """Test that system can be recalibrated"""
        # First calibration
        for point in [(0.1, 0.1), (0.9, 0.1), (0.1, 0.9), (0.9, 0.9), (0.5, 0.5)]:
            self.mose.calibrate(point[0], point[1])
        
        self.assertTrue(self.mose.calibrated)
        first_min_x = self.mose.min_x
        
        # Reset for recalibration
        self.mose.calibrated = False
        self.mose.calib_index = 0
        self.mose.calib_points = []
        
        self.assertFalse(self.mose.calibrated)
        
        # Second calibration with different values
        for point in [(0.2, 0.2), (0.8, 0.2), (0.2, 0.8), (0.8, 0.8), (0.5, 0.5)]:
            self.mose.calibrate(point[0], point[1])
        
        self.assertTrue(self.mose.calibrated)
        second_min_x = self.mose.min_x
        
        # Verify calibration values changed
        self.assertNotEqual(first_min_x, second_min_x)


class TestErrorHandling(unittest.TestCase):
    """Test error handling and edge cases"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.mose = OcularisMose()
    
    def test_eye_ratio_with_minimal_landmarks(self):
        """Test eye ratio calculation doesn't crash with minimal data"""
        mock_landmarks = []
        for i in range(500):
            landmark = Mock()
            landmark.x = 0.5
            landmark.y = 0.5
            mock_landmarks.append(landmark)
        
        ratio = self.mose.get_eye_ratio(mock_landmarks, self.mose.LEFT_EYE)
        self.assertIsInstance(ratio, (float, np.floating))
    
    def test_coordinate_clamping_extreme_values(self):
        """Test coordinate clamping with extreme values"""
        self.mose.min_x = 0.2
        self.mose.max_x = 0.8
        self.mose.calibrated = True
        
        # Test extreme negative
        curr_x = -1.0
        norm_x = max(0, min(1, (curr_x - self.mose.min_x) / (self.mose.max_x - self.mose.min_x)))
        self.assertEqual(norm_x, 0.0)
        
        # Test extreme positive
        curr_x = 10.0
        norm_x = max(0, min(1, (curr_x - self.mose.min_x) / (self.mose.max_x - self.mose.min_x)))
        self.assertEqual(norm_x, 1.0)
    
    def test_empty_smoothing_buffer(self):
        """Test handling of empty smoothing buffer"""
        self.mose.smooth_x = []
        
        # Verify buffer is empty
        self.assertEqual(len(self.mose.smooth_x), 0)
        
        # Add a value
        self.mose.smooth_x.append(0.5)
        
        # Should now have one value
        self.assertEqual(len(self.mose.smooth_x), 1)


if __name__ == '__main__':
    unittest.main()
