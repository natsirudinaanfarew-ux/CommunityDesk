# === Stage 73: Add a lightweight HTML report export ===
# Project: CommunityDesk
def export_report(self, path="report.html"):
    """Export a lightweight HTML summary of CommunityDesk data."""
    try:
        from jinja2 import Template
        template = Template("""\
<html><head><title>CommunityDesk Report</title></head><body style="font-family:sans-serif;">
<h1>CommunityDesk Report</h1>
<p>Total members: {{ total_members }}</p>
<p>Total events: {{ total_events }}</p>
<p>Total requests: {{ total_requests }}</p>
<p>Total volunteers: {{ total_volunteers }}</p>
<hr><h2>Recent Announcements</h2>
{% for a in announcements %}
<p>{{ a.title }} – {{ a.date }}</p>
{% endfor %}</body></html>\
""")
        with open(path, "w", encoding="utf-8") as f:
            f.write(template.render(
                total_members=len(self.members) if hasattr(self, 'members') else 0,
                total_events=len(self.events) if hasattr(self, 'events') else 0,
                total_requests=len(self.requests) if hasattr(self, 'requests') else 0,
                total_volunteers=len(self.volunteers) if hasattr(self, 'volunteers') else 0,
                announcements=sorted(self.announcements or [], key=lambda x: getattr(x, "date", ""), reverse=True)[:5]
            ))
        return path
    except ImportError:
        with open(path, "w") as f:
            f.write("<html><body><h1>CommunityDesk Report</h1></body></html>")
        return path
