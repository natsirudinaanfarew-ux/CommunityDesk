# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: CommunityDesk
def validate_required(value, field_name):
    if not value:
        raise ValueError(f"Field '{field_name}' is required")
    return True

def validate_identifier(identifier):
    if not identifier or len(identifier) < 3 or len(identifier) > 50:
        raise ValueError("Identifier must be between 3 and 50 characters")
    if not re.match(r'^[a-zA-Z][a-zA-Z0-9_-]*$', identifier):
        raise ValueError("Identifier must start with a letter and contain only letters, numbers, underscores or hyphens")
    return True

def validate_short_text(text, max_length=140):
    if not text:
        raise ValueError("Text cannot be empty")
    if len(text) > max_length:
        raise ValueError(f"Text exceeds {max_length} characters limit")
    return True
