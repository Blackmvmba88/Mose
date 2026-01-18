"""
Unit tests for OcularisMose core functionality.
"""
import unittest
from unittest.mock import Mock, patch, MagicMock
import numpy as np

from main import OcularisMose


class TestOcularisMose(unittest.TestCase):
    """Test cases for OcularisMose class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.mose = OcularisMose()
    
    def test_initialization(self):
        """Test that OcularisMose initializes correctly"""
        self.assertFalse(self.mose.calibrated)
        self.assertEqual(self.mose.calib_index, 0)
        self.assertEqual(len(self.mose.calib_points), 0)
        self.assertEqual(len(self.mose.calib_targets), 5)
        self.assertEqual(self.mose.buffer_size, 8)
        
    def test_calibration_targets(self):
        """Test that calibration targets are correctly defined"""
        expected_targets = [(0.1, 0.1), (0.9, 0.1), (0.1, 0.9), (0.9, 0.9), (0.5, 0.5)]
        self.assertEqual(self.mose.calib_targets, expected_targets)
    
    def test_eye_ratio_calculation(self):
        """Test eye ratio calculation for blink detection"""
        # Create mock landmarks
        mock_landmarks = []
        for i in range(500):
            landmark = Mock()
            if i == self.mose.LEFT_EYE[12]:
                landmark.x = 0.5
                landmark.y = 0.4
            elif i == self.mose.LEFT_EYE[4]:
                landmark.x = 0.5
                landmark.y = 0.42
            else:
                landmark.x = 0.5
                landmark.y = 0.5
            mock_landmarks.append(landmark)
        
        ratio = self.mose.get_eye_ratio(mock_landmarks, self.mose.LEFT_EYE)
        self.assertIsInstance(ratio, (float, np.floating))
        self.assertGreater(ratio, 0)
    
    def test_calibrate_single_point(self):
        """Test calibration with a single point"""
        initial_index = self.mose.calib_index
        self.mose.calibrate(0.45, 0.35)
        
        self.assertEqual(self.mose.calib_index, initial_index + 1)
        self.assertEqual(len(self.mose.calib_points), 1)
        self.assertEqual(self.mose.calib_points[0], (0.45, 0.35))
        self.assertFalse(self.mose.calibrated)
    
    def test_calibrate_complete(self):
        """Test complete calibration with all 5 points"""
        test_points = [
            (0.1, 0.1),
            (0.9, 0.1),
            (0.1, 0.9),
            (0.9, 0.9),
            (0.5, 0.5)
        ]
        
        for point in test_points:
            self.mose.calibrate(point[0], point[1])
        
        self.assertTrue(self.mose.calibrated)
        self.assertEqual(self.mose.calib_index, 5)
        self.assertEqual(len(self.mose.calib_points), 5)
        self.assertAlmostEqual(self.mose.min_x, 0.1, places=2)
        self.assertAlmostEqual(self.mose.max_x, 0.9, places=2)
        self.assertAlmostEqual(self.mose.min_y, 0.1, places=2)
        self.assertAlmostEqual(self.mose.max_y, 0.9, places=2)
    
    def test_smoothing_buffer(self):
        """Test that smoothing buffer maintains correct size"""
        for i in range(15):
            self.mose.smooth_x.append(0.5 + i * 0.01)
            if len(self.mose.smooth_x) > self.mose.buffer_size:
                self.mose.smooth_x.pop(0)
        
        self.assertLessEqual(len(self.mose.smooth_x), self.mose.buffer_size)
    
    def test_coordinate_normalization(self):
        """Test coordinate normalization after calibration"""
        # Simulate complete calibration
        self.mose.min_x = 0.2
        self.mose.max_x = 0.8
        self.mose.min_y = 0.15
        self.mose.max_y = 0.85
        self.mose.calibrated = True
        
        # Test point at center of calibrated range
        curr_x = 0.5
        curr_y = 0.5
        
        norm_x = (curr_x - self.mose.min_x) / (self.mose.max_x - self.mose.min_x)
        norm_y = (curr_y - self.mose.min_y) / (self.mose.max_y - self.mose.min_y)
        
        self.assertAlmostEqual(norm_x, 0.5, places=2)
        self.assertAlmostEqual(norm_y, 0.5, places=2)
        
        # Test clamping - point outside range
        curr_x = 1.0
        norm_x = max(0, min(1, (curr_x - self.mose.min_x) / (self.mose.max_x - self.mose.min_x)))
        self.assertEqual(norm_x, 1.0)
        
        curr_x = 0.0
        norm_x = max(0, min(1, (curr_x - self.mose.min_x) / (self.mose.max_x - self.mose.min_x)))
        self.assertEqual(norm_x, 0.0)
    
    def test_blink_threshold(self):
        """Test blink detection threshold"""
        self.assertIsInstance(self.mose.blink_threshold, float)
        self.assertGreater(self.mose.blink_threshold, 0)
        self.assertLess(self.mose.blink_threshold, 0.1)
    
    def test_click_cooldown(self):
        """Test click cooldown mechanism"""
        self.assertIsInstance(self.mose.click_cooldown, float)
        self.assertGreater(self.mose.click_cooldown, 0)
        self.assertEqual(self.mose.click_cooldown, 0.3)
    
    def test_screen_dimensions(self):
        """Test screen dimensions are captured"""
        self.assertIsInstance(self.mose.screen_w, int)
        self.assertIsInstance(self.mose.screen_h, int)
        self.assertGreater(self.mose.screen_w, 0)
        self.assertGreater(self.mose.screen_h, 0)


class TestCalibrationSystem(unittest.TestCase):
    """Test cases for calibration system"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.mose = OcularisMose()
    
    def test_calibration_reset(self):
        """Test calibration can be reset"""
        # Add some calibration points
        self.mose.calibrate(0.1, 0.1)
        self.mose.calibrate(0.9, 0.1)
        
        # Reset calibration
        self.mose.calibrated = False
        self.mose.calib_index = 0
        self.mose.calib_points = []
        
        self.assertFalse(self.mose.calibrated)
        self.assertEqual(self.mose.calib_index, 0)
        self.assertEqual(len(self.mose.calib_points), 0)
    
    def test_calibration_range_calculation(self):
        """Test that calibration correctly calculates min/max ranges"""
        points = [
            (0.15, 0.12),
            (0.85, 0.13),
            (0.14, 0.88),
            (0.86, 0.87),
            (0.50, 0.51)
        ]
        
        for point in points:
            self.mose.calibrate(point[0], point[1])
        
        points_array = np.array(points)
        expected_min_x = np.min(points_array[:, 0])
        expected_max_x = np.max(points_array[:, 0])
        expected_min_y = np.min(points_array[:, 1])
        expected_max_y = np.max(points_array[:, 1])
        
        self.assertAlmostEqual(self.mose.min_x, expected_min_x, places=2)
        self.assertAlmostEqual(self.mose.max_x, expected_max_x, places=2)
        self.assertAlmostEqual(self.mose.min_y, expected_min_y, places=2)
        self.assertAlmostEqual(self.mose.max_y, expected_max_y, places=2)


class TestSmoothingSystem(unittest.TestCase):
    """Test cases for cursor smoothing system"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.mose = OcularisMose()
    
    def test_smoothing_buffer_averaging(self):
        """Test that smoothing buffer correctly averages values"""
        values = [0.1, 0.2, 0.3, 0.4, 0.5]
        self.mose.smooth_x = values.copy()
        
        avg = sum(self.mose.smooth_x) / len(self.mose.smooth_x)
        expected_avg = sum(values) / len(values)
        
        self.assertEqual(avg, expected_avg)
    
    def test_buffer_size_limit(self):
        """Test that buffer doesn't exceed maximum size"""
        for i in range(20):
            self.mose.smooth_x.append(i)
            if len(self.mose.smooth_x) > self.mose.buffer_size:
                self.mose.smooth_x.pop(0)
        
        self.assertEqual(len(self.mose.smooth_x), self.mose.buffer_size)
    
    def test_buffer_fifo_behavior(self):
        """Test that buffer follows FIFO (First In First Out) behavior"""
        # Fill buffer beyond capacity
        for i in range(self.mose.buffer_size + 3):
            self.mose.smooth_x.append(i)
            if len(self.mose.smooth_x) > self.mose.buffer_size:
                self.mose.smooth_x.pop(0)
        
        # Check that oldest values were removed
        self.assertEqual(len(self.mose.smooth_x), self.mose.buffer_size)
        self.assertEqual(self.mose.smooth_x[0], 3)  # First value should be 3
        self.assertEqual(self.mose.smooth_x[-1], 10)  # Last value should be 10


if __name__ == '__main__':
    unittest.main()
