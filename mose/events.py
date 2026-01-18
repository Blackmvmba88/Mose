"""
MOSE Events API

This module provides a simple event-based API for consuming MOSE eye-tracking events.
External applications can use this to integrate eye-tracking functionality.

Example usage:
    from mose import EventStream

    # Create event stream from webcam
    stream = EventStream()
    
    # Process events
    for event in stream:
        if event.type == "blink_click":
            print(f"Click detected at: {event.data['position']}")
        elif event.type == "gaze_move":
            print(f"Gaze moved to: {event.data['position']}")
        elif event.type == "calibration_complete":
            print("Calibration completed!")
"""

from enum import Enum
from dataclasses import dataclass
from typing import Any, Dict, Optional, Iterator
import time


class EventType(Enum):
    """Types of events that MOSE can generate"""
    GAZE_MOVE = "gaze_move"           # Cursor movement from gaze
    BLINK_CLICK = "blink_click"       # Click from blink detection
    BLINK_DETECTED = "blink_detected" # Raw blink detection (before click)
    CALIBRATION_START = "calibration_start"
    CALIBRATION_POINT = "calibration_point"
    CALIBRATION_COMPLETE = "calibration_complete"
    FACE_DETECTED = "face_detected"
    FACE_LOST = "face_lost"
    ERROR = "error"


@dataclass
class Event:
    """
    Represents a single MOSE event
    
    Attributes:
        type: The type of event as a string (value from EventType enum)
        timestamp: Unix timestamp when event occurred
        data: Dictionary containing event-specific data
    """
    type: str
    timestamp: float
    data: Dict[str, Any]
    
    def __repr__(self):
        return f"Event(type={self.type}, timestamp={self.timestamp}, data={self.data})"


class EventStream:
    """
    Main event stream interface for MOSE
    
    This class provides an iterator interface for consuming eye-tracking events.
    It wraps the core MOSE functionality and exposes it as a simple event stream.
    
    Args:
        camera_index: Camera device index (default: 0)
        smoothing: Enable cursor smoothing (default: True)
        mirror_mode: Mirror the camera feed (default: True)
    
    Example:
        stream = EventStream()
        for event in stream:
            if event.type == "blink_click":
                print("Click!")
    """
    
    def __init__(
        self,
        camera_index: int = 0,
        smoothing: bool = True,
        mirror_mode: bool = True,
        auto_calibrate: bool = False
    ):
        self.camera_index = camera_index
        self.smoothing = smoothing
        self.mirror_mode = mirror_mode
        self.auto_calibrate = auto_calibrate
        self._running = False
        
    def __iter__(self) -> Iterator[Event]:
        """
        Make EventStream iterable
        
        Yields:
            Event objects as they occur
        """
        self._running = True
        
        # Import here to avoid circular dependencies
        try:
            import cv2
            from mose.core.face_detection import FaceDetector
            from mose.core.eye_tracking import EyeTracker
            from mose.core.blink_detector import BlinkDetector
            from mose.core.gaze_to_cursor import GazeToCursor
            from mose.ui.calibration import CalibrationSystem
        except ImportError as e:
            yield Event(
                type=EventType.ERROR.value,
                timestamp=time.time(),
                data={"error": str(e), "message": "Failed to import MOSE modules"}
            )
            return
        
        # Initialize components
        cap = cv2.VideoCapture(self.camera_index)
        if not cap.isOpened():
            yield Event(
                type=EventType.ERROR.value,
                timestamp=time.time(),
                data={"error": "Camera not available", "camera_index": self.camera_index}
            )
            return
        
        face_detector = FaceDetector()
        eye_tracker = EyeTracker()
        blink_detector = BlinkDetector()
        gaze_mapper = GazeToCursor(smoothing_enabled=self.smoothing)
        calibration = CalibrationSystem()
        
        face_was_detected = False
        last_gaze_position = None
        
        try:
            while self._running:
                ret, frame = cap.read()
                if not ret:
                    yield Event(
                        type=EventType.ERROR.value,
                        timestamp=time.time(),
                        data={"error": "Failed to read frame from camera"}
                    )
                    break
                
                if self.mirror_mode:
                    frame = cv2.flip(frame, 1)
                
                # Detect face
                face_landmarks = face_detector.detect(frame)
                
                if face_landmarks is not None:
                    # Face detected event
                    if not face_was_detected:
                        face_was_detected = True
                        yield Event(
                            type=EventType.FACE_DETECTED.value,
                            timestamp=time.time(),
                            data={}
                        )
                    
                    # Track eyes
                    iris_data = eye_tracker.track(frame, face_landmarks)
                    
                    if iris_data:
                        # Check for blinks
                        blink_detected = blink_detector.detect_blink(iris_data)
                        
                        if blink_detected:
                            yield Event(
                                type=EventType.BLINK_DETECTED.value,
                                timestamp=time.time(),
                                data={"iris_data": iris_data}
                            )
                        
                        # Map gaze to cursor (if calibrated)
                        if calibration.is_calibrated():
                            cursor_pos = gaze_mapper.map_gaze_to_cursor(
                                iris_data["left_iris_center"],
                                iris_data["right_iris_center"],
                                calibration.calibration_data
                            )
                            
                            if cursor_pos != last_gaze_position:
                                yield Event(
                                    type=EventType.GAZE_MOVE.value,
                                    timestamp=time.time(),
                                    data={"position": cursor_pos}
                                )
                                last_gaze_position = cursor_pos
                            
                            # Generate click event if appropriate
                            if blink_detected and blink_detector.should_click():
                                yield Event(
                                    type=EventType.BLINK_CLICK.value,
                                    timestamp=time.time(),
                                    data={"position": cursor_pos}
                                )
                else:
                    # Face lost event
                    if face_was_detected:
                        face_was_detected = False
                        yield Event(
                            type=EventType.FACE_LOST.value,
                            timestamp=time.time(),
                            data={}
                        )
                
        except Exception as e:
            yield Event(
                type=EventType.ERROR.value,
                timestamp=time.time(),
                data={"error": str(e), "exception_type": type(e).__name__}
            )
        finally:
            cap.release()
    
    def stop(self):
        """Stop the event stream"""
        self._running = False


def events(camera_index: int = 0, **kwargs) -> EventStream:
    """
    Convenience function to create an event stream
    
    Args:
        camera_index: Camera device index (default: 0)
        **kwargs: Additional arguments passed to EventStream
    
    Returns:
        EventStream object ready to iterate
    
    Example:
        from mose import events
        
        for e in events():
            if e.type == "blink_click":
                print("Click detected!")
    """
    return EventStream(camera_index=camera_index, **kwargs)
