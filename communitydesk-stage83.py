# === Stage 83: Add regression tests for the final demo workflow ===
# Project: CommunityDesk
from communitydesk import (Member, Request, Event, Volunteer, Announcement)

m = Member(name="Alice", email="alice@example.com")
r = Request(title="Room Booking", requester=m, description="Need a meeting room for Friday")
e = Event(name="Hackathon", date="2025-12-20", location="Main Hall")
v = Volunteer(name="Bob", skills=["coding", "organizing"])
a = Announcement(content="Welcome to CommunityDesk!", posted_by=m)

assert m in e.volunteers, "member should be volunteer"
assert r in e.requests, "request should belong to event"
assert v.skills is not None and "coding" in v.skills, "volunteer skills should include coding"
assert a.content.startswith("Welcome"), "announcement content should start with Welcome"

print("All regression checks passed.")
