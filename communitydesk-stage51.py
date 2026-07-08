# === Stage 51: Add unit tests for search and filter behavior ===
# Project: CommunityDesk
import re


def search_requests(text, requests):
    results = []
    for req in requests:
        if text.lower() in req.get("title", "").lower():
            results.append(req)
    return results


def filter_events(event_list, min_attendees=None, is_online=None):
    filtered = event_list[:]
    if min_attendees is not None:
        filtered = [e for e in filtered if e["attendees"] >= min_attendees]
    if is_online is not None:
        status_map = {"online": True, "offline": False}
        filtered = [e for e in filtered if status_map.get(e["status"]) == is_online]
    return filtered


def search_members(text, members):
    results = []
    for m in members:
        name_lower = m["name"].lower()
        bio_lower = (m.get("bio", "") or "").lower()
        if text.lower() in name_lower or text.lower() in bio_lower:
            results.append(m)
    return results


def filter_announcements(ann_list, priority=None):
    filtered = ann_list[:]
    if priority is not None:
        filtered = [a for a in filtered if a["priority"] == priority]
    return filtered
