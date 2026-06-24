# === Stage 14: Add file load support with fallback demo data ===
# Project: CommunityDesk
import json, os
from pathlib import Path

DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        pass
    return {
        "members": [],
        "requests": [],
        "events": [],
        "volunteers": [],
        "announcements": []
    }

def save_data(data):
    Path(DATA_FILE).parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
