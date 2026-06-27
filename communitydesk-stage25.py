# === Stage 25: Add daily summary calculations ===
# Project: CommunityDesk
from datetime import datetime, timedelta
def calculate_daily_summary(events):
    today = datetime.now().date()
    summary = {"total_events": 0, "upcoming_count": 0, "past_count": 0}
    for event in events:
        if isinstance(event.get("start_date"), str):
            start_dt = datetime.strptime(event["start_date"], "%Y-%m-%d").date()
        else:
            start_dt = event["start_date"]
        summary["total_events"] += 1
        if start_dt > today:
            summary["upcoming_count"] += 1
        elif start_dt < today:
            summary["past_count"] += 1
    return summary
