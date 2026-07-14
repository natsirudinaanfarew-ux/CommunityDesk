# === Stage 63: Add relationships between records where useful ===
# Project: CommunityDesk
import datetime, random

# Seed a few sample events so we have something to assign volunteers and announce.
EVENTS = [
    {"id": 10, "title": "Community Meetup", "date": datetime.date(2025, 6, 14), "location": "Main Hall"},
    {"id": 11, "title": "Code Jam",       "date": datetime.date(2025, 7, 4),   "location": "Lab B"},
    {"id": 12, "title": "Workshop: Intro to Python", "date": datetime.date(2025, 8, 16), "location": "Room C"},
]

# Pick a few volunteers and assign them to events at random.
VOLUNTEERS = [v for v in MEMBERS if v.get("role") == "volunteer"]
for ev in EVENTS:
    count = random.randint(2, 4)
    chosen = random.sample(VOLUNTEERS, min(count, len(VOLUNTEERS)))
    for vol in chosen:
        vol["events"].append(ev["id"])

# Build a simple announcements list referencing events and members.
ANNOUNCEMENTS = [
    {"date": datetime.date(2025, 1, 1), "text": "Welcome to CommunityDesk!"},
    {"date": datetime.date(2025, 3, 10), "text": f"Register for {EVENTS[0]['title']} by {EVENTS[0]['date'].strftime('%Y-%m-%d')}."},
    {"date": datetime.date(2025, 4, 22), "text": "New volunteers are needed – check the event list!"},
]

# Requests referencing members and announcements.
REQUESTS = [
    {"id": 1, "member_id": 3, "type": "support", "status": "open"},
    {"id": 2, "member_id": 5, "type": "resource", "status": "pending"},
]

# Members referencing requests they made.
for req in REQUESTS:
    member = MEMBERS[req["member_id"]] if req["member_id"] < len(MEMBERS) else None
    if member:
        member.setdefault("requests_made", []).append(req["id"])
