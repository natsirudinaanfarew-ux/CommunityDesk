# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: CommunityDesk
def find_member_by_name(name: str) -> Member | None:
    for m in members:
        if m.name.lower() == name.lower():
            return m
    return None


def is_volunteer_available(volunteer_id: int, event_date: datetime.date) -> bool:
    vol = next((v for v in volunteers if v.id == volunteer_id), None)
    if vol is None:
        raise ValueError(f"Volunteer {volunteer_id} not found")
    return (event_date - vol.next_available).days >= 0


def filter_events_by_category(cat: str) -> list[Event]:
    return [e for e in events if cat.lower() in e.category.lower()]


def format_member_summary(member: Member) -> str:
    return f"{member.name} ({member.email}) — joined {member.joined_date}"


def get_volunteer_count_by_event_id(event_id: int) -> int:
    return len([v for v in volunteer_events if v.event_id == event_id])
