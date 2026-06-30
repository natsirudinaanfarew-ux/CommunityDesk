# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: CommunityDesk
from datetime import datetime, date
import re

def parse_date(date_str: str) -> date | None:
    """Parse a string into a date object using common formats."""
    if not date_str or not isinstance(date_str, str):
        return None
    
    patterns = [
        (r"^\d{4}-\d{2}-\d{2}$", "%Y-%m-%d"),  # ISO format
        (r"^\d{1,2}/\d{1,2}/\d{2,4}$", None),   # MM/DD/YYYY or DD/MM/YY
        (r"^(\w+)\s+\d{1,2},?\s+\d{4}$", None),  # Month Day, Year
    ]

    for pattern, fmt in patterns:
        if re.match(pattern, date_str.strip()):
            try:
                if fmt is None:
                    candidates = [("%m/%d/%Y", "%d/%m/%Y"), ("%Y-%m-%d", "%d-%m-%y")]
                    for c_fmt in candidates:
                        d = datetime.strptime(date_str, c_fmt).date()
                        return d
                else:
                    return datetime.strptime(date_str.strip(), fmt).date()
            except ValueError:
                continue
    raise ValueError(f"Unable to parse date string: '{date_str}'")

def validate_date_range(start_str: str, end_str: str) -> tuple[date | None, date | None]:
    """Validate and return a start and end date range."""
    try:
        start = parse_date(start_str)
        end = parse_date(end_str)
        if not (start and end):
            raise ValueError("Both dates must be valid.")
        if start > end:
            raise ValueError(f"Start date '{start}' cannot be after end date '{end}'.")
        return start, end
    except ValueError as e:
        raise ValueError(f"Date range validation failed: {e}") from None
