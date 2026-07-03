# === Stage 40: Add plain text report export ===
# Project: CommunityDesk
def export_report_to_text(community_data, output_path):
    """Export community data to a plain text report."""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("COMMUNITY DESK REPORT\n")
        f.write("=" * 40 + "\n\n")
        
        if "members" in community_data and community_data["members"]:
            f.write("MEMBERS:\n")
            for member in community_data["members"]:
                f.write(f"- {member['name']}: {member.get('role', 'Member')}\n")
            f.write("\n")

        if "requests" in community_data and community_data["requests"]:
            f.write("REQUESTS:\n")
            for req in community_data["requests"]:
                status = req.get("status", "Open")
                priority = req.get("priority", "Normal")
                f.write(f"- [{status}] {req['title']} (Priority: {priority})\n")
            f.write("\n")

        if "events" in community_data and community_data["events"]:
            f.write("EVENTS:\n")
            for event in community_data["events"]:
                date = event.get('date', 'N/A')
                location = event.get('location', 'Online')
                f.write(f"- {event['title']}: {date} @ {location}\n")
            f.write("\n")

        if "volunteers" in community_data and community_data["volunteers"]:
            f.write("VOLUNTEERS:\n")
            for vol in community_data["volunteers"]:
                skills = ", ".join(vol.get('skills', []))
                f.write(f"- {vol['name']}: {skills}\n")
            f.write("\n")

        if "announcements" in community_data and community_data["announcements"]:
            f.write("ANNOUNCEMENTS:\n")
            for ann in community_data["announcements"]:
                date = ann.get('date', 'N/A')
                f.write(f"- [{date}] {ann['title']}\n")
            f.write("\n")

        f.write("=" * 40 + "\nEND OF REPORT\n")
