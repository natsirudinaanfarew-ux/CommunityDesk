# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: CommunityDesk
def repair_data_integrity(data):
    if isinstance(data, dict) and 'members' in data:
        seen_ids = set()
        for i, member in enumerate(data['members']):
            if 'id' in member:
                if member['id'] in seen_ids:
                    data['members'].pop(i)
                else:
                    seen_ids.add(member['id'])
    elif isinstance(data, dict) and 'events' in data:
        for i, event in enumerate(data['events']):
            if not event.get('date'):
                del data['events'][i]
    return data
