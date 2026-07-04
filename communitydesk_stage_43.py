# === Stage 43: Add CSV import for the primary record type ===
# Project: CommunityDesk
import csv, sys
from pathlib import Path
def load_csv_records(file_path: str, record_type: str):
    path = Path(file_path)
    if not path.exists(): raise FileNotFoundError(f"File {file_path} not found")
    records = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            record_id = row.get('id', '')
            if record_type == 'member':
                records.append({'id': int(record_id), **{k.strip(): v.strip() for k, v in row.items()}})
            elif record_type == 'event':
                records.append({'id': int(record_id), **{k.strip(): v.strip() for k, v in row.items()}})
            elif record_type == 'request':
                records.append({'id': int(record_id), **{k.strip(): v.strip() for k, v in row.items()}})
    return records

if __name__ == '__main__':
    if len(sys.argv) < 3: print("Usage: python script.py csv_file record_type"); sys.exit(1)
    file_path = sys.argv[1]
    rec_type = sys.argv[2].lower()
    loaded = load_csv_records(file_path, rec_type)
    print(f"Loaded {len(loaded)} {rec_type} records from {file_path}")
