# === Stage 19: Add undo support for the last simple mutation ===
# Project: CommunityDesk
import json
from typing import Optional, List

class UndoManager:
    def __init__(self):
        self._history: List[dict] = []
        self._max_depth: int = 50

    def record(self, action_type: str, payload: dict) -> None:
        entry = {"type": action_type, "payload": payload}
        if len(self._history) >= self._max_depth:
            self._history.pop(0)
        self._history.append(entry)

    def undo_last(self) -> Optional[dict]:
        if not self._history:
            return None
        entry = self._history.pop()
        action_type = entry["type"]
        payload = entry["payload"]
        
        if action_type == "add_member":
            member_id, name, role = payload
            members_map[member_id] = {"name": name, "role": role}
        elif action_type == "remove_member":
            member_id = payload
            del members_map[member_id]
        elif action_type == "update_request_status":
            request_id, status = payload
            requests_map[request_id]["status"] = status
        elif action_type == "add_event":
            event_id, title, date = payload
            events_list.append({"id": event_id, "title": title, "date": date})
        elif action_type == "remove_event":
            event_id = payload
            events_list = [e for e in events_list if e["id"] != event_id]
        
        return entry

    def get_history(self) -> List[dict]:
        return self._history
