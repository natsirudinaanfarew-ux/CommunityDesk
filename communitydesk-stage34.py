# === Stage 34: Add support for multiple local user profiles ===
# Project: CommunityDesk
class ProfileManager:
    def __init__(self, base_path=".profiles"):
        self.base_path = Path(base_path)
        self.profiles = {}

    def load_all(self):
        if not self.base_path.exists():
            return
        for p in self.base_path.glob("*.json"):
            try:
                data = json.load(p.open())
                name = data.get("name", p.stem)
                self.profiles[name] = Profile(data)
            except Exception:
                continue

    def get(self, name):
        return self.profiles.get(name) or None

class Profile:
    def __init__(self, data):
        self.name = data.get("name", "default")
        self.email = data.get("email", "")
        self.role = data.get("role", "member")
        self.preferences = data.get("preferences", {})
