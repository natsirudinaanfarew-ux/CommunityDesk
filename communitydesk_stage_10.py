# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: CommunityDesk
class SearchFilter:
    def __init__(self, data):
        self.data = data
    
    def search(self, query):
        if not query: return self.data
        
        q_lower = query.lower()
        results = []
        
        for item in self.data:
            fields_to_check = [item.get('name', ''), item.get('email', ''), 
                              item.get('role', ''), item.get('status', '')]
            
            if any(q_lower in field for field in fields_to_check):
                results.append(item)
        
        return results
