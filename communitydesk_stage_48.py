# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: CommunityDesk
import unittest
from communitydesk.models import Member, Request, Event, Volunteer, Announcement


class TestCreationHelpers(unittest.TestCase):
    def test_member_creation(self):
        m = Member(name="Alice", email="alice@example.com")
        self.assertEqual(m.name, "Alice")
        self.assertEqual(m.email, "alice@example.com")

    def test_request_valid(self):
        r = Request(title="Help needed", description="I need help with Python")
        self.assertEqual(r.title, "Help needed")
        self.assertTrue(r.is_valid())

    def test_event_creation(self):
        e = Event(name="Python Meetup", date="2024-12-01", location="Online")
        self.assertEqual(e.name, "Python Meetup")
        self.assertTrue(e.is_valid())

    def test_volunteer_creation(self):
        v = Volunteer(name="Bob", skills=["Python", "Docker"])
        self.assertEqual(v.name, "Bob")
        self.assertIn("Python", v.skills)
        self.assertTrue(v.is_available())

    def test_announcement_creation(self):
        a = Announcement(title="New feature", body="Please check the docs")
        self.assertEqual(a.title, "New feature")
        self.assertTrue(a.is_valid())


if __name__ == "__main__":
    unittest.main()
