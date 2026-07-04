# === Stage 42: Add CSV export without external dependencies ===
# Project: CommunityDesk
def export_to_csv(data, filename="community_desk_export.csv"):
    if not data:
        return
    headers = list(data[0].keys())
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for row in data:
            # Convert datetime objects to ISO format strings if present
            clean_row = {k: v.isoformat() if isinstance(v, datetime.datetime) else v for k, v in row.items()}
            writer.writerow(clean_row)
