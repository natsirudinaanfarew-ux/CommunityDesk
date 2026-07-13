# === Stage 60: Add saved views for frequently used filters ===
# Project: CommunityDesk
class SavedView:
    """Compact saved-view manager for frequently used filters."""

    def __init__(self, data, view_name):
        self.data = data
        self.view_name = view_name

    def save(self, key="default"):
        return {"key": key, "view_name": self.view_name}

    @staticmethod
    def load(key="default", views=None):
        if views is None:
            views = {}
        return views.get(key)

    @staticmethod
    def delete(key="default", views=None):
        if views is None:
            views = {}
        del views[key]
