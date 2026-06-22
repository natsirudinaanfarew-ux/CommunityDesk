# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: CommunityDesk
import json, os

def load_json_safe(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[WARN] File not found: {path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"[ERROR] Malformed JSON in '{path}': {e.msg} at line {e.lineno}")
        return {}

def save_json_safe(path, data):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"[OK] Saved to {path}")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to save {path}: {e}")
        return False

if __name__ == "__main__":
    data = load_json_safe("data.json")
    if not data and os.path.exists("data.json"):
        exit(1)
