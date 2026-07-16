# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: CommunityDesk
def reset_demo_data():
    """Reset all tables to demo data for manual testing."""
    import sqlite3
    conn = sqlite3.connect('community_desk.db')
    c = conn.cursor()
    # Clear all data
    c.execute("DELETE FROM announcements")
    c.execute("DELETE FROM volunteers")
    c.execute("DELETE FROM events")
    c.execute("DELETE FROM requests")
    c.execute("DELETE FROM members")
    # Re-insert demo members
    demo_members = [
        ('Alice Johnson', 'alice@example.com'),
        ('Bob Smith', 'bob@example.com'),
        ('Charlie Brown', 'charlie@example.com'),
    ]
    for name, email in demo_members:
        c.execute("INSERT INTO members (name, email) VALUES (?, ?)", (name, email))
    # Re-insert demo announcements
    demo_announcements = [
        ('Welcome to CommunityDesk!', '2024-01-15'),
        ('Upcoming Event Registration Open', '2024-01-20'),
    ]
    for title, date in demo_announcements:
        c.execute("INSERT INTO announcements (title, created_at) VALUES (?, ?)", (title, date))
    # Re-insert demo events
    demo_events = [
        ('Annual Community Meetup', '2024-03-15 18:00'),
        ('Python Workshop for Beginners', '2024-04-20 10:00'),
    ]
    for title, time in demo_events:
        c.execute("INSERT INTO events (title, event_time) VALUES (?, ?)", (title, time))
    # Re-insert demo volunteers
    demo_volunteers = [
        ('Alice Johnson', 'Annual Community Meetup'),
        ('Bob Smith', 'Python Workshop for Beginners'),
    ]
    for name, event in demo_volunteers:
        c.execute("INSERT INTO volunteers (volunteer_name, event_id) VALUES (?, ?)", (name, event))
    # Re-insert demo requests
    demo_requests = [
        ('Need more chairs for the meetup', '2024-01-25'),
        ('Book a projector for the workshop', '2024-02-01'),
    ]
    for title, date in demo_requests:
        c.execute("INSERT INTO requests (title, created_at) VALUES (?, ?)", (title, date))
    conn.commit()
    print("Demo data has been reset successfully!")

if __name__ == "__main__":
    reset_demo_data()
