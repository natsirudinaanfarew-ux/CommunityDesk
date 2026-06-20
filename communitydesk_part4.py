# === Stage 4: Implement create operations for the primary records ===
# Project: CommunityDesk
from typing import Optional, List
import uuid
from datetime import datetime

class Member:
    def __init__(self, name: str, email: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email

class Request:
    def __init__(self, title: str, description: str, status: str = "open"):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.status = status
        self.created_at = datetime.now()

class Event:
    def __init__(self, name: str, date: datetime):
        self.id = str(uuid.uuid4())
        self.name = name
        self.date = date

class Announcement:
    def __init__(self, title: str, content: str):
        self.id = str(uuid.uuid4())
        self.title = title
        self.content = content
