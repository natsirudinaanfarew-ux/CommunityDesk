# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: CommunityDesk
def manage_tags(tags, item):
    return {**item, "tags": list(set(item.get("tags", []) + tags))}

def remove_tags(tags, item):
    current = set(item.get("tags", []))
    to_remove = [t for t in tags if t in current]
    return {**item, "tags": list(current - set(to_remove))}

def generate_tag_summary(items):
    tag_counts = {}
    for i in items:
        for t in i.get("tags", []):
            tag_counts[t] = tag_counts.get(t, 0) + 1
    return sorted(tag_counts.items(), key=lambda x: -x[1])
