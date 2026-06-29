# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: CommunityDesk
from datetime import datetime, timedelta
def get_upcoming_events(events: list[dict], days_ahead: int = 7) -> list[dict]:
    now = datetime.now()
    cutoff = (now + timedelta(days=days_ahead)).date()
    return [e for e in events if e.get('start_date', '').replace('-', '') <= cutoff.replace('-', '') and e.get('status') != 'cancelled']

def get_upcoming_requests(requests: list[dict], days_ahead: int = 7) -> list[dict]:
    now = datetime.now()
    cutoff = (now + timedelta(days=days_ahead)).date()
    return [r for r in requests if r.get('due_date', '').replace('-', '') <= cutoff.replace('-', '') and not r.get('completed')]

def get_upcoming_announcements(announcements: list[dict], days_ahead: int = 7) -> list[dict]:
    now = datetime.now()
    cutoff = (now + timedelta(days=days_ahead)).date()
    return [a for a in announcements if a.get('publish_date', '').replace('-', '') <= cutoff.replace('-','') and not a.get('archived')]

def get_upcoming_volunteer_shifts(shifts: list[dict], days_ahead: int = 7) -> list[dict]:
    now = datetime.now()
    cutoff = (now + timedelta(days=days_ahead)).date()
    return [s for s in shifts if s.get('shift_date', '').replace('-', '') <= cutoff.replace('-','') and not s.get('filled')]
