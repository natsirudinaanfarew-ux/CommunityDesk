# === Stage 49: Add unit tests for update and delete edge cases ===
# Project: CommunityDesk
import unittest


class TestEdgeCases(unittest.TestCase):
    def test_update_nonexistent(self):
        desk = CommunityDesk()
        with self.assertRaises(ValueError):
            desk.update_member("nonexistent", {"name": "Updated"})

    def test_delete_nonexistent(self):
        desk = CommunityDesk()
        with self.assertRaises(ValueError):
            desk.delete_event("nonexistent")

    def test_update_wrong_type(self):
        desk = CommunityDesk()
        desk.add_request({"title": "Test Request", "description": "Details"})
        with self.assertRaises(TypeError):
            desk.update_request(123, {"title": "Updated"})

    def test_delete_wrong_type(self):
        desk = CommunityDesk()
        desk.add_member("John Doe")
        with self.assertRaises(TypeError):
            desk.delete_member(456)


if __name__ == "__main__":
    unittest.main()
