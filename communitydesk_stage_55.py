# === Stage 55: Add a setting to disable colorized output ===
# Project: CommunityDesk
class ColorMode:
    """Toggle colorized console output for CLI helpers."""
    
    def __init__(self, enabled=True):
        self.enabled = enabled
    
    @property
    def is_enabled(self):
        return self.enabled
    
    def set_enabled(self, value):
        self.enabled = bool(value)
    
    def disable_colors(self):
        """Return a context manager that disables colors within its scope."""
        class _Context:
            def __enter__(self):
                ColorMode.enabled = False
                return self
            
            def __exit__(self, exc_type, exc_val, exc_tb):
                ColorMode.enabled = True  # Restore previous state
                return False
        
        return _Context()
    
    @staticmethod
    def reset():
        """Reset to default enabled state."""
        ColorMode.enabled = True
    
    def __repr__(self):
        status = "ON" if self.enabled else "OFF"
        return f"<ColorMode: {status}>"

# Example usage demonstration (uncomment for testing)
if __name__ == "__main__":
    mode = ColorMode()
    print(f"Default state: colors {'enabled' if mode.enabled else 'disabled'}")
    
    with mode.disable_colors():
        print("Inside context: colors should be disabled")
    
    print("After context: colors restored to enabled")
