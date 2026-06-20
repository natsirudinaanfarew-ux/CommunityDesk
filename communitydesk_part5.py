# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: CommunityDesk
def update_member(member_id, **kwargs):
    if member_id not in members:
        raise ValueError(f"Member {member_id} does not exist")
    for key, value in kwargs.items():
        if hasattr(members[member_id], key) and getattr(members[member_id], key) is not None:
            setattr(members[member_id], key, value)

def update_request(request_id, **kwargs):
    if request_id not in requests:
        raise ValueError(f"Request {request_id} does not exist")
    for key, value in kwargs.items():
        if hasattr(requests[request_id], key) and getattr(requests[request_id], key) is not None:
            setattr(requests[request_id], key, value)

def update_event(event_id, **kwargs):
    if event_id not in events:
        raise ValueError(f"Event {event_id} does not exist")
    for key, value in kwargs.items():
        if hasattr(events[event_id], key) and getattr(events[event_id], key) is not None:
            setattr(events[event_id], key, value)

def update_volunteer(volunteer_id, **kwargs):
    if volunteer_id not in volunteers:
        raise ValueError(f"Volunteer {volunteer_id} does not exist")
    for key, value in kwargs.items():
        if hasattr(volunteers[volunteer_id], key) and getattr(volunteers[volunteer_id], key) is not None:
            setattr(volunteers[volunteer_id], key, value)

def update_announcement(announcement_id, **kwargs):
    if announcement_id not in announcements:
        raise ValueError(f"Announcement {announcement_id} does not exist")
    for key, value in kwargs.items():
        if hasattr(announcements[announcement_id], key) and getattr(announcements[announcement_id], key) is not None:
            setattr(announcements[announcement_id], key, value)
