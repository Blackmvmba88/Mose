# Changelog

All notable changes to the MOSE project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-01-18

### Added
- **Events API**: Major new feature allowing external applications to consume MOSE events
  - New `mose/events.py` module with `EventStream` and `EventType` classes
  - Simple iterator-based API for consuming eye-tracking events
  - Support for events: gaze_move, blink_click, blink_detected, face_detected, face_lost, calibration events, and errors
  - Comprehensive API examples in `examples/` directory
- **Community Resources**:
  - `ROADMAP.md`: Clear 6-milestone development roadmap
  - `PITCH.md`: Elevator pitch for conferences and forums (100-200 words)
  - `GOOD_FIRST_ISSUES.md`: 20 beginner-friendly contribution ideas
  - `DEMO_VIDEO_GUIDE.md`: Complete guide for creating demo videos
  - `RELEASE_STRATEGY.md`: Comprehensive release and marketing strategy
- **GitHub Discussion Templates**: 4 templates for community engagement
  - Ideas template
  - Q&A template
  - Show & Tell template
  - Accessibility-focused template
- **API Examples**: 3 complete usage examples
  - `simple_api_usage.py`: Basic event consumption
  - `click_logger.py`: JSON logging of click events
  - `custom_integration.py`: Advanced integration with custom app
- **Testing**: 11 new unit tests for the events API module
- **Package Distribution**: Enhanced setup.py with entry points for `pip install`
- **Modular Architecture**: Refactored code into organized modules
  - `mose/core/`: Core functionality (face detection, eye tracking, blink detection, gaze mapping)
  - `mose/ui/`: User interface components (calibration, feedback overlay)
- **Comprehensive Documentation**:
  - `INSTALLATION.md`: Detailed installation guide for all platforms
  - `ARCHITECTURE.md`: Technical documentation of system pipeline
  - `CONTRIBUTING.md`: Guidelines for contributors
  - `CHANGELOG.md`: This file
  - `LICENSE`: GPL v3 license
- **GitHub Templates**:
  - Bug report template
  - Feature request template
  - Question template
- **Pinned Dependencies**: Exact version numbers in requirements.txt for reproducibility
- **Enhanced Visual Feedback**:
  - Improved calibration interface
  - Better on-screen instructions
  - Click feedback indicator
- **Improved Documentation**: Extensive inline code documentation with docstrings

### Changed
- Updated README.md with API documentation and installation instructions
- Enhanced setup.py with proper metadata and console script entry point
- Updated `mose/__init__.py` to export EventStream and EventType
- Added `main()` function wrapper to main.py for console script support
- Improved code organization and maintainability
- Better separation of concerns between components

### Technical Improvements
- Version consistently set to 1.1.0 across all files
- All core logic properly documented with docstrings
- Configuration parameters clearly exposed and documented
- Temporal parameters for blink detection documented
- Smoothing algorithm (moving average) explained
- Full test coverage for events API (11 tests, 100% passing)

## [1.0.0] - 2026-01-XX (Initial Release)

### Added
- Initial release of MOSE (Mouse by Eye System)
- Eye-tracking based cursor control using webcam
- MediaPipe Face Mesh integration for face and iris detection
- 5-point calibration system
- Blink detection for click events
- Real-time cursor tracking with moving average smoothing
- Visual feedback overlay
- Basic README and project documentation
- Support for Windows, macOS, and Linux

### Features
- Camera-based eye tracking (no special hardware required)
- Natural interaction (look to move, blink to click)
- Configurable sensitivity and smoothing
- Mirror mode for intuitive control
- Real-time performance (30+ FPS)

---

## Future Releases (Planned)

### [1.2.0] - Planned
- Kalman filter for improved cursor smoothing
- Configuration file for user preferences
- Multi-language support (Spanish, English, Portuguese)
- Video tutorial and demo
- Performance metrics and telemetry (opt-in)

### [2.0.0] - Planned
- Multi-monitor support
- Additional gesture recognition (double blink, wink)
- Adaptive calibration (background recalibration)
- Dead zones configuration
- Audio feedback options
- Accessibility improvements

---

## Legend

- **Added**: New features
- **Changed**: Changes to existing functionality
- **Deprecated**: Features that will be removed
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security fixes

---

For more details on any release, see the corresponding Git tags and release notes.
