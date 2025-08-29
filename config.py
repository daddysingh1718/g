#!/usr/bin/env python3
"""
Configuration and settings for Gemini Codex CLI
"""

import os
import json
from pathlib import Path
from typing import Dict, Any

class Config:
    """Configuration management for the CLI"""
    
    DEFAULT_CONFIG = {
        "model": "gemini-1.5-pro",
        "temperature": 0.7,
        "max_tokens": 4000,
        "theme": "monokai",
        "auto_save": True,
        "backup_count": 5,
        "log_level": "INFO",
        "timeout": 30,
        "retry_attempts": 3
    }
    
    def __init__(self):
        self.config_dir = Path.home() / ".gemini_codex"
        self.config_file = self.config_dir / "config.json"
        self.settings = self.load_config()
    
    def load_config(self) -> Dict[str, Any]:
        """Load configuration from file"""
        if not self.config_file.exists():
            self.create_default_config()
        
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                # Merge with defaults for any missing keys
                return {**self.DEFAULT_CONFIG, **config}
        except Exception:
            return self.DEFAULT_CONFIG.copy()
    
    def create_default_config(self):
        """Create default configuration file"""
        self.config_dir.mkdir(exist_ok=True)
        with open(self.config_file, 'w') as f:
            json.dump(self.DEFAULT_CONFIG, f, indent=2)
    
    def save_config(self):
        """Save current configuration"""
        self.config_dir.mkdir(exist_ok=True)
        with open(self.config_file, 'w') as f:
            json.dump(self.settings, f, indent=2)
    
    def get(self, key: str, default=None):
        """Get configuration value"""
        return self.settings.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set configuration value"""
        self.settings[key] = value
        self.save_config()
    
    def update(self, updates: Dict[str, Any]):
        """Update multiple configuration values"""
        self.settings.update(updates)
        self.save_config()

# Global configuration instance
config = Config()
