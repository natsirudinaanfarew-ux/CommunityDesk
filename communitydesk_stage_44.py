# === Stage 44: Add backup creation for the data file ===
# Project: CommunityDesk
import shutil, os, datetime
from pathlib import Path

def backup_data(data_file: str) -> bool:
    if not os.path.exists(data_file):
        return False
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    backup_path = f"{data_file}.bak_{timestamp}"
    try:
        shutil.copy2(data_file, backup_path)
        print(f"Backup created: {backup_path}")
        return True
    except Exception as e:
        print(f"Backup failed: {e}")
        return False

if __name__ == "__main__":
    data_file = "community_desk.json"
    if backup_data(data_file):
        print("Operation successful")
    else:
        print("No action taken or error occurred")
