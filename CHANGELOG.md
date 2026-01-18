# Changelog

All notable changes to the MOSE project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-01-18

### Added
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
- Updated README.md with clearer structure and information
- Improved code organization and maintainability
- Better separation of concerns between components

### Technical Improvements
- All core logic properly documented with docstrings
- Configuration parameters clearly exposed and documented
- Temporal parameters for blink detection documented
- Smoothing algorithm (moving average) explained

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
