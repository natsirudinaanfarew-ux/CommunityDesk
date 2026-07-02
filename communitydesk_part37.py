# === Stage 37: Add recommendations for the next useful action ===
# Project: CommunityDesk
from typing import Optional, List, Dict
import random
from datetime import datetime, timedelta

def get_next_action(user_profile: Dict, recent_events: List[Dict], pending_requests: List[Dict]) -> Optional[str]:
    """Generates a human-like next action recommendation based on context."""
    
    # Check for urgent requests needing immediate attention
    if pending_requests and random.random() < 0.3:
        urgent = min(pending_requests, key=lambda r: datetime.fromisoformat(r['deadline']) - datetime.now())
        return f"Review request #{urgent.get('id', 'unknown')} due in {int((datetime.fromisoformat(urgent['deadline']) - datetime.now()).total_seconds() / 60)} minutes."

    # Check if user has attended many events recently (suggest rest or new topic)
    recent_count = sum(1 for e in recent_events if e.get('attended', False))
    if recent_count > 3:
        return "You've been active lately. Consider reviewing community guidelines or helping with onboarding."

    # Randomly suggest checking announcements or volunteering
    actions_pool = [
        "Check the latest announcements for new opportunities.",
        "Volunteer for an upcoming event you haven't seen yet.",
        "Review pending requests to see if any match your skills.",
        "Update your profile with recent achievements."
    ]
    
    return random.choice(actions_pool)
