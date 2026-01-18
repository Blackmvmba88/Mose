"""
MOSE Events API - Custom Integration Example

This example shows how to integrate MOSE with a custom application.
It demonstrates filtering events and triggering custom actions.

Usage:
    python examples/custom_integration.py
"""

from mose import EventStream, EventType
import time

class CustomApp:
    """
    Example custom application that uses MOSE for eye-tracking input
    """
    
    def __init__(self):
        self.click_count = 0
        self.last_position = None
        self.session_start = time.time()
        
    def on_click(self, position):
        """Handle click events"""
        self.click_count += 1
        print(f"🖱️  Click #{self.click_count} at {position}")
        
        # Add your custom logic here
        # For example: trigger an action, send to API, update UI, etc.
        
    def on_gaze_move(self, position):
        """Handle gaze movement"""
        self.last_position = position
        # Add your custom logic here
        # For example: update cursor, highlight UI elements, etc.
        
    def on_face_lost(self):
        """Handle face lost event"""
        print("⚠️  Face lost - pausing interactions")
        # Add your custom logic here
        # For example: pause application, show warning, etc.
        
    def on_face_detected(self):
        """Handle face detected event"""
        print("✓ Face detected - resuming interactions")
        # Add your custom logic here
        
    def get_stats(self):
        """Get session statistics"""
        elapsed = time.time() - self.session_start
        return {
            "clicks": self.click_count,
            "session_duration": elapsed,
            "clicks_per_minute": (self.click_count / elapsed) * 60 if elapsed > 0 else 0,
        }

def main():
    """
    Run the custom application with MOSE integration
    """
    print("🧿 MOSE Custom Integration Example")
    print("=" * 50)
    print("Running custom app with eye-tracking...")
    print("Press Ctrl+C to stop\n")
    
    app = CustomApp()
    
    try:
        # Create event stream with custom settings
        stream = EventStream(
            camera_index=0,
            smoothing=True,
            mirror_mode=True
        )
        
        for event in stream:
            # Route events to appropriate handlers
            if event.type == EventType.BLINK_CLICK.value:
                position = event.data.get("position")
                app.on_click(position)
            
            elif event.type == EventType.GAZE_MOVE.value:
                position = event.data.get("position")
                app.on_gaze_move(position)
            
            elif event.type == EventType.FACE_DETECTED.value:
                app.on_face_detected()
            
            elif event.type == EventType.FACE_LOST.value:
                app.on_face_lost()
            
            elif event.type == EventType.ERROR.value:
                error = event.data.get("error")
                print(f"❌ Error: {error}")
    
    except KeyboardInterrupt:
        print("\n\n" + "=" * 50)
        print("Session Statistics:")
        stats = app.get_stats()
        print(f"  Total clicks: {stats['clicks']}")
        print(f"  Duration: {stats['session_duration']:.1f} seconds")
        print(f"  Clicks/minute: {stats['clicks_per_minute']:.1f}")
        print("\n✓ Done!")

if __name__ == "__main__":
    main()
