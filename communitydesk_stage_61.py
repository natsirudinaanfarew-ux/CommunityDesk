# === Stage 61: Add performance timing for core list and search operations ===
# Project: CommunityDesk
import time
from functools import wraps


def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"[{func.__name__}] {elapsed:.4f}s")
        return result
    return wrapper


@timed
def list_all_members():
    """Return a sorted list of all Member instances."""
    from models.member import Member
    members = [m for m in Member._all if isinstance(m, Member)]
    return sorted(members, key=lambda m: (m.created_at or 0, m.name))


@timed
def search_events(term):
    """Search event titles and descriptions containing *term* (case-insensitive)."""
    from models.event import Event
    term = term.lower()
    events = [e for e in Event._all if isinstance(e, Event) and
              any(term in text for text in (e.title or "", str(e.description or "")))]
    return sorted(events, key=lambda e: e.created_at or 0)


@timed
def list_active_volunteers():
    """Return volunteers whose profile is currently active."""
    from models.volunteer import Volunteer
    return [v for v in Volunteer._all if isinstance(v, Volunteer) and v.active]


@timed
def get_pending_requests():
    """Return requests awaiting any action (no response date yet)."""
    from models.request import Request
    return [r for r in Request._all if isinstance(r, Request) and not r.responded_at]


@timed
def list_announcements():
    """Return announcements sorted newest-first."""
    from models.announcement import Announcement
    return sorted(Announcement._all or [], key=lambda a: a.created_at or 0, reverse=True)
