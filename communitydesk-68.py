# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: CommunityDesk
def generate_changelog(activity_log: dict) -> str:
    """Generate a compact changelog from an activity log."""
    lines = ["=== CommunityDesk Changelog ===", ""]
    for entry in activity_log.get("entries", []):
        date = entry.get("date", "Unknown")
        desc = entry.get("description", "")[:100]
        lines.append(f"[{date}] {desc}")
    lines.append("")
    return "\n".join(lines)
