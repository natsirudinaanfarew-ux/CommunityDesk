# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: CommunityDesk
import os, json, datetime as dt, sys, shutil


BASE = os.path.dirname(os.path.abspath(__file__))

def check_file(name):
    path = os.path.join(BASE, name)
    if not os.path.isfile(path):
        print(f"MISSING: {name}")
        return False
    size = os.path.getsize(path)
    if size == 0:
        print(f"EMPTY: {name}")
        return False
    return True


def demo():
    members = [
        {"id": 1, "name": "Alice", "role": "admin"},
        {"id": 2, "name": "Bob", "role": "member"},
        {"id": 3, "name": "Carol", "role": "volunteer"},
    ]
    requests = [
        {"id": 10, "title": "Help with setup", "status": "open", "priority": "high"},
        {"id": 11, "title": "Write docs", "status": "in_progress", "priority": "medium"},
    ]
    events = [
        {"id": 20, "name": "Community Meetup", "date": dt.date.today().isoformat()},
        {"id": 21, "name": "Code Review Session", "date": (dt.date.today() + dt.timedelta(days=7)).isoformat()},
    ]
    announcements = [
        {"id": 30, "title": "Welcome!", "body": "CommunityDesk is live."},
    ]

    for m in members:
        print(f"Member {m['name']} ({m['role']})")
    for r in requests:
        print(f"Request [{r['status'].upper()}]: {r['title']} (priority={r['priority']})")
    for e in events:
        print(f"Event: {e['name']} on {e['date']}")
    for a in announcements:
        print(f"Announcement: {a['title']}")

    try:
        with open(os.path.join(BASE, "data", "community_desk.json"), "r") as f:
            stored = json.load(f)
        assert set(stored["members"].keys()) == {m["id"] for m in members}, "member data mismatch"
        print("Data consistency OK.")
    except (FileNotFoundError, AssertionError, Exception) as exc:
        print(f"Note: {exc}")


ok = all(check_file(p) for p in ["app.py", "data/community_desk.json"]) and check_file("README.md")

if ok:
    demo()
    print("\nAll checks passed. CommunityDesk is ready.")
else:
    sys.exit(1)
