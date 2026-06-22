# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: CommunityDesk
from operator import itemgetter

def sort_items(items, key='date'):
    """Sort items by title (asc), date (desc), priority (asc), or last_update."""
    if key == 'title':
        return sorted(items, key=itemgetter('title'))
    elif key == 'priority':
        return sorted(items, key=lambda x: (x.get('priority', 0) is None, x.get('priority', 1)))
    else:
        # Default sort by date descending or last_update if available
        sort_key = itemgetter(key)
        try:
            return sorted(items, key=sort_key, reverse=True)
        except TypeError:
            return items
