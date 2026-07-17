# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: CommunityDesk
def seed_demo_data(db):
    """Insert deterministic demo data into CommunityDesk tables."""
    db.session.add(Announcement("Welcome to CommunityDesk!", "admin", 0, datetime.utcnow(), None))
    db.session.add(Member("Alice", "alice@example.com", "active"))
    db.session.add(Member("Bob", "bob@example.com", "active"))
    db.session.add(Request("Help with event setup", "event_coordinator", "pending", "Alice", 0, datetime.utcnow(), None))
    db.session.add(Event("Community Meetup", "2024-12-15", "community", "Bob", None))
    db.session.add(Volunteer("Charlie", "charlie@example.com", "available"))
    db.session.commit()
