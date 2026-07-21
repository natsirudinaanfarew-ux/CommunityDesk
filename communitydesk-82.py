# === Stage 82: Add an end-to-end demo function that prints a complete walkthrough ===
# Project: CommunityDesk
def demo():
    print("=== CommunityDesk End-to-End Demo ===")
    members = {"alice": 3, "bob": 2}
    events = {"workshop": "2024-12-05", "meetup": "2024-12-12"}
    requests = {"help_setup": {"by": "carol", "members_needed": 2}}
    volunteers = {"dave": ["workshop", "help_setup"], "eve": ["meetup"]}
    announcements = [
        "Welcome to CommunityDesk!",
        "The workshop is on Dec 5.",
        "We need 2 more hands for help_setup."
    ]
    print(f"Members: {members}")
    print(f"Events: {events}")
    print(f"Requests: {requests}")
    print(f"Volunteers: {volunteers}")
    print(f"Announcements:\n- {announcements[0]}\n- {announcements[1]}\n- {announcements[2]}")

demo()
