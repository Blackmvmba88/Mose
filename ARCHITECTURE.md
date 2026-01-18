# MOSE Architecture Documentation

## Overview

MOSE (Mouse by Eye System) is an eye-tracking based cursor control system built using computer vision and real-time face mesh detection. This document explains the technical architecture and pipeline.

## System Pipeline

The MOSE system follows this processing pipeline:

```
┌─────────────┐
│   CAMERA    │ 30+ FPS video stream
│   CAPTURE   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    FACE     │ MediaPipe Face Mesh
│  DETECTION  │ 478 facial landmarks
└──────┬──────┘
       │
       ▼
┌─────────────┐
│     EYE     │ Track iris positions
│  TRACKING   │ Landmarks: 468 (left), 473 (right)
└──────┬──────┘
       │
       ├──────────────────────┐
       │                      │
       ▼                      ▼
┌─────────────┐      ┌──────────────┐
│    GAZE     │      │    BLINK     │
│  TO CURSOR  │      │  DETECTION   │
└──────┬──────┘      └──────┬───────┘
       │                     │
       │ Map to screen       │ Eye aspect ratio
       │ Apply smoothing     │ < threshold
       │                     │
       ▼                     ▼
┌─────────────┐      ┌──────────────┐
│   CURSOR    │      │    CLICK     │
│  MOVEMENT   │      │    EVENT     │
└─────────────┘      └──────────────┘
```

## Core Components

### 1. Face Detection (`face_detection.py`)

**Technology**: MediaPipe Face Mesh

**Purpose**: Detect and track facial landmarks in real-time

**Key Features**:
- Detects up to 478 3D facial landmarks
- Refine mode enabled for accurate iris tracking
- Tracks through head movements and rotations
- Confidence thresholds: 0.5 for detection and tracking

**Landmarks Used**:
- Iris centers: 468 (left eye), 473 (right eye)
- Eye regions: 16 points per eye for blink detection

**Performance**:
- Runs at 30+ FPS on standard hardware
- CPU-based processing (no GPU required)
- Latency: ~30-50ms per frame

### 2. Eye Tracking (`eye_tracking.py`)

**Purpose**: Extract eye and iris positions from facial landmarks

**Iris Position Calculation**:
```python
# Average of left and right iris centers
avg_x = (left_iris.x + right_iris.x) / 2
avg_y = (left_iris.y + right_iris.y) / 2
```

**Eye Aspect Ratio (EAR)**:
```python
# Vertical distance between top and bottom of eye
# Used for blink detection
EAR = ||top_landmark - bottom_landmark||
```

**Coordinate System**:
- MediaPipe outputs normalized coordinates [0, 1]
- Origin: top-left corner of frame
- Independent of camera resolution

### 3. Blink Detection (`blink_detector.py`)

**Algorithm**: Eye Aspect Ratio (EAR) Thresholding

**Temporal Parameters**:
- **Threshold**: 0.0045 (empirically determined)
  - Below this value = eye is closed
  - Typical open eye: 0.008-0.015
  - Typical closed eye: 0.001-0.004
  
- **Cooldown**: 0.3 seconds
  - Prevents multiple clicks from single blink
  - Allows ~3 clicks per second maximum
  - Reduces false positives from natural blinking

**Detection Logic**:
```python
if eye_ratio < threshold:
    if time_since_last_click > cooldown:
        register_click()
        reset_timer()
```

**False Positive Prevention**:
- Cooldown period between clicks
- Single-eye monitoring (more reliable than both eyes)
- Threshold tuned to distinguish intentional blinks from natural eye movements

### 4. Calibration (`calibration.py`)

**Purpose**: Map user's eye movement range to screen coordinates

**5-Point Calibration**:
```
(0.1, 0.1)    ━━━━━    (0.9, 0.1)
                │
                │
                │ (0.5, 0.5)
                │
                │
(0.1, 0.9)    ━━━━━    (0.9, 0.9)
```

**Process**:
1. User looks at top-left corner → press SPACE
2. User looks at top-right corner → press SPACE
3. User looks at bottom-left corner → press SPACE
4. User looks at bottom-right corner → press SPACE
5. User looks at center → press SPACE

**Calibration Range Calculation**:
```python
min_x = min(all_collected_x_values)
max_x = max(all_collected_x_values)
min_y = min(all_collected_y_values)
max_y = max(all_collected_y_values)
```

This establishes the personal eye movement range for each user.

### 5. Gaze to Cursor Mapping (`gaze_to_cursor.py`)

**Purpose**: Convert eye gaze coordinates to screen cursor position

**Normalization**:
```python
# Map calibrated eye range [min, max] to screen range [0, 1]
normalized_x = (gaze_x - min_x) / (max_x - min_x)
normalized_y = (gaze_y - min_y) / (max_y - min_y)

# Clamp to ensure valid range
normalized_x = clamp(normalized_x, 0, 1)
normalized_y = clamp(normalized_y, 0, 1)

# Map to screen pixels
screen_x = normalized_x * screen_width
screen_y = normalized_y * screen_height
```

**Smoothing Algorithm**: Moving Average Filter

```python
# Add current position to buffer
smooth_buffer_x.append(normalized_x)
smooth_buffer_y.append(normalized_y)

# Keep only last N positions
if len(smooth_buffer_x) > buffer_size:
    smooth_buffer_x.pop(0)
    smooth_buffer_y.pop(0)

# Calculate average
smooth_x = sum(smooth_buffer_x) / len(smooth_buffer_x)
smooth_y = sum(smooth_buffer_y) / len(smooth_buffer_y)
```

**Buffer Size**: 8 frames (default)
- Higher = smoother but less responsive
- Lower = more responsive but jittery
- 8 frames ≈ 250ms lag at 30 FPS

**Why Moving Average?**
- Simple and fast (O(1) per frame)
- Predictable behavior
- Good balance of smoothness vs responsiveness

**Future Improvement**: Kalman Filter
- Better prediction of movement
- Accounts for velocity and acceleration
- Reduces jitter while maintaining responsiveness

### 6. Visual Feedback (`feedback_overlay.py`)

**Purpose**: Provide real-time visual feedback to the user

**Feedback Elements**:
- **Calibration targets**: Yellow circles showing where to look
- **Iris markers**: Green dots showing detected iris positions
- **Click indicator**: "CLICK!" text flash on blink
- **Instructions**: On-screen keyboard shortcuts
- **Status messages**: Progress updates

**OpenCV Drawing**:
```python
cv2.circle(image, center, radius, color, thickness)
cv2.putText(image, text, position, font, scale, color, thickness)
```

## Data Flow

### Initialization Phase

```
User starts MOSE
    ↓
Initialize camera (CV2)
    ↓
Initialize MediaPipe Face Mesh
    ↓
Initialize all components (trackers, detectors, mappers)
    ↓
Display instructions
    ↓
Wait for user input
```

### Calibration Phase

```
User presses 'c'
    ↓
Show calibration target 1/5
    ↓
User looks at target + presses SPACE
    ↓
Capture iris position
    ↓
Repeat for targets 2-5
    ↓
Calculate min/max range
    ↓
Configure gaze mapper
    ↓
Enter tracking mode
```

### Tracking Phase (Main Loop)

```
┌─────────────────────────────────────┐
│  Capture frame from camera          │
│  Flip horizontally (mirror mode)    │
└─────────────┬───────────────────────┘
              ↓
┌─────────────────────────────────────┐
│  Convert BGR → RGB                   │
│  Process with MediaPipe              │
└─────────────┬───────────────────────┘
              ↓
         Face detected?
              │
        Yes ──┴── No → Continue
              │
              ↓
┌─────────────────────────────────────┐
│  Extract iris position               │
│  Calculate eye aspect ratio          │
└─────────────┬───────────────────────┘
              │
              ├──────────────────┐
              ↓                  ↓
┌──────────────────────┐  ┌───────────────┐
│  Map to screen       │  │ Check blink?  │
│  Apply smoothing     │  └───────┬───────┘
│  Move cursor         │          │
└──────────────────────┘     Yes ─┴─ No
                              ↓
                       ┌──────────────┐
                       │ pyautogui.   │
                       │ click()      │
                       └──────────────┘
```

## Technical Specifications

### Performance Metrics

| Metric | Target | Typical |
|--------|--------|---------|
| Frame Rate | 30 FPS | 30-60 FPS |
| Latency (gaze → cursor) | <100ms | 50-80ms |
| CPU Usage | <30% | 15-25% |
| RAM Usage | <500MB | 200-400MB |
| Calibration Time | <2 min | 30-60 sec |

### Accuracy Metrics

| Metric | Description | Expected Value |
|--------|-------------|----------------|
| Precision | Cursor stability on fixed gaze | ±50px radius |
| Tracking Coverage | % of screen reachable | 95-100% |
| False Positive (clicks) | Unintended clicks | <5% |
| False Negative (clicks) | Missed intentional blinks | <10% |

### Models Used

**MediaPipe Face Mesh**:
- Model type: TensorFlow Lite (TFLite)
- Architecture: Lightweight CNN-based
- Landmarks: 478 points (468 face + 10 iris)
- Model size: ~10MB
- License: Apache 2.0

**No custom ML models**:
- All processing uses rule-based algorithms
- No training required
- Deterministic behavior

## Coordinate Systems

### Camera Space
- Origin: Top-left corner
- Range: [0, 1] normalized
- Axes: X (left→right), Y (top→bottom)

### Screen Space
- Origin: Top-left corner
- Range: [0, screen_width], [0, screen_height] pixels
- Axes: X (left→right), Y (top→bottom)

### Face Mesh Space
- 3D coordinates with depth
- Normalized to face bounding box
- Z-axis (depth) not used in MOSE

## Configuration Parameters

### Tunable Parameters

```python
# Face Detection
min_detection_confidence = 0.5  # Range: 0.0-1.0
min_tracking_confidence = 0.5   # Range: 0.0-1.0

# Blink Detection
blink_threshold = 0.0045        # Range: 0.003-0.006
click_cooldown = 0.3            # Seconds

# Gaze Mapping
smoothing_buffer_size = 8       # Range: 4-16 frames

# Calibration
calibration_points = 5          # Fixed at 5 points
```

### Effect of Parameter Changes

**Increasing `blink_threshold`**:
- ✅ Fewer false positive clicks
- ❌ Harder to trigger intentional clicks

**Increasing `smoothing_buffer_size`**:
- ✅ Smoother cursor movement
- ❌ More lag in response

**Increasing confidence thresholds**:
- ✅ More stable tracking
- ❌ More frequent tracking loss

## Security & Privacy

**Data Processing**:
- ✅ All processing done locally
- ✅ No data sent to external servers
- ✅ No video/image storage
- ✅ No telemetry or analytics

**Camera Access**:
- Only used during application runtime
- Released immediately on exit
- No background access

## Future Enhancements

### Planned Improvements

1. **Kalman Filtering**: Replace moving average with Kalman filter for better prediction
2. **Multi-monitor Support**: Detect and handle multiple displays
3. **Gesture Recognition**: Additional eye gestures (double blink, wink)
4. **Adaptive Calibration**: Background recalibration during use
5. **Dead Zones**: Configurable screen regions with no cursor movement
6. **Velocity-based Smoothing**: Less smoothing for fast movements

### Research Directions

1. **Fitts' Law Analysis**: Measure time-to-target performance
2. **Drift Compensation**: Automatic correction for calibration drift
3. **Fatigue Detection**: Monitor eye strain indicators
4. **Personalization**: User-specific models that improve over time

## References

- MediaPipe Face Mesh: https://google.github.io/mediapipe/solutions/face_mesh
- Eye Aspect Ratio: Soukupová and Čech (2016) "Real-Time Eye Blink Detection"
- Gaze Tracking: Papoutsaki et al. (2016) "WebGazer: Scalable Webcam Eye Tracking"

## Glossary

- **EAR**: Eye Aspect Ratio - metric for eye openness
- **FPS**: Frames Per Second - video processing rate
- **Landmark**: Specific point on face detected by MediaPipe
- **Iris**: Colored part of eye, used as gaze indicator
- **Normalized coordinates**: Values scaled to [0, 1] range
- **Smoothing buffer**: Circular buffer storing recent positions
- **Cooldown**: Minimum time between repeated actions
