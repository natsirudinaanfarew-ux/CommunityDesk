# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: CommunityDesk
from dataclasses import dataclass, field
from datetime import date
from typing import Optional, List

@dataclass
class Member:
    id: int
    name: str
    email: str
    role: str = "member"
    joined_date: date = None
    
@dataclass 
class Request:
    id: int
    title: str
    description: str
    status: str = "open"
    assigned_to: Optional[int] = None

@dataclass
class Event:
    id: int
    name: str
    start_date: date
    end_date: date
    location: str
    attendees: List[int] = field(default_factory=list)

@dataclass
class Volunteer:
    id: int
    member_id: Optional[int] = None
    skills: List[str] = field(default_factory=list)
    availability: str = "flexible"

@dataclass
class Announcement:
    id: int
    title: str
    content: str
    published_date: date
    author_id: Optional[int] = None
