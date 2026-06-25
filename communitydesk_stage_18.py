# === Stage 18: Add an activity log with timestamps and action names ===
# Project: CommunityDesk
class ActivityLog:
    def __init__(self):
        self._log = []

    def log(self, action_name, user=None, details=""):
        entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action_name,
            "user": user or "system",
            "details": details
        }
        self._log.append(entry)

    def get_log(self):
        return self._log.copy()
