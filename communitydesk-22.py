# === Stage 22: Add favorite records and quick favorite listing ===
# Project: CommunityDesk
from typing import Optional, List
import json
from pathlib import Path

class FavoriteManager:
    def __init__(self, data_file: str = "favorites.json"):
        self.data_file = Path(data_file)
        if not self.data_file.exists():
            self._save({})

    def _load(self) -> dict:
        with open(self.data_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _save(self, data: dict):
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add_favorite(self, item_id: str, category: str = "general", note: Optional[str] = None):
        data = self._load()
        if category not in data:
            data[category] = []
        entry = {"id": item_id, "note": note}
        # Avoid duplicates by ID within same category
        if not any(e["id"] == item_id for e in data[category]):
            data[category].append(entry)
        self._save(data)

    def remove_favorite(self, item_id: str, category: Optional[str] = None):
        data = self._load()
        if category and category in data:
            data[category] = [e for e in data[category] if e["id"] != item_id]
            if not data[category]:
                del data[category]
        elif "general" in data:
            data["general"] = [e for e in data["general"] if e["id"] != item_id]
            if not data["general"]:
                del data["general"]
        self._save(data)

    def get_favorites(self, category: Optional[str] = None) -> List[dict]:
        data = self._load()
        if category and category in data:
            return list(data[category])
        elif "general" in data:
            return list(data["general"])
        return []

    def is_favorite(self, item_id: str, category: Optional[str] = None) -> bool:
        items = self.get_favorites(category)
        return any(e["id"] == item_id for e in items)
