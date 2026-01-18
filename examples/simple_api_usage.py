"""
MOSE Events API - Simple Example

This example demonstrates the basic usage of the MOSE events API.
It listens to eye-tracking events and prints them to the console.

Usage:
    python examples/simple_api_usage.py
"""

from mose import events

def main():
    """
    Simple example: print all events as they occur
    """
    print("🧿 MOSE Events API - Simple Example")
    print("=" * 50)
    print("Starting event stream...")
    print("Press Ctrl+C to stop\n")
    
    try:
        # Create an event stream
        # This will start the camera and begin tracking
        for event in events():
            # Print event information
            print(f"[{event.timestamp:.2f}] {event.type}")
            
            # Handle specific event types
            if event.type == "face_detected":
                print("  ✓ Face detected - tracking started")
            
            elif event.type == "face_lost":
                print("  ✗ Face lost - tracking paused")
            
            elif event.type == "gaze_move":
                pos = event.data.get("position")
                if pos:
                    print(f"  → Gaze moved to: ({pos[0]}, {pos[1]})")
            
            elif event.type == "blink_detected":
                print("  👁 Blink detected")
            
            elif event.type == "blink_click":
                pos = event.data.get("position")
                print(f"  🖱️ CLICK at position: ({pos[0]}, {pos[1]})")
            
            elif event.type == "error":
                error_msg = event.data.get("error", "Unknown error")
                print(f"  ❌ Error: {error_msg}")
    
    except KeyboardInterrupt:
        print("\n\nStopping MOSE...")
        print("✓ Done!")

if __name__ == "__main__":
    main()
