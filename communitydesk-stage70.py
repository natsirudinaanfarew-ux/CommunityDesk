# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: CommunityDesk
def clear_state():
    """Reset all internal state to a fresh, empty condition."""
    if _confirmed is None:
        raise RuntimeError("clear_state() must be called after confirm_clear()")
    members = []
    requests = {}
    events = []
    volunteers = set()
    announcements = []
    return {
        "members": members,
        "requests": requests,
        "events": events,
        "volunteers": volunteers,
        "announcements": announcements,
    }
