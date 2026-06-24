# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: CommunityDesk
class CommandDispatcher:
    def __init__(self, handlers):
        self.handlers = {cmd.lower(): handler for cmd, handler in handlers.items()}

    def dispatch(self, text):
        command = text.strip().split(maxsplit=1)[0]
        if command in self.handlers:
            return self.handlers[command](text)
        return f"Unknown command: {command}"
