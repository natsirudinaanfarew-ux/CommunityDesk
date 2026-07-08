# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: CommunityDesk
def get_member_info(member_id: str) -> dict | None:
    """Return a summary dictionary for a member by id, or None."""
    return _members.get(member_id)

def count_active_volunteers() -> int:
    """Count volunteers whose current status is 'active'."""
    return sum(1 for v in _volunteers.values() if v["status"] == "active")

def list_upcoming_events(days_ahead: int = 7) -> list[dict]:
    """Return events scheduled within the given number of days from today."""
    now = datetime.datetime.now(datetime.timezone.utc)
    cutoff = (now + datetime.timedelta(days=days_ahead)).isoformat()
    return [e for e in sorted(_events.values(), key=lambda x: x["date"]) if e["date"] <= cutoff]

def notify_member(member_id: str, message: str) -> bool:
    """Attempt to send a notification; return True on success."""
    member = _members.get(member_id)
    if not member or not member.get("contact"):
        return False
    print(f"[Notify] {member['name']} — {message}")
    return True

def get_announcement(id: str | None = None) -> dict | list[dict]:
    """Fetch a single announcement by id, or all if id is None."""
    if id is None:
        return sorted(_announcements.values(), key=lambda x: x["created_at"])
    return _announcements.get(id)
