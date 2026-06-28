# === Stage 28: Add overdue item detection based on due dates ===
# Project: CommunityDesk
from datetime import date, timedelta

def detect_overdue_items(announcements):
    today = date.today()
    overdue = []
    for item in announcements:
        due_date_str = item.get('due_date')
        if not due_date_str:
            continue
        try:
            due_date = date.fromisoformat(due_date_str)
            days_over = (today - due_date).days
            if days_over > 0:
                overdue.append({**item, 'status': 'overdue', 'days_over': days_over})
        except ValueError:
            continue
    return overdue

def notify_members_about_overdue(announcements):
    today = date.today()
    for item in announcements:
        due_date_str = item.get('due_date')
        if not due_date_str:
            continue
        try:
            due_date = date.fromisoformat(due_date_str)
            days_over = (today - due_date).days
            if days_over > 0 and item['status'] != 'overdue':
                print(f"⚠️ Overdue alert: {item.get('title')} is {days_over} days past due.")
                item['status'] = 'overdue'
        except ValueError:
            continue
