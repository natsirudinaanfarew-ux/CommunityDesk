# === Stage 41: Add plain text import for a simple line-based format ===
# Project: CommunityDesk
import csv
from typing import List, Dict, Any

def load_line_based_data(file_path: str) -> List[Dict[str, Any]]:
    """Load data from a simple line-based text file where each line is 'key=value;key2=value2'."""
    records = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                record = {}
                parts = [p.strip() for p in line.split(';')]
                for part in parts:
                    if '=' in part:
                        key, value = part.split('=', 1)
                        record[key.strip()] = value.strip()
                if record:
                    records.append(record)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    return records

def save_line_based_data(records: List[Dict[str, Any]], file_path: str) -> None:
    """Save data to a simple line-based text file."""
    try:
        with open(file_path, mode='w', encoding='utf-8') as f:
            for record in records:
                if not record:
                    continue
                parts = [f"{k}={v}" for k, v in sorted(record.items())]
                line = ';'.join(parts)
                f.write(line + '\n')
    except IOError as e:
        print(f"Error writing to file '{file_path}': {e}")
