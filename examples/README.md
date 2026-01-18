# MOSE Examples and Tests

This directory contains example scripts and tests for MOSE.

## Available Scripts

### test_components.py

A simple test script that verifies MOSE components work correctly without requiring a camera.

**Usage**:
```bash
python examples/test_components.py
```

**What it tests**:
- All module imports work
- BlinkDetector logic (threshold, cooldown)
- Calibrator state management (5-point calibration)
- GazeToCursor coordinate mapping
- Configuration loading and defaults

**Expected output** (when passing):
```
==================================================
MOSE Component Tests
==================================================
Testing imports...
  ✓ FaceDetector
  ✓ EyeTracker
  ✓ BlinkDetector
  ✓ GazeToCursor
  ✓ Calibrator
  ✓ FeedbackOverlay
  ✓ Config

✅ All imports successful

Testing basic functionality...
  ✓ BlinkDetector: No false positive
  ✓ BlinkDetector: Detects closed eye
  ✓ BlinkDetector: Respects cooldown
  ✓ Calibrator: Initial state correct
  ✓ Calibrator: Completes with 5 points
  ✓ Calibrator: Returns calibration range
  ✓ GazeToCursor: Requires calibration
  ✓ GazeToCursor: Calibration works
  ✓ GazeToCursor: Maps to screen coordinates

✅ All functionality tests passed

Testing configuration...
  ✓ Config: Loads defaults
  ✓ Config: Integer values work
  ✓ Config: Boolean values work

✅ Config tests passed

==================================================
✅ ALL TESTS PASSED!
MOSE components are working correctly.

Next steps:
  1. Run 'python main.py' to test with your camera
  2. Follow calibration instructions
  3. Start using eye tracking!
```

## Future Examples

More examples will be added:
- Camera detection and selection
- Custom calibration patterns
- Integration with other applications
- Performance benchmarking
- Advanced configuration examples

## Running Tests

Before using MOSE with your camera, it's a good idea to run the tests:

```bash
# Make sure dependencies are installed
pip install -r requirements.txt

# Run tests
python examples/test_components.py

# If all tests pass, try MOSE with your camera
python main.py
```

## Troubleshooting

If tests fail:

1. **Import errors**: Install dependencies with `pip install -r requirements.txt`
2. **Path errors**: Run from the project root directory (where main.py is)
3. **Other errors**: Check the full error message and traceback

For more help, see [INSTALLATION.md](../INSTALLATION.md) or [create an issue](https://github.com/Blackmvmba88/Mose/issues).
