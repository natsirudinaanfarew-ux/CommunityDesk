# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: CommunityDesk
def format_member(m):
    return f"[{m['id']}] {m['name']} ({m['role']})"

def format_event(e):
    status = "✓" if e.get('confirmed') else "?"
    return f"{status} {e['title']} @ {e['date']}"

def format_request(r):
    priority = r.get('priority', 'normal')
    return f"[{r['id']}] {r['subject']} [{priority.upper()}]"

def format_announcement(a):
    return f"📢 {a['title']}: {a['message']}"

def print_list(items, formatter):
    if not items:
        print("  (empty)")
        return
    for item in items:
        print(f"  • {formatter(item)}")

def print_detail(obj, fields=None):
    if fields is None:
        fields = list(obj.keys())
    lines = [f"{obj['id']}:"]
    for f in fields:
        val = obj.get(f, '')
        lines.append(f"  {f}: {val}")
    print("\n".join(lines))
