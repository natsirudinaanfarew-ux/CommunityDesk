# === Stage 31: Add compact table rendering for long lists ===
# Project: CommunityDesk
def render_compact_table(data, columns=None):
    if not data: return ""
    if columns is None: columns = list(data[0].keys())
    width_map = {col: max(len(str(row.get(col, ''))) for row in data) + 2 for col in columns}
    header_line = " | ".join(f"{col[:width_map[col]]}" for col in columns)
    separator   = "-+-".join("-" * (width_map[col] + 2) for col in columns)
    lines       = [header_line, separator]
    for row in data:
        line = " | ".join(f"{row.get(col, '')[:width_map[col]]}" for col in columns)
        lines.append(line)
    return "\n".join(lines)
