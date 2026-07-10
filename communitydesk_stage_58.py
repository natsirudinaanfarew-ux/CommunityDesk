# === Stage 58: Add bulk update behavior for selected records ===
# Project: CommunityDesk
def bulk_update_records(self, records):
    """Update multiple records at once using a single query."""
    if not records:
        return 0
    
    self._validate_batch(records)
    
    for record in records:
        record.validate()
    
    update_query = f"""
        UPDATE {self.table_name} 
        SET name = COALESCE(name, ''), description = COALESCE(description, '')
        WHERE id IN ({', '.join(['%s'] * len(records))})
    """
    
    values_list = [r.id for r in records]
    for i, record in enumerate(records):
        values_list.append(record.name)
        values_list.append(record.description)
    
    cursor.execute(update_query, tuple(values_list))
    return cursor.rowcount
