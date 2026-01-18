"""
MOSE - Mouse by Eye System
Eye-tracking based mouse control system
"""

__version__ = "1.1.0"

# Export events API for external use
from mose.events import EventStream, EventType

__all__ = ["EventStream", "EventType", "__version__"]
