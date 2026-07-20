# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: CommunityDesk
def format_request_summary(req):
    """Return a human-readable one-line summary of a request."""
    return f"[{req.priority}] {req.title} — assigned to {req.assignee}"

def validate_event_schedule(ev):
    """Check that event times are valid and within the allowed window."""
    if ev.start > ev.end:
        raise ValueError(f"Event '{ev.name}' has start after end")
    if ev.end - ev.start < timedelta(hours=1):
        raise ValueError(f"Event '{ev.name}' is too short")

def build_announcement_text(ann):
    """Compose the public-facing announcement body."""
    parts = [f"**{ann.title}**: {ann.body}", f"By @{ann.author}"]
    if ann.deadline:
        parts.append(f"Deadline: {ann.deadline.strftime('%Y-%m-%d')}")
    return "\n".join(parts)

def count_active_volunteers(volunteers):
    """Return how many volunteers have a pending request."""
    active = [v for v in volunteers if any(
        r.status == "open" and r.assignee is None for r in v.requests
    )]
    return len(active)
