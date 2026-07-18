# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: CommunityDesk
def snapshot_diff(before: dict, after: dict) -> list[dict]:
    """Compare two snapshots and return a list of per-key change records."""
    changes = []
    for key in set(list(before.keys()) + list(after.keys())):
        b_val = before.get(key)
        a_val = after.get(key)
        if b_val == a_val:
            continue
        if isinstance(b_val, (list, dict)) and isinstance(a_val, (list, dict)):
            try:
                sub_diff = snapshot_diff(b_val, a_val)
                changes.append({"key": key, "changes": sub_diff})
            except TypeError:
                pass
        else:
            changes.append({"key": key, "before": b_val, "after": a_val})
    return changes
