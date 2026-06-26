# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: CommunityDesk
from datetime import datetime, timedelta
import json
import os

ARCHIVE_DIR = "archive"
RETENTION_DAYS = 365

def archive_records(records, cutoff_date=None):
    if cutoff_date is None:
        cutoff_date = datetime.now() - timedelta(days=RETENTION_DAYS)
    
    archived = []
    active = []
    for record in records:
        created_at = record.get("created_at", datetime.min)
        status = record.get("status")
        
        if (not status or status == "completed" and 
            created_at < cutoff_date):
            archive_path = os.path.join(ARCHIVE_DIR, f"{record['id']}.json")
            with open(archive_path, "w", encoding="utf-8") as f:
                json.dump(record, f)
            archived.append(record["id"])
        else:
            active.append(record)
    return active, archived

def restore_records(source_dir=None):
    if source_dir is None:
        source_dir = ARCHIVE_DIR
    
    restored = []
    for filename in os.listdir(source_dir):
        if filename.endswith(".json"):
            filepath = os.path.join(source_dir, filename)
            with open(filepath, "r", encoding="utf-8") as f:
                record = json.load(f)
            # Remove archive-specific metadata before restoring to main list
            restored.append(record)
    return restored
