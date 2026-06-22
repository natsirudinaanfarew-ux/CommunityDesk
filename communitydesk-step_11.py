# === Stage 11: Add JSON export for the current application state ===
# Project: CommunityDesk
def export_state_to_json():
    import json
    from pathlib import Path
    
    def load_module_data(module_name):
        try:
            return getattr(sys.modules[__name__], f"{module_name}_data", {})
        except AttributeError:
            return {}

    state = {
        "members": load_module_data("members"),
        "requests": load_module_data("requests"),
        "events": load_module_data("events"),
        "volunteers": load_module_data("volunteers"),
        "announcements": load_module_data("announcements")
    }

    output_path = Path(__file__).parent / "communitydesk_state.json"
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
        
    print(f"[INFO] State exported to {output_path}")

if __name__ == "__main__":
    export_state_to_json()
