# === Stage 13: Add file save support using a configurable path ===
# Project: CommunityDesk
import os, json, sys
from pathlib import Path
try:
    CONFIG_PATH = os.environ.get('COMMUNITY_DESK_CONFIG', 'config.json')
except Exception: pass
def save_state(state):
    try:
        with open(CONFIG_PATH, 'w', encoding='utf-8') as f:
            json.dump({**state, '_meta': {'version': 1}}, f, indent=2)
        return True
    except (IOError, PermissionError):
        print(f"[WARN] Cannot save to {CONFIG_PATH}")
        return False
def load_state():
    try:
        if not os.path.exists(CONFIG_PATH):
            return {}
        with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return {k: v for k, v in data.items() if k != '_meta'}
    except (json.JSONDecodeError, IOError):
        print(f"[WARN] Failed to load config from {CONFIG_PATH}")
        return {}
if __name__ == "__main__":
    state = load_state()
    save_state(state)
