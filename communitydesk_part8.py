# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: CommunityDesk
from typing import Optional, List, Dict, Any

def filter_requests(
    requests: List[Dict[str, Any]],
    status: Optional[str] = None,
    category: Optional[str] = None,
    owner: Optional[str] = None,
    tag: Optional[str] = None
) -> List[Dict[str, Any]]:
    filtered = []
    for req in requests:
        if status and req.get('status') != status:
            continue
        if category and req.get('category') != category:
            continue
        if owner and req.get('owner') != owner:
            continue
        if tag and tag not in req.get('tags', []):
            continue
        filtered.append(req)
    return filtered

def filter_events(
    events: List[Dict[str, Any]],
    status: Optional[str] = None,
    category: Optional[str] = None,
    owner: Optional[str] = None,
    tag: Optional[str] = None
) -> List[Dict[str, Any]]:
    filtered = []
    for ev in events:
        if status and ev.get('status') != status:
            continue
        if category and ev.get('category') != category:
            continue
        if owner and ev.get('owner') != owner:
            continue
        if tag and tag not in ev.get('tags', []):
            continue
        filtered.append(ev)
    return filtered

def filter_members(
    members: List[Dict[str, Any]],
    status: Optional[str] = None,
    category: Optional[str] = None,
    owner: Optional[str] = None,
    tag: Optional[str] = None
) -> List[Dict[str, Any]]:
    filtered = []
    for mem in members:
        if status and mem.get('status') != status:
            continue
        if category and mem.get('category') != category:
            continue
        if owner and mem.get('owner') != owner:
            continue
        if tag and tag not in mem.get('tags', []):
            continue
        filtered.append(mem)
    return filtered
