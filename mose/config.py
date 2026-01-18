"""
Configuration loader for MOSE.
Reads settings from config.ini file.
"""

import configparser
import os


class Config:
    """Configuration manager for MOSE settings."""
    
    def __init__(self, config_file='config.ini'):
        """
        Load configuration from file.
        
        Args:
            config_file: Path to configuration file
        """
        self.config = configparser.ConfigParser()
        
        # Set defaults
        self._set_defaults()
        
        # Try to load config file
        if os.path.exists(config_file):
            self.config.read(config_file)
        else:
            print(f"⚠️  Config file '{config_file}' not found. Using defaults.")
    
    def _set_defaults(self):
        """Set default configuration values."""
        # Detection defaults
        self.config['detection'] = {
            'min_detection_confidence': '0.5',
            'min_tracking_confidence': '0.5'
        }
        
        # Blink defaults
        self.config['blink'] = {
            'threshold': '0.0045',
            'cooldown': '0.3'
        }
        
        # Gaze defaults
        self.config['gaze'] = {
            'smoothing_buffer_size': '8'
        }
        
        # Camera defaults
        self.config['camera'] = {
            'camera_index': '0'
        }
        
        # UI defaults
        self.config['ui'] = {
            'show_iris_markers': 'true',
            'show_instructions': 'true',
            'click_feedback_frames': '10'
        }
    
    def get_float(self, section, key):
        """Get a float value from config."""
        return self.config.getfloat(section, key)
    
    def get_int(self, section, key):
        """Get an integer value from config."""
        return self.config.getint(section, key)
    
    def get_bool(self, section, key):
        """Get a boolean value from config."""
        return self.config.getboolean(section, key)
    
    def get_str(self, section, key):
        """Get a string value from config."""
        return self.config.get(section, key)
