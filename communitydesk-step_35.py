# === Stage 35: Add active user switching and user-specific records ===
# Project: CommunityDesk
class ActiveUserManager:
    def __init__(self, storage_path="community_desk_data.json"):
        self.storage = load_json(storage_path) if os.path.exists(storage_path) else {}
        self.current_user_id = None
        self.active_records = []

    def set_current_user(self, user_id):
        self.current_user_id = user_id
        return self

    def get_active_context(self):
        context = {
            "user": self.storage.get("users", {}).get(self.current_user_id),
            "my_requests": [r for r in self.storage.get("requests", []) if r["created_by"] == self.current_user_id],
            "my_events": [e for e in self.storage.get("events", []) if e["organizer"] == self.current_user_id],
            "volunteer_for_me": [v for v in self.storage.get("volunteers", []) if v["for_user"] == self.current_user_id]
        }
        return context

    def add_my_request(self, request_data):
        request_data["created_by"] = self.current_user_id
        request_data["status"] = "pending"
        self.storage.setdefault("requests", []).append(request_data)
        save_json(self.storage)
        return True

    def update_my_event_status(self, event_id, new_status):
        events = self.storage.get("events", [])
        for e in events:
            if e["id"] == event_id and (e["organizer"] == self.current_user_id or "participants" in e and self.current_user_id in e["participants"]):
                e["status"] = new_status
                save_json(self.storage)
                return True
        return False

    def get_all_active_records_summary(self):
        summary = {
            "total_requests": len([r for r in self.storage.get("requests", []) if r["created_by"] == self.current_user_id]),
            "my_events_count": len([e for e in self.storage.get("events", []) if e["organizer"] == self.current_user_id or (self.current_user_id in e.get("participants", []))]),
            "volunteer_slots_open": sum(1 for v in self.storage.get("volunteers", []) if not v["filled"])
        }
        return summary
