# === Stage 24: Add grouped summaries by category or status ===
# Project: CommunityDesk
def generate_grouped_summary(data, key_field='category'):
    groups = {}
    for item in data:
        k = item.get(key_field) or 'Uncategorized'
        if k not in groups:
            groups[k] = {'count': 0, 'total_value': 0}
        groups[k]['count'] += 1
        if isinstance(item.get('value'), (int, float)):
            groups[k]['total_value'] += item['value']
    return {k: v for k, v in sorted(groups.items(), key=lambda x: -x[1]['count'])}
