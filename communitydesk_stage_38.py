# === Stage 38: Add data integrity checks for broken references ===
# Project: CommunityDesk
def validate_references(data):
    members = {m['id']: m for m in data.get('members', [])}
    requests = data.get('requests', [])
    events = data.get('events', [])
    volunteers = data.get('volunteers', [])
    
    errors = []
    for req in requests:
        if req.get('member_id') and req['member_id'] not in members:
            errors.append(f"Request {req['id']} references unknown member {req['member_id']}")
        if req.get('event_id') and req['event_id']:
            event_ids = {e['id'] for e in events}
            if req['event_id'] not in event_ids:
                errors.append(f"Request {req['id']} references unknown event {req['event_id']}")
        if req.get('volunteer_id') and req['volunteer_id']:
            volunteer_ids = {v['id'] for v in volunteers}
            if req['volunteer_id'] not in volunteer_ids:
                errors.append(f"Request {req['id']} references unknown volunteer {req['volunteer_id']}")

    for evt in events:
        if evt.get('organizer_id') and evt['organizer_id'] not in members:
            errors.append(f"Event {evt['id']} references unknown organizer {evt['organizer_id']}")
        if evt.get('member_ids'):
            member_ids = set(members.keys())
            for mid in evt['member_ids']:
                if mid and mid not in member_ids:
                    errors.append(f"Event {evt['id']} references unknown member {mid}")

    return len(errors) == 0, errors
