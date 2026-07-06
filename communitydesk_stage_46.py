# === Stage 46: Add a schema version field and migration helper ===
# Project: CommunityDesk
import json, os

SCHEMA_VERSION = 3


def migrate(db_path: str) -> None:
    """Apply schema migrations if needed."""
    db_path = os.path.join(os.path.dirname(__file__), db_path)
    with open(db_path, "r") as f:
        data = json.load(f)

    current_version = int(data.get("__schema_version", 1))
    if current_version < SCHEMA_VERSION:
        if "__schema_version" not in data:
            data["__schema_version"] = SCHEMA_VERSION
        # Migration v2->v3: add a 'status' field to every request dict
        for key in ("requests",):
            records = data.get(key, [])
            for rec in records:
                if "status" not in rec:
                    rec["status"] = "open"

    with open(db_path, "w") as f:
        json.dump(data, f, indent=2)


def ensure_schema_version(version: int) -> None:
    """Set the schema version to a specific value."""
    global SCHEMA_VERSION
    SCHEMA_VERSION = version
