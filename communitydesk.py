# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: CommunityDesk
from typing import List, Dict, Any
from datetime import date
import uuid

class CommunityDesk:
    def __init__(self):
        self.members: Dict[str, Dict] = {}
        self.requests: List[Dict] = []
        self.events: List[Dict] = []
        self.volunteers: Dict[str, Dict] = {}
        self.announcements: List[Dict] = []

    def add_member(self, name: str, email: str) -> None:
        member_id = str(uuid.uuid4())[:8]
        self.members[member_id] = {"name": name, "email": email}

    def create_request(self, title: str, description: str, status: str = "open") -> Dict[str, Any]:
        req_id = str(uuid.uuid4())[:8]
        request = {
            "id": req_id,
            "title": title,
            "description": description,
            "status": status,
            "created_at": date.today().isoformat()
        }
        self.requests.append(request)
        return request

    def register_volunteer(self, name: str, skills: List[str]) -> None:
        vol_id = str(uuid.uuid4())[:8]
        self.volunteers[vol_id] = {"name": name, "skills": skills}

    def add_event(self, title: str, date_str: str) -> Dict[str, Any]:
        event_id = str(uuid.uuid4())[:8]
        event = {
            "id": event_id,
            "title": title,
            "date": date_str,
            "registered_volunteers": []
        }
        self.events.append(event)
        return event

    def post_announcement(self, text: str) -> None:
        ann_id = str(uuid.uuid4())[:8]
        announcement = {
            "id": ann_id,
            "text": text,
            "created_at": date.today().isoformat()
        }
        self.announcements.append(announcement)

def demo_data():
    desk = CommunityDesk()
    desk.add_member("Alice", "alice@example.com")
    desk.create_request("Need help with Python scripts", "I need a script to parse logs.")
    desk.register_volunteer("Bob", ["Python", "Linux"])
    desk.add_event("Community Meetup", "2023-12-15")
    desk.post_announcement("Welcome new members!")
    return desk

if __name__ == "__main__":
    d = demo_data()
    print(f"Members: {len(d.members)}")
    print(f"Requests: {d.requests[0]['title']}")
