"""
Tests for MOSE Events API

This module tests the events API functionality without requiring a camera.
"""

import pytest
from mose.events import Event, EventType, EventStream
import time


class TestEvent:
    """Test the Event dataclass"""
    
    def test_event_creation(self):
        """Test creating an Event object"""
        event = Event(
            type="test_event",
            timestamp=time.time(),
            data={"key": "value"}
        )
        assert event.type == "test_event"
        assert isinstance(event.timestamp, float)
        assert event.data["key"] == "value"
    
    def test_event_repr(self):
        """Test Event string representation"""
        event = Event(
            type="test",
            timestamp=1234567890.0,
            data={"test": True}
        )
        repr_str = repr(event)
        assert "Event" in repr_str
        assert "test" in repr_str
        assert "1234567890.0" in repr_str


class TestEventType:
    """Test the EventType enum"""
    
    def test_event_types_exist(self):
        """Test that all expected event types exist"""
        expected_types = [
            "gaze_move",
            "blink_click",
            "blink_detected",
            "calibration_start",
            "calibration_point",
            "calibration_complete",
            "face_detected",
            "face_lost",
            "error"
        ]
        
        for event_type in expected_types:
            # Check that the event type exists in the enum
            found = False
            for et in EventType:
                if et.value == event_type:
                    found = True
                    break
            assert found, f"EventType.{event_type} not found"
    
    def test_event_type_values(self):
        """Test accessing EventType enum values"""
        assert EventType.GAZE_MOVE.value == "gaze_move"
        assert EventType.BLINK_CLICK.value == "blink_click"
        assert EventType.FACE_DETECTED.value == "face_detected"
        assert EventType.FACE_LOST.value == "face_lost"
        assert EventType.ERROR.value == "error"


class TestEventStream:
    """Test the EventStream class"""
    
    def test_event_stream_initialization(self):
        """Test creating an EventStream object"""
        stream = EventStream(
            camera_index=0,
            smoothing=True,
            mirror_mode=True
        )
        assert stream.camera_index == 0
        assert stream.smoothing == True
        assert stream.mirror_mode == True
        assert stream._running == False
    
    def test_event_stream_with_custom_settings(self):
        """Test EventStream with custom settings"""
        stream = EventStream(
            camera_index=1,
            smoothing=False,
            mirror_mode=False
        )
        assert stream.camera_index == 1
        assert stream.smoothing == False
        assert stream.mirror_mode == False
    
    def test_event_stream_stop(self):
        """Test stopping the event stream"""
        stream = EventStream()
        stream._running = True
        stream.stop()
        assert stream._running == False


class TestEventsFunction:
    """Test the convenience events() function"""
    
    def test_events_function_returns_stream(self):
        """Test that events() returns an EventStream"""
        from mose.events import events
        stream = events(camera_index=0)
        assert isinstance(stream, EventStream)
        assert stream.camera_index == 0
    
    def test_events_function_with_kwargs(self):
        """Test events() with keyword arguments"""
        from mose.events import events
        stream = events(
            camera_index=1,
            smoothing=False,
            mirror_mode=False
        )
        assert stream.camera_index == 1
        assert stream.smoothing == False
        assert stream.mirror_mode == False


class TestEventsIntegration:
    """Integration tests for events API"""
    
    def test_imports_work(self):
        """Test that all public API imports work"""
        from mose import EventStream, EventType
        from mose.events import events
        
        # Verify classes/functions are accessible
        assert EventStream is not None
        assert EventType is not None
        assert events is not None
        assert callable(events)
    
    def test_event_stream_is_iterable(self):
        """Test that EventStream is iterable (has __iter__)"""
        stream = EventStream()
        assert hasattr(stream, '__iter__')
        assert callable(getattr(stream, '__iter__'))


# Note: We cannot test the actual camera-based event generation without hardware
# Those tests should be done manually or with integration tests on real hardware
