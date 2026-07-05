# === Stage 45: Add restore from backup with validation ===
# Project: CommunityDesk
import json, os, hashlib

def restore_backup(backup_path: str) -> bool:
    if not backup_path.endswith('.json'):
        raise ValueError("Backup file must be a JSON archive.")
    try:
        with open(backup_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return False
    
    required_keys = {'members', 'requests', 'events', 'volunteers', 'announcements'}
    if not all(k in data for k in required_keys):
        print("Validation failed: missing required sections.")
        return False

    base_dir = os.path.dirname(os.path.abspath(__file__))
    target_path = os.path.join(base_dir, 'data.json')
    
    try:
        with open(target_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
        
        backup_hash = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()[:12]
        print(f"Restored successfully. Backup ID: {backup_hash}")
        return True
    except IOError as e:
        print(f"Write error during restore: {e}")
        return False
