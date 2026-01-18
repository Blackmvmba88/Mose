# GitHub Labels for MOSE Project

This document describes the labeling system used for issues and pull requests.

## Label Categories

### Type Labels
- **`bug`** 🐛 - Something isn't working correctly
- **`enhancement`** ✨ - New feature or improvement request
- **`documentation`** 📚 - Documentation improvements or additions
- **`question`** ❓ - Questions about usage or functionality

### Priority Labels
- **`priority: high`** 🔴 - Critical issues that need immediate attention
- **`priority: medium`** 🟡 - Important but not urgent
- **`priority: low`** 🟢 - Nice to have, low urgency

### Status Labels
- **`status: in-progress`** 🚧 - Currently being worked on
- **`status: blocked`** 🚫 - Blocked by another issue or dependency
- **`status: needs-review`** 👀 - Needs review from maintainers
- **`status: ready`** ✅ - Ready to be worked on

### Area Labels
- **`area: core`** - Core functionality (face detection, eye tracking, blink detection)
- **`area: ui`** - User interface and visual feedback
- **`area: calibration`** - Calibration system
- **`area: config`** - Configuration and settings
- **`area: docs`** - Documentation (README, guides, etc.)
- **`area: performance`** - Performance optimization
- **`area: testing`** - Testing infrastructure

### Technical Labels
- **`accessibility`** ♿ - Related to accessibility features
- **`assistive-technology`** - Assistive technology improvements
- **`computer-vision`** 👁️ - Computer vision algorithms
- **`hci`** - Human-computer interaction
- **`eye-tracking`** - Eye tracking specific features
- **`gaze-tracking`** - Gaze tracking functionality

### Special Labels
- **`good first issue`** 🌱 - Good for newcomers to the project
- **`help wanted`** 🙋 - Extra attention needed from contributors
- **`wontfix`** - This will not be worked on
- **`duplicate`** - Duplicate of another issue
- **`invalid`** - Not a valid issue

## Usage Guidelines

### For Issue Reporters
When creating an issue:
1. Use the appropriate template (bug, feature, question)
2. The template will suggest initial labels
3. Maintainers will add additional labels as needed

### For Contributors
When working on an issue:
1. Self-assign the issue
2. Add `status: in-progress` label
3. Remove when PR is submitted, add `status: needs-review`

### For Maintainers
When triaging issues:
1. Add **type** label (bug, enhancement, etc.)
2. Add **area** label to categorize
3. Add **priority** if urgent
4. Add **good first issue** if suitable for beginners
5. Update **status** labels as work progresses

## Examples

**Bug Report**:
```
Labels: bug, area: core, priority: high
```

**Feature Request**:
```
Labels: enhancement, area: ui, help wanted
```

**Documentation Improvement**:
```
Labels: documentation, good first issue
```

**Accessibility Feature**:
```
Labels: enhancement, accessibility, assistive-technology, area: ui
```

## Setting Up Labels

To create these labels in your repository:

```bash
# Create label with name, color, and description
gh label create "bug" --color d73a4a --description "Something isn't working"
gh label create "enhancement" --color a2eeef --description "New feature or request"
# ... etc
```

Or use the GitHub web interface:
1. Go to Issues → Labels
2. Click "New label"
3. Enter name, description, and color
4. Click "Create label"

## Color Scheme

- 🔴 Red (`d73a4a`): Bugs, critical issues
- 🟢 Green (`0e8a16`): Low priority, ready to work
- 🔵 Blue (`0075ca`): Information, documentation
- 🟡 Yellow (`fbca04`): Medium priority, warnings
- 🟣 Purple (`7057ff`): Technical, advanced
- ⚪ Gray (`e4e4e4`): Status, meta

---

This labeling system helps organize and prioritize work on MOSE, making it easier for contributors to find issues they can help with and for maintainers to manage the project effectively.
