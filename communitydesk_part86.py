# === Stage 86: Add sample command transcripts for the main CLI workflows ===
# Project: CommunityDesk
# Sample CLI transcripts for CommunityDesk main workflows
from communitydesk.cli import console


def demo_transcripts():
    """Print example command sequences a typical user might run."""
    # 1. Register as volunteer
    print(">>> register --name Alice --email alice@example.com")
    print(f"   -> Registered: {console.register(name='Alice', email='alice@example.com')}")

    # 2. Browse pending requests
    print("\n>>> browse-requests --status open")
    for req in console.browse_requests(status="open"):
        print(f"   - [{req.id}] {req.title} | {req.description[:40]}...")

    # 3. Apply to a request
    print("\n>>> apply-request --id R101 --volunteer Alice --skills Python,SQL")
    console.apply_request("R101", "Alice", ["Python", "SQL"])

    # 4. Announce an event
    print("\n>>> announce-event --title 'Hackathon' --date 2025-09-20 --location Lab A")
    console.announce_event(title="Hackathon", date="2025-09-20", location="Lab A")

    # 5. List members
    print("\n>>> list-members")
    for m in console.list_members():
        print(f"   - {m.name} ({m.role})")


demo_transcripts()
