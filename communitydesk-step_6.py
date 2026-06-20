# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: CommunityDesk
def delete_item(item_id, confirm=False):
    if not confirm:
        raise ValueError("Delete requires explicit confirmation flag set to True")
    
    # Simulate deletion logic for Members, Requests, Events, Volunteers, Announcements
    # In a real app, this would query the specific database table or dictionary key
    deleted = False
    
    try:
        if item_id in members_db[item_id].get('status', 'active'):
            del members_db[item_id]
            deleted = True
        elif item_id in requests_db[item_id].get('status', 'open'):
            del requests_db[item_id]
            deleted = True
        elif item_id in events_db[item_id].get('status', 'scheduled'):
            del events_db[item_id]
            deleted = True
        elif item_id in volunteers_db[item_id].get('status', 'available'):
            del volunteers_db[item_id]
            deleted = True
        elif item_id in announcements_db[item_id].get('status', 'published'):
            del announcements_db[item_id]
            deleted = True
            
        if not deleted:
            raise KeyError(f"No active record found for ID: {item_id}")
            
    except (KeyError, TypeError):
        # Handle cases where the key doesn't exist or structure is different
        pass
        
    return deleted
