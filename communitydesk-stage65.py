# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: CommunityDesk
def dedupe_imports(imports, seen=None):
    if seen is None:
        seen = set()
    result = []
    for imp in imports:
        key = (imp.module, getattr(imp, 'name', ''))
        if key not in seen:
            seen.add(key)
            result.append(imp)
    return result
