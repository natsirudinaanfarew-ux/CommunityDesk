# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: CommunityDesk
def colorize(text, color):
    """Return ANSI-colored text if colors are enabled."""
    _colors = {
        "red": "\033[91m", "green": "\033[92m", "yellow": "\033[93m",
        "blue": "\033[94m", "magenta": "\033[95m", "cyan": "\033[96m",
        "white": "\033[97m", "reset": "\033[0m"
    }
    return _colors.get(color, "") + text + _colors["reset"]

def print_header(title):
    """Print a centered header line."""
    border = "=" * 60
    print(border)
    print(f"{colorize(title, 'cyan').center(60)}")
    print(border)

def print_item(label, value):
    """Print a key-value item in green."""
    if label:
        print(f"  {colorize(label, 'green')}: {value}")
