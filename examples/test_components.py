"""
Simple test script to verify MOSE components work correctly.
This doesn't require a camera - just tests imports and basic functionality.
"""

import sys
import traceback


def test_imports():
    """Test that all MOSE modules can be imported."""
    print("Testing imports...")
    
    try:
        from mose.core.face_detection import FaceDetector
        print("  ✓ FaceDetector")
    except ImportError as e:
        print(f"  ✗ FaceDetector: {e}")
        return False
    
    try:
        from mose.core.eye_tracking import EyeTracker
        print("  ✓ EyeTracker")
    except ImportError as e:
        print(f"  ✗ EyeTracker: {e}")
        return False
    
    try:
        from mose.core.blink_detector import BlinkDetector
        print("  ✓ BlinkDetector")
    except ImportError as e:
        print(f"  ✗ BlinkDetector: {e}")
        return False
    
    try:
        from mose.core.gaze_to_cursor import GazeToCursor
        print("  ✓ GazeToCursor")
    except ImportError as e:
        print(f"  ✗ GazeToCursor: {e}")
        return False
    
    try:
        from mose.ui.calibration import Calibrator
        print("  ✓ Calibrator")
    except ImportError as e:
        print(f"  ✗ Calibrator: {e}")
        return False
    
    try:
        from mose.ui.feedback_overlay import FeedbackOverlay
        print("  ✓ FeedbackOverlay")
    except ImportError as e:
        print(f"  ✗ FeedbackOverlay: {e}")
        return False
    
    try:
        from mose.config import Config
        print("  ✓ Config")
    except ImportError as e:
        print(f"  ✗ Config: {e}")
        return False
    
    return True


def test_basic_functionality():
    """Test basic functionality without camera."""
    print("\nTesting basic functionality...")
    
    try:
        from mose.core.blink_detector import BlinkDetector
        detector = BlinkDetector(threshold=0.005, cooldown=0.3)
        
        # Test that blink detection works with mock data
        result = detector.detect_blink(0.01)  # Open eye
        assert result == False, "Should not detect blink with open eye"
        print("  ✓ BlinkDetector: No false positive")
        
        result = detector.detect_blink(0.001)  # Closed eye
        assert result == True, "Should detect blink with closed eye"
        print("  ✓ BlinkDetector: Detects closed eye")
        
        result = detector.detect_blink(0.001)  # Closed eye again (cooldown)
        assert result == False, "Should respect cooldown"
        print("  ✓ BlinkDetector: Respects cooldown")
        
    except Exception as e:
        print(f"  ✗ BlinkDetector test failed: {e}")
        traceback.print_exc()
        return False
    
    try:
        from mose.ui.calibration import Calibrator
        calibrator = Calibrator()
        
        # Test calibration state
        assert not calibrator.is_complete(), "Should start not calibrated"
        print("  ✓ Calibrator: Initial state correct")
        
        # Add calibration points
        for i in range(5):
            calibrator.add_point(0.5, 0.5)
        
        assert calibrator.is_complete(), "Should be complete after 5 points"
        print("  ✓ Calibrator: Completes with 5 points")
        
        calib_range = calibrator.get_calibration_range()
        assert calib_range is not None, "Should return calibration range"
        print("  ✓ Calibrator: Returns calibration range")
        
    except Exception as e:
        print(f"  ✗ Calibrator test failed: {e}")
        traceback.print_exc()
        return False
    
    try:
        from mose.core.gaze_to_cursor import GazeToCursor
        mapper = GazeToCursor(1920, 1080, buffer_size=8)
        
        # Test that mapper requires calibration
        result = mapper.map_to_screen(0.5, 0.5)
        assert result is None, "Should return None when not calibrated"
        print("  ✓ GazeToCursor: Requires calibration")
        
        # Set calibration
        mapper.set_calibration(0.4, 0.6, 0.4, 0.6)
        assert mapper.is_calibrated(), "Should be calibrated after setting"
        print("  ✓ GazeToCursor: Calibration works")
        
        # Test mapping
        result = mapper.map_to_screen(0.5, 0.5)
        assert result is not None, "Should return coordinates when calibrated"
        assert len(result) == 2, "Should return (x, y) tuple"
        print("  ✓ GazeToCursor: Maps to screen coordinates")
        
    except Exception as e:
        print(f"  ✗ GazeToCursor test failed: {e}")
        traceback.print_exc()
        return False
    
    return True


def test_config():
    """Test configuration loading."""
    print("\nTesting configuration...")
    
    try:
        from mose.config import Config
        
        # Test with non-existent file (should use defaults)
        config = Config('nonexistent.ini')
        
        threshold = config.get_float('blink', 'threshold')
        assert threshold == 0.0045, f"Default threshold should be 0.0045, got {threshold}"
        print("  ✓ Config: Loads defaults")
        
        buffer_size = config.get_int('gaze', 'smoothing_buffer_size')
        assert buffer_size == 8, f"Default buffer size should be 8, got {buffer_size}"
        print("  ✓ Config: Integer values work")
        
        show_markers = config.get_bool('ui', 'show_iris_markers')
        assert show_markers == True, "Default show_iris_markers should be True"
        print("  ✓ Config: Boolean values work")
        
    except Exception as e:
        print(f"  ✗ Config test failed: {e}")
        traceback.print_exc()
        return False
    
    return True


def main():
    """Run all tests."""
    print("=" * 50)
    print("MOSE Component Tests")
    print("=" * 50)
    
    all_passed = True
    
    if not test_imports():
        print("\n❌ Import tests FAILED")
        print("Run: pip install -r requirements.txt")
        all_passed = False
    else:
        print("\n✅ All imports successful")
    
    if not test_basic_functionality():
        print("\n❌ Functionality tests FAILED")
        all_passed = False
    else:
        print("\n✅ All functionality tests passed")
    
    if not test_config():
        print("\n❌ Config tests FAILED")
        all_passed = False
    else:
        print("\n✅ Config tests passed")
    
    print("\n" + "=" * 50)
    if all_passed:
        print("✅ ALL TESTS PASSED!")
        print("MOSE components are working correctly.")
        print("\nNext steps:")
        print("  1. Run 'python main.py' to test with your camera")
        print("  2. Follow calibration instructions")
        print("  3. Start using eye tracking!")
        return 0
    else:
        print("❌ SOME TESTS FAILED")
        print("Please fix the errors above before running MOSE.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
