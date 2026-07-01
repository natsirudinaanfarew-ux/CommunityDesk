# === Stage 36: Add templates for quickly creating common records ===
# Project: CommunityDesk
from typing import Optional, List, Dict, Any
import json
from datetime import date

class RecordTemplates:
    """Self-contained templates for CommunityDesk records."""
    
    @staticmethod
    def create_event(name: str, description: str, start_date: date) -> Dict[str, Any]:
        return {
            "type": "event",
            "name": name,
            "description": description,
            "start_date": start_date.isoformat(),
            "end_date": None,
            "location": "",
            "status": "planned"
        }

    @staticmethod
    def create_request(requester: str, request_type: str, details: str) -> Dict[str, Any]:
        return {
            "type": "request",
            "requester": requester,
            "request_type": request_type,
            "details": details,
            "status": "pending"
        }

    @staticmethod
    def create_volunteer(name: str, skills: List[str], availability: str) -> Dict[str, Any]:
        return {
            "type": "volunteer",
            "name": name,
            "skills": skills,
            "availability": availability,
            "status": "active"
        }

    @staticmethod
    def create_announcement(title: str, content: str) -> Dict[str, Any]:
        return {
            "type": "announcement",
            "title": title,
            "content": content,
            "date_posted": date.today().isoformat(),
            "author": ""
        }

    @staticmethod
    def create_member(name: str, role: str) -> Dict[str, Any]:
        return {
            "type": "member",
            "name": name,
            "role": role,
            "joined_date": date.today().isoformat(),
            "status": "active"
        }

    @staticmethod
    def bulk_create_events(events_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        created = []
        for e in events_data:
            if isinstance(e, dict) and "name" in e:
                created.append(RecordTemplates.create_event(**e))
            else:
                created.append(RecordTemplates.create_event(name=e.get("name", ""), description="", start_date=date.today()))
        return created

    @staticmethod
    def export_templates_to_json() -> str:
        templates = {
            "event": RecordTemplates.create_event("Template Event", "A sample event.", date.today()),
            "request": RecordTemplates.create_request("User Name", "General Request", "Details here"),
            "volunteer": RecordTemplates.create_volunteer("Volunteer Name", ["Python", "Testing"], "Weekends"),
            "announcement": RecordTemplates.create_announcement("Welcome!", "This is a test announcement."),
            "member": RecordTemplates.create_member("New Member", "Participant")
        }
        return json.dumps(templates, indent=2)
