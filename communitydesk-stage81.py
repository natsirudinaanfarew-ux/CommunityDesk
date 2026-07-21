# === Stage 81: Add final README text as a module string with usage examples ===
# Project: CommunityDesk
def usage_examples():
    """Demonstrate typical CommunityDesk usage."""
    desk = CommunityDesk("Tech Meetup")
    desk.add_member(Member("Alice", "alice@example.com"))
    desk.add_volunteer(Volunteer("Bob", "bob@example.com", skills=["Python"]))
    desk.create_event(Event("Workshop", date="2024-10-15", location="Hall A"))
    desk.submit_request(Request("Need 3 volunteers for Workshop", priority=HIGH))
    desk.post_announcement(Announcement("Event confirmed!", source_type="admin"))
    print(f"Desk: {desk.title}")
    print(f"Members: {[m.name for m in desk.members]}")
    print(f"Volunteers: {[v.name for v in desk.volunteers]}")
    print(f"Events: {[e.title for e in desk.events]}")
    print(f"Pending requests: {len(desk.pending_requests)}")
