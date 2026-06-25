# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: CommunityDesk
def dry_run_mode():
    import sys, os
    if len(sys.argv) > 1 and sys.argv[1] == "--dry-run":
        print("DRY RUN MODE: No changes will be made to the database or files.")
        return True
    return False

def safe_add_member(name, email):
    from datetime import datetime
    dry = dry_run_mode()
    if not dry:
        with open("members.txt", "a") as f:
            record = f"{name}|{email}|member|{datetime.now().isoformat()}\n"
            f.write(record)
        print(f"[OK] Added member {name}")
    else:
        print(f"[DRY-RUN] Would add member: {name} ({email})")

def safe_add_request(topic, description):
    from datetime import datetime
    dry = dry_run_mode()
    if not dry:
        with open("requests.txt", "a") as f:
            record = f"{topic}|{description}|request|{datetime.now().isoformat()}\n"
            f.write(record)
        print(f"[OK] Created request for {topic}")
    else:
        print(f"[DRY-RUN] Would create request: {topic} - {description[:20]}...")

def safe_add_event(title, date):
    from datetime import datetime
    dry = dry_run_mode()
    if not dry:
        with open("events.txt", "a") as f:
            record = f"{title}|{date}|event|{datetime.now().isoformat()}\n"
            f.write(record)
        print(f"[OK] Scheduled event {title}")
    else:
        print(f"[DRY-RUN] Would schedule event: {title} on {date}")

def safe_add_volunteer(name, skills):
    from datetime import datetime
    dry = dry_run_mode()
    if not dry:
        with open("volunteers.txt", "a") as f:
            record = f"{name}|{skills}|volunteer|{datetime.now().isoformat()}\n"
            f.write(record)
        print(f"[OK] Registered volunteer {name}")
    else:
        print(f"[DRY-RUN] Would register volunteer: {name} with skills: {skills}")

def safe_add_announcement(text):
    from datetime import datetime
    dry = dry_run_mode()
    if not dry:
        with open("announcements.txt", "a") as f:
            record = f"{text}|announcement|{datetime.now().isoformat()}\n"
            f.write(record)
        print(f"[OK] Posted announcement")
    else:
        print(f"[DRY-RUN] Would post announcement: {text[:30]}...")
