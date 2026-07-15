# === Stage 66: Add export of a short status dashboard ===
# Project: CommunityDesk
def show_dashboard(communities):
    print("\n=== CommunityDesk Status Dashboard ===")
    print(f"Total communities: {len(communities)}\n")
    for comm in communities:
        members = sum(len(m) for m in comm.get("members", []))
        requests = len(comm.get("requests", []))
        events = len(comm.get("events", []))
        volunteers = len(comm.get("volunteers", []))
        print(f"  {comm['name']}:")
        print(f"    Members:  {members}")
        print(f"    Requests: {requests}")
        print(f"    Events:   {events}")
        print(f"    Volunteers:{volunteers}")
    print("\n=== End Dashboard ===")
