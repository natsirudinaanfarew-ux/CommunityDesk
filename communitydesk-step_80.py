# === Stage 80: Polish user-facing messages, names, and examples for consistency ===
# Project: CommunityDesk
# Step 80 – Polish user-facing messages, names, and examples for consistency.

# ── Consistent greeting & sign-off helpers ────────────────────────────────
def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}! Welcome to CommunityDesk."


def farewell(name: str) -> str:
    """Return a warm goodbye message."""
    return f"Goodbye, {name}. See you at the next event!"


# ── Request status messages (single source of truth) ──────────────────────
REQUEST_STATUS_MESSAGES = {
    "pending":   "Your request is pending review.",
    "approved":  "Your request has been approved. Get ready!",
    "rejected":  "Your request was not accepted this time. Try again later.",
}


# ── Event-related messages ───────────────────────────────────────────────
EVENT_STATUS_MESSAGES = {
    "upcoming":   "An exciting event is coming up! Mark your calendar.",
    "ongoing":    "This event is happening right now! Join the fun!",
    "completed":  "The event has ended. Thanks for participating!",
}


# ── Announcement style helper ────────────────────────────────────────────
def announce(subject: str, body: str) -> str:
    """Format a readable announcement."""
    return f"[Announcement] {subject}\n\n{body}"


# ── Example usage (kept for reference only; not executed in production) ───
if __name__ == "__main__":
    print(greet("Alice"))
    print(farewell("Bob"))
    print(REQUEST_STATUS_MESSAGES["approved"])
    print(EVENT_STATUS_MESSAGES["upcoming"])
    print(announce("New Volunteer Spot", "We're looking for more volunteers. Apply now!"))
