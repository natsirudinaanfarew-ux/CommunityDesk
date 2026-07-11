# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: CommunityDesk
def bulk_delete(items, confirm_flag):
    """Delete multiple items only when a confirmation flag is set."""
    if not isinstance(items, list) or len(items) == 0:
        raise ValueError("items must be a non-empty list")
    if not confirm_flag:
        print(f"Refusing to delete {len(items)} item(s): confirmation required.")
        return False
    deleted = []
    for item in items:
        try:
            del item["deleted_at"]
            item["status"] = "deleted"
            deleted.append(item)
        except KeyError as e:
            raise RuntimeError(f"Missing field {e}") from None
    if deleted:
        print(f"Deleted {len(deleted)} item(s).")
    return deleted
