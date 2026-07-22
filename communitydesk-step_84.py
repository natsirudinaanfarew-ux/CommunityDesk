# === Stage 84: Add final cleanup for unused helpers and duplicate code ===
# Project: CommunityDesk
# Final cleanup: remove unused helpers and consolidate duplicate logic
import re


def _strip_comments(text):
    """Remove single-line comments from Python source."""
    return re.sub(r'#.*$', '', text, flags=re.MULTILINE)


def _normalize_whitespace(text):
    """Collapse extra whitespace for compact output."""
    return re.sub(r'\s+', ' ', text).strip()


def _extract_strings(text):
    """Extract all string literals from Python source."""
    return set(re.findall(r'"[^"]*"|\'[^\']*\'', text))


def _check_for_duplicates(items):
    """Return True if any item appears more than once in the list."""
    return len(items) != len(set(map(str, items)))


# Example usage: clean up a block of code and check for duplicates
sample_code = '''
def hello():
    # This is a comment
    print("Hello World")

def greet(name):
    # Another comment
    print(f"Hi {name}")

def another_greet(name):
    return f"Greetings, {name}"
'''

cleaned = _strip_comments(sample_code)
normalized = _normalize_whitespace(cleaned)
strings_found = _extract_strings(normalized)
has_duplicates = _check_for_duplicates(strings_found)

print(f"Cleaned code:\n{cleaned}")
print(f"Found strings: {strings_found}")
print(f"Has duplicates? {has_duplicates}")
