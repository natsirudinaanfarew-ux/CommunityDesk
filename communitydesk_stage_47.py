# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: CommunityDesk
from communitydesk import (Member, Request, Event, Volunteer, Announcement)
from datetime import date

# --- Demo scenario: coordinate a charity run ---

member_alice = Member("Alice", "alice@example.com")
member_bob   = Member("Bob" , "bob@example.com")
member_carol = Member("Carol","carol@example.com")

event_run = Event(
    name="Charity 5K Run",
    date=date(2026, 11, 15),
    location="Central Park",
)

request_help = Request(
    title="Need volunteers for registration desk",
    description="We need at least 3 people to staff the check-in table.",
    target_date=date(2026, 11, 14),
)

volunteer_alice = Volunteer(
    name="Alice",
    role="Registration Lead",
    event=event_run,
    request=request_help,
)

announcement_signups = Announcement(
    title="Sign-ups Open for Charity 5K Run",
    body=f"Register at {event_run.location} on {event_run.date}. "
         f"Volunteers are needed — join now!",
)

print(f"{volunteer_alice.name} is leading registration for the run.")
print(announcement_signups.title)
