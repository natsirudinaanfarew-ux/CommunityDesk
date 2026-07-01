# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: CommunityDesk
COMMUNITY_DESK_SETTINGS = {
    "app_name": "CommunityDesk",
    "version": "1.0.33",
    "max_request_comments": 5,
    "event_notification_delay": 60,
    "volunteer_approval_required": True,
    "announcement_max_length": 280,
}

def update_settings(key: str, value):
    if key in COMMUNITY_DESK_SETTINGS:
        COMMUNITY_DESK_SETTINGS[key] = value
        return True
    raise KeyError(f"Unknown setting key: {key}")

def get_setting(key: str) -> any:
    try:
        return COMMUNITY_DESK_SETTINGS[key]
    except KeyError:
        return None
