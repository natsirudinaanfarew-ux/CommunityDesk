# === Stage 26: Add weekly summary calculations ===
# Project: CommunityDesk
def calculate_weekly_summary(events, requests):
    from datetime import datetime, timedelta
    today = datetime.now()
    week_start = (today - timedelta(days=today.weekday())).date()
    week_end = week_start + timedelta(days=6)
    
    weekly_events = [e for e in events if week_start <= e['date'] <= week_end]
    weekly_requests = [r for r in requests if week_start <= r['created_at'].replace(tzinfo=None).date() <= week_end]
    
    total_completed = sum(1 for e in weekly_events if e.get('status') == 'completed')
    total_open = len([e for e in weekly_events if e.get('status') != 'completed'])
    total_requests_handled = sum(1 for r in weekly_requests if r.get('resolved'))
    
    return {
        "week_start": week_start,
        "week_end": week_end,
        "total_events": len(weekly_events),
        "completed_events": total_completed,
        "open_events": total_open,
        "new_requests": sum(1 for r in weekly_requests if not r.get('resolved')),
        "requests_resolved": total_requests_handled
    }
