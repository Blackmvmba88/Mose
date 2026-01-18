# Contributing to MOSE

First off, thank you for considering contributing to MOSE! It's people like you that make MOSE a great tool for accessibility and assistive technology.

## Code of Conduct

This project is dedicated to providing a welcoming and harassment-free experience for everyone. We expect all contributors to:

- Use welcoming and inclusive language
- Be respectful of differing viewpoints and experiences
- Gracefully accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the existing issues to avoid duplicates. When creating a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples** (code snippets, screenshots)
- **Describe the behavior you observed** and what you expected
- **Include details about your configuration** (OS, Python version, camera specs)

Use the [Bug Report template](.github/ISSUE_TEMPLATE/bug_report.md) when creating your issue.

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:

- **Use a clear and descriptive title**
- **Provide a detailed description** of the proposed functionality
- **Explain why this enhancement would be useful**
- **List any alternatives you've considered**

Use the [Feature Request template](.github/ISSUE_TEMPLATE/feature_request.md) when creating your issue.

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the code style guidelines
3. **Test your changes** thoroughly
4. **Update documentation** if needed
5. **Write meaningful commit messages**
6. **Submit a pull request**

## Development Setup

### Prerequisites

- Python 3.9 or higher
- Webcam for testing
- Virtual environment tool (recommended)

### Setup Steps

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/Mose.git
cd Mose

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run MOSE
python main.py
```

## Code Style Guidelines

### Python Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use descriptive variable names

### Documentation

- Add docstrings to all functions, classes, and modules
- Use Google-style docstrings format:

```python
def function_name(param1, param2):
    """
    Brief description of function.
    
    More detailed description if needed.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
        
    Raises:
        ExceptionType: When this exception is raised
    """
    pass
```

### Comments

- Write comments for complex logic
- Keep comments up-to-date with code changes
- Use `#` for inline comments, docstrings for functions/classes

### Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- First line: brief summary (50 chars or less)
- Blank line, then detailed description if needed

Example:
```
Add Kalman filter for cursor smoothing

Replaces moving average with Kalman filter to reduce jitter
while maintaining responsiveness. Improves tracking accuracy
by 15% in user testing.
```

## Project Structure

```
Mose/
├── main.py                 # Original monolithic version
├── main_modular.py         # Refactored modular version
├── mose/                   # Package directory
│   ├── __init__.py
│   ├── core/               # Core functionality
│   │   ├── face_detection.py
│   │   ├── eye_tracking.py
│   │   ├── blink_detector.py
│   │   └── gaze_to_cursor.py
│   └── ui/                 # User interface components
│       ├── calibration.py
│       └── feedback_overlay.py
├── requirements.txt        # Dependencies with pinned versions
├── README.md              # Project overview
├── INSTALLATION.md        # Installation instructions
├── ARCHITECTURE.md        # Technical documentation
└── CONTRIBUTING.md        # This file
```

## Areas for Contribution

### High Priority

- **Testing**: Add unit tests and integration tests
- **Documentation**: Improve inline code documentation
- **Performance**: Optimize frame processing speed
- **Accessibility**: Add keyboard shortcuts, audio feedback

### Medium Priority

- **UI Improvements**: Better calibration interface
- **Configuration**: Settings file for user preferences
- **Multi-language Support**: Internationalization (i18n)
- **Platform Testing**: Test on various OS/hardware combinations

### Research & Experimentation

- **Kalman Filter**: Implement for better smoothing
- **Machine Learning**: Personalized calibration models
- **Gesture Recognition**: Additional eye gestures
- **Metrics**: Collect and analyze performance data

## Testing Guidelines

### Manual Testing Checklist

Before submitting a PR, test:

- [ ] Installation on fresh environment
- [ ] Calibration process (5 points)
- [ ] Cursor tracking accuracy
- [ ] Blink detection for clicks
- [ ] Keyboard shortcuts ('c', 'q')
- [ ] Performance (FPS, CPU usage)
- [ ] Different lighting conditions
- [ ] Different camera distances

### Writing Tests (Future)

When test infrastructure is added:

```python
# Example test structure
def test_iris_position():
    """Test iris position extraction from landmarks."""
    tracker = EyeTracker()
    # Mock landmarks
    landmarks = create_mock_landmarks()
    x, y = tracker.get_iris_position(landmarks)
    assert 0 <= x <= 1
    assert 0 <= y <= 1
```

## Documentation Contributions

Documentation improvements are always welcome:

- Fix typos or clarify instructions
- Add examples or screenshots
- Translate to other languages
- Create video tutorials
- Write blog posts about MOSE usage

## Community

### Getting Help

- **GitHub Issues**: For bugs and feature requests
- **Discussions**: For questions and general discussion
- **Documentation**: Check INSTALLATION.md and ARCHITECTURE.md

### Recognition

All contributors will be:
- Listed in the project's contributors
- Mentioned in release notes for significant contributions
- Given credit in documentation for major features

## License

By contributing to MOSE, you agree that your contributions will be licensed under the GPL v3 license.

## Questions?

Don't hesitate to ask questions! Create an issue with the "question" label or start a discussion.

---

**Thank you for helping make MOSE better for everyone!** 🧿👁️
