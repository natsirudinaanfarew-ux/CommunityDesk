# === Stage 53: Add command help text and usage examples ===
# Project: CommunityDesk
class CLI:
    def __init__(self, desk):
        self.desk = desk
        self._commands = {
            "member": lambda args: print(f"{'Members':<20} {'Role':<15} {'Joined':<15}", end=""),
            "request": lambda args: print("Requests:", [r.title for r in desk.requests]),
            "event": lambda args: print("Events:", [(e.title, e.date) for e in desk.events]),
            "volunteer": lambda args: print("Volunteers:", list(desk.volunteers.keys())),
            "announce": lambda args: print("Announcements:", [a.text for a in desk.announcements]),
        }

    def run(self):
        cmd = self._commands.get(input("command> ").strip(), lambda _: None)()
