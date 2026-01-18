"""
MOSE Events API - Click Logger Example

This example demonstrates logging all click events to a file.
Useful for tracking user interactions or debugging.

Usage:
    python examples/click_logger.py
"""

import json
from datetime import datetime
from mose import events, EventType

def main():
    """
    Log all blink-click events to a JSON file
    """
    print("🧿 MOSE Click Logger")
    print("=" * 50)
    print("Logging all clicks to 'clicks.json'")
    print("Press Ctrl+C to stop\n")
    
    clicks = []
    
    try:
        for event in events():
            # Only process click events
            if event.type == EventType.BLINK_CLICK.value:
                click_data = {
                    "timestamp": event.timestamp,
                    "datetime": datetime.fromtimestamp(event.timestamp).isoformat(),
                    "position": event.data.get("position"),
                }
                
                clicks.append(click_data)
                print(f"Click #{len(clicks)} at {click_data['position']}")
                
                # Save to file after each click
                with open("clicks.json", "w") as f:
                    json.dump(clicks, f, indent=2)
    
    except KeyboardInterrupt:
        print(f"\n\nLogged {len(clicks)} clicks to 'clicks.json'")
        print("✓ Done!")

if __name__ == "__main__":
    main()
