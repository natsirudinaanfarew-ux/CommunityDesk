# === Stage 64: Add validation for relationship references ===
# Project: CommunityDesk
class RelationshipValidationError(Exception):
    """Raised when a relationship reference cannot be resolved."""
    pass


def validate_relationship_references(relationships, members=None, events=None):
    if members is None:
        members = {}
    if events is None:
        events = {}
    
    for rel in relationships:
        required_refs = []
        ref_map = {
            'member': lambda r: (r.get('member_id') or r.get('from_member'), members),
            'event': lambda r: (r.get('event_id') or r.get('to_event'), events),
            'volunteer': lambda r: (r.get('volunteer_id'), {}),
        }
        
        for rel_type in ('member', 'event'):
            if rel.get(rel_type):
                key, lookup = ref_map[rel_type]
                resolved = lookup.get(key)
                if not resolved:
                    raise RelationshipValidationError(
                        f"Cannot resolve {rel_type} reference: '{key}' "
                        f"in relationship {id(rel)}."
                    )

    return True
