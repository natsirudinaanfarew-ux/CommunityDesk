# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: CommunityDesk
def validate_community_desk(data):
    """Validate CommunityDesk data and return a report of warnings and errors."""
    errors = []
    warnings = []
    
    if 'members' not in data:
        errors.append("Missing 'members' field")
    elif isinstance(data['members'], list) and len(data['members']) == 0:
        warnings.append("No members provided")
    
    if 'requests' not in data:
        errors.append("Missing 'requests' field")
    elif isinstance(data['requests'], list):
        for req in data['requests']:
            if not isinstance(req.get('priority'), (str, int)):
                errors.append(f"Request '{req.get('id', '?')}' has invalid priority type: {type(req.get('priority'))}")
    
    if 'events' not in data:
        errors.append("Missing 'events' field")
    elif isinstance(data['events'], list) and len(data['events']) == 0:
        warnings.append("No events scheduled")
    
    if 'volunteers' not in data:
        errors.append("Missing 'volunteers' field")
    elif isinstance(data['volunteers'], dict):
        for name, info in data['volunteers'].items():
            if not isinstance(info.get('skills'), list) or len(info['skills']) == 0:
                warnings.append(f"Volunteer '{name}' has no skills listed")
    
    if 'announcements' not in data:
        errors.append("Missing 'announcements' field")
    elif isinstance(data['announcements'], list):
        for ann in data['announcements']:
            if not ann.get('title'):
                warnings.append(f"Announcement with id '{ann.get('id', '?')}' has no title")
    
    return {'errors': errors, 'warnings': warnings}
