# === Stage 27: Add monthly summary calculations ===
# Project: CommunityDesk
def calculate_monthly_summary(events, requests):
    from datetime import datetime
    now = datetime.now()
    month_start = now.replace(day=1)
    cutoff = (month_start + timedelta(days=30)).replace(hour=23, minute=59, second=59)
    monthly_events = [e for e in events if month_start <= e['date'] < cutoff]
    monthly_requests = [r for r in requests if month_start <= r['created_at'] < cutoff and r['status'] != 'archived']
    total_event_attendance = sum(e.get('attendance', 0) for e in monthly_events)
    total_request_count = len(monthly_requests)
    volunteer_hours = sum(v.get('hours_contributed', 0) for v in volunteers if month_start <= datetime.fromtimestamp(v['joined_at']) < cutoff)
    summary = {
        'month': now.strftime('%Y-%m'),
        'total_events': len(monthly_events),
        'event_attendance': total_event_attendance,
        'active_requests': total_request_count,
        'volunteer_hours': volunteer_hours,
        'generated_at': now.isoformat()
    }
    return summary
