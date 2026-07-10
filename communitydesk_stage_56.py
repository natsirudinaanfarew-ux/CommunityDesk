# === Stage 56: Add compact error classes for domain failures ===
# Project: CommunityDesk
class CommunityDeskError(Exception):
    pass


class MemberNotFoundError(CommunityDeskError):
    def __init__(self, member_id: str) -> None:
        self.member_id = member_id
        super().__init__(f"Member {member_id} not found")


class RequestNotFulfillableError(CommunityDeskError):
    pass


class EventCapacityExceededError(CommunityDeskError):
    def __init__(self, event_id: str) -> None:
        self.event_id = event_id
        super().__init__(f"Event {event_id} capacity exceeded")


class VolunteerNotEligibleError(CommunityDeskError):
    pass


class AnnouncementInvalidError(CommunityDeskError):
    def __init__(self, reason: str) -> None:
        self.reason = reason
        super().__init__(f"Announcement invalid ({reason})")
