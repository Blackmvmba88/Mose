# Quick Start Guide

## Which version should I use?

MOSE comes in two versions:

### 1. `main.py` - Original Version
- ✅ Simple, single-file implementation
- ✅ Easy to understand and modify
- ✅ Works out of the box

### 2. `main_modular.py` - Modular Version
- ✅ Better code organization
- ✅ Easier to extend and maintain
- ✅ Supports configuration file (`config.ini`)
- ✅ More professional structure

**Both versions work identically!** Choose based on your needs:
- **Learning/Quick testing?** → Use `main.py`
- **Development/Contributing?** → Use `main_modular.py`

## Running MOSE

```bash
# Original version
python main.py

# OR modular version
python main_modular.py
```

## First Time Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Test your camera**:
   ```bash
   python -c "import cv2; cap = cv2.VideoCapture(0); ret, _ = cap.read(); print('Camera OK!' if ret else 'Camera FAILED'); cap.release()"
   ```

3. **Run MOSE**:
   ```bash
   python main.py
   ```

4. **Calibrate**:
   - Press `c` to start calibration
   - Look at each yellow circle and press SPACE
   - Complete all 5 points

5. **Use**:
   - Move your eyes to move the cursor
   - Blink quickly to click

## Troubleshooting

### "Failed to read from camera"
- Check if another app is using the camera
- Try changing `camera_index` in `config.ini` (0, 1, or 2)
- Verify camera permissions in your OS settings

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt
```

### Cursor is too jittery
Edit `config.ini`:
```ini
[gaze]
smoothing_buffer_size = 12  # Increase for smoother (was 8)
```

### Clicks are too sensitive
Edit `config.ini`:
```ini
[blink]
threshold = 0.005  # Increase to make harder to trigger (was 0.0045)
```

### Cursor is too slow
Edit `config.ini`:
```ini
[gaze]
smoothing_buffer_size = 4  # Decrease for faster response (was 8)
```

## Tips for Best Performance

1. **Lighting**: Face should be well-lit, no backlight
2. **Distance**: 40-80cm from camera
3. **Angle**: Look straight at the camera
4. **Stability**: Keep head relatively still during use
5. **Environment**: Quiet, minimal distractions

## Next Steps

- Read [INSTALLATION.md](INSTALLATION.md) for detailed setup
- Read [ARCHITECTURE.md](ARCHITECTURE.md) to understand how it works
- Check [CONTRIBUTING.md](CONTRIBUTING.md) to contribute
- Report issues at [GitHub Issues](https://github.com/Blackmvmba88/Mose/issues)

---

**Happy eye tracking!** 🧿👁️
