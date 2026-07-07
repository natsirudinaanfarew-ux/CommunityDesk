# === Stage 50: Add unit tests for import and export behavior ===
# Project: CommunityDesk
import json, os, sys

sys.path.insert(0, os.path.dirname(__file__))
from community_desk import CommunityDesk

desk = CommunityDesk()
desk.add_member("Alice")
desk.add_event({"title": "Lunch", "date": "2026-05-10"})
desk.add_request({"who": "Bob", "what": "Help needed at Lunch", "status": "open"})

# Export to JSON string and back
json_str = desk.export()
assert json_str.startswith("{")
restored = CommunityDesk.from_json(json_str)
assert restored.members == ["Alice"]
assert len(restored.events) == 1
assert len(restored.requests) == 1
