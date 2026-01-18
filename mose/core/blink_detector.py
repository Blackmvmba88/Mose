"""
Blink detection module for click events.
"""

import time


class BlinkDetector:
    """
    Detects eye blinks based on eye aspect ratio.
    
    Uses temporal parameters to filter intentional blinks from
    natural eye movements.
    """
    
    def __init__(self, threshold=0.0045, cooldown=0.3):
        """
        Initialize the blink detector.
        
        Args:
            threshold: Eye aspect ratio threshold for blink detection.
                      Lower values indicate closed eyes. Default: 0.0045
            cooldown: Minimum time (seconds) between consecutive clicks
                     to avoid accidental multiple clicks. Default: 0.3s
        """
        self.threshold = threshold
        self.cooldown = cooldown
        self.last_click_time = 0
    
    def detect_blink(self, eye_ratio):
        """
        Detect if a blink occurred based on eye aspect ratio.
        
        Args:
            eye_ratio: Current eye aspect ratio from EyeTracker
            
        Returns:
            bool: True if a blink was detected and cooldown has passed
        """
        current_time = time.time()
        
        # Check if eye is closed (below threshold) and cooldown has passed
        if eye_ratio < self.threshold:
            if current_time - self.last_click_time > self.cooldown:
                self.last_click_time = current_time
                return True
        
        return False
    
    def reset_cooldown(self):
        """Reset the click cooldown timer."""
        self.last_click_time = time.time()
