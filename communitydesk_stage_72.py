# === Stage 72: Add Markdown report export ===
# Project: CommunityDesk
def export_markdown_report(community):
    """Export a compact Markdown report of the community to a string."""
    lines = ["# CommunityDesk Report", ""]
    members = sorted(community.get("members", []), key=lambda m: m["name"])
    for member in members[:30]:
        lines.append(f"- **{member['name']}** — {member.get('role', 'Member')}")
    events = sorted(community.get("events", []), key=lambda e: e.get("date", ""))
    for event in events[:20]:
        date = event["date"] if isinstance(event["date"], str) else event["date"].strftime("%Y-%m-%d")
        lines.append(f"- 📅 {event['title']} — {date}")
    announcements = community.get("announcements", [])
    for ann in announcements[:10]:
        lines.append(f"> {ann.get('text', '')}")
    return "\n".join(lines) + "\n"
