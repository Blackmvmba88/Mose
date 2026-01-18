# Installation Guide

This guide provides detailed installation instructions for MOSE on different platforms.

## System Requirements

- **Python**: 3.9 or higher (tested on 3.9, 3.10, 3.11, 3.12)
- **Webcam**: Any standard USB or built-in webcam (minimum 480p, 30fps recommended)
- **Operating System**: Windows 10+, macOS 10.14+, or Linux (Ubuntu 20.04+)
- **RAM**: Minimum 4GB (8GB recommended)
- **Lighting**: Well-lit environment for best performance

## Quick Installation

```bash
# Clone the repository
git clone https://github.com/Blackmvmba88/Mose.git
cd Mose

# Install dependencies
pip install -r requirements.txt

# Run MOSE
python main.py
```

## Platform-Specific Installation

### Windows 10/11

1. **Install Python**
   - Download Python from [python.org](https://www.python.org/downloads/)
   - During installation, check "Add Python to PATH"
   - Verify installation: `python --version`

2. **Install dependencies**
   ```cmd
   pip install -r requirements.txt
   ```

3. **Camera permissions**
   - Go to Settings → Privacy → Camera
   - Enable camera access for desktop apps

4. **Run MOSE**
   ```cmd
   python main.py
   ```

**Common Windows Issues:**
- If `pip` is not found, use `python -m pip install -r requirements.txt`
- If camera doesn't open, check antivirus software isn't blocking camera access

### macOS (Intel & Apple Silicon)

1. **Install Python**
   ```bash
   # Using Homebrew (recommended)
   brew install python@3.11
   ```

2. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Camera permissions**
   - System Preferences → Security & Privacy → Camera
   - Grant camera access to Terminal or your Python IDE

4. **Run MOSE**
   ```bash
   python3 main.py
   ```

**Apple Silicon (M1/M2) Notes:**
- All dependencies work natively on ARM architecture
- If using Rosetta, ensure Python is ARM version for best performance

### Linux (Ubuntu/Debian)

1. **Install system dependencies**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   sudo apt install libopencv-dev python3-opencv
   sudo apt install portaudio19-dev  # For audio support
   ```

2. **Install Python dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Camera permissions**
   - Most distributions work out of the box
   - Add user to video group if needed:
     ```bash
     sudo usermod -a -G video $USER
     ```
   - Log out and back in for changes to take effect

4. **Run MOSE**
   ```bash
   python3 main.py
   ```

**Wayland Users:**
- PyAutoGUI may have issues on Wayland
- Try using X11 session or install: `pip3 install python-xlib`

### Linux (Fedora/RHEL)

```bash
# Install system dependencies
sudo dnf install python3 python3-pip
sudo dnf install opencv python3-opencv

# Install Python dependencies
pip3 install -r requirements.txt

# Run MOSE
python3 main.py
```

## Virtual Environment (Recommended)

Using a virtual environment keeps dependencies isolated:

```bash
# Create virtual environment
python -m venv mose_env

# Activate it
# On Windows:
mose_env\Scripts\activate
# On macOS/Linux:
source mose_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run MOSE
python main.py
```

## Verifying Installation

Run this test to verify all dependencies are working:

```python
python -c "import cv2, mediapipe, pyautogui, numpy; print('All dependencies OK!')"
```

Expected output: `All dependencies OK!`

## Troubleshooting

### Camera Issues

**Problem**: "Failed to read from camera" or black screen

**Solutions**:
1. Check if another application is using the camera
2. Try different camera index in code (change `cv2.VideoCapture(0)` to `1` or `2`)
3. Check camera drivers are installed and up to date
4. Verify camera works in other applications first

**Test camera**:
```python
import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
print("Camera working!" if ret else "Camera failed")
cap.release()
```

### Low FPS / Performance Issues

**Problem**: Laggy cursor movement, low frame rate

**Solutions**:
1. Ensure good lighting (face detection works better with good light)
2. Close other resource-intensive applications
3. Reduce `buffer_size` in code for more responsive (but less smooth) tracking
4. Use a lower resolution camera if available
5. Check CPU usage - should be under 50%

**Check FPS**:
- FPS counter is shown in terminal when running MOSE
- Aim for 25+ FPS for smooth experience

### MediaPipe Installation Issues

**Problem**: Error installing MediaPipe

**Solutions**:
```bash
# Try upgrading pip first
pip install --upgrade pip setuptools wheel

# Install MediaPipe specifically
pip install mediapipe==0.10.8

# If still failing, try without version pin
pip install mediapipe
```

### PyAutoGUI Not Moving Mouse

**Problem**: Cursor doesn't move even after calibration

**Solutions**:
1. **macOS**: Grant accessibility permissions
   - System Preferences → Security & Privacy → Accessibility
   - Add Terminal or Python to allowed apps

2. **Linux**: Install xdotool
   ```bash
   sudo apt install xdotool  # Ubuntu/Debian
   sudo dnf install xdotool  # Fedora
   ```

3. Check for PyAutoGUI fail-safes:
   ```python
   import pyautogui
   pyautogui.FAILSAFE = False  # Disable corner fail-safe if testing
   ```

### Calibration Not Working

**Problem**: Calibration doesn't capture points

**Solutions**:
1. Make sure your face is clearly visible and well-lit
2. Look directly at the yellow circles when pressing SPACE
3. Keep head relatively still during calibration
4. Try recalibrating (press 'c') if first attempt fails

### Import Errors

**Problem**: `ModuleNotFoundError: No module named 'mose'`

**Solutions**:
```bash
# Make sure you're in the MOSE directory
cd /path/to/Mose

# Run from project root
python main.py

# Or set PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:/path/to/Mose"  # Linux/macOS
set PYTHONPATH=%PYTHONPATH%;C:\path\to\Mose     # Windows
```

## Advanced Configuration

### Adjusting Sensitivity

Edit the code in `main.py` or use the modular version:

```python
# In main.py or when initializing components:

# Blink sensitivity (lower = easier to trigger clicks)
blink_detector = BlinkDetector(threshold=0.0045, cooldown=0.3)

# Smoothing (higher = smoother but less responsive)
gaze_mapper = GazeToCursor(screen_w, screen_h, buffer_size=8)

# Face detection confidence
face_detector = FaceDetector(
    min_detection_confidence=0.5,  # 0.0 to 1.0
    min_tracking_confidence=0.5    # 0.0 to 1.0
)
```

### Multiple Camera Setup

If you have multiple cameras:

```python
# Test different camera indices
for i in range(4):
    cap = cv2.VideoCapture(i)
    if cap.isOpened():
        print(f"Camera {i}: Available")
        cap.release()
```

Then update the camera index in code.

## Getting Help

If you continue to have issues:

1. Check the [GitHub Issues](https://github.com/Blackmvmba88/Mose/issues)
2. Create a new issue with:
   - Your OS and Python version
   - Error messages (full traceback)
   - Camera specs
   - What you've already tried

## Next Steps

After successful installation:
1. Read the [README.md](README.md) for usage instructions
2. Check [ARCHITECTURE.md](ARCHITECTURE.md) to understand how MOSE works
3. Run calibration and start controlling your computer with your eyes!
