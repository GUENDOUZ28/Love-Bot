import os
import random
from datetime import datetime, date
from pathlib import Path
from dotenv import load_dotenv

# Load .env file
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

# Bot Token
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()

# User IDs (convert to int if provided)
def _parse_id(val):
    try:
        return int(val) if val and val.strip() else None
    except ValueError:
        return None

HAKIM_USER_ID = _parse_id(os.getenv("HAKIM_USER_ID"))
FATIMA_USER_ID = _parse_id(os.getenv("FATIMA_USER_ID"))

# Names
BOYFRIEND_NAME = os.getenv("BOYFRIEND_NAME", "Hakim").strip()
GIRLFRIEND_NAME = os.getenv("GIRLFRIEND_NAME", "Fatima").strip()

# Nicknames
_fatima_nicks_raw = os.getenv(
    "FATIMA_NICKNAMES",
    "Fatima,Fatimati,Hayati,Mon amour,Habibati,Princesse,My Queen,Amouna,Mon bébé,Omri,Ntiya kolchi"
)
FATIMA_NICKNAMES = [n.strip() for n in _fatima_nicks_raw.split(",") if n.strip()]

_hakim_nicks_raw = os.getenv(
    "HAKIM_NICKNAMES",
    "Hakim,Mon cœur,Habibi,Mon amour,My prince,Hbibi,Omri"
)
HAKIM_NICKNAMES = [n.strip() for n in _hakim_nicks_raw.split(",") if n.strip()]

# Anniversary Date (defaults to 2024-01-01 if not set)
ANNIVERSARY_DATE_STR = os.getenv("ANNIVERSARY_DATE", "2024-01-01").strip()

def get_anniversary_date() -> date:
    try:
        return datetime.strptime(ANNIVERSARY_DATE_STR, "%Y-%m-%d").date()
    except Exception:
        return date(2024, 1, 1)

def get_random_fatima_nickname() -> str:
    return random.choice(FATIMA_NICKNAMES)

def get_random_hakim_nickname() -> str:
    return random.choice(HAKIM_NICKNAMES)

def is_authorized(user_id: int) -> bool:
    """If both IDs are configured, restrict access. Otherwise allow anyone so they can set it up."""
    if HAKIM_USER_ID is not None and FATIMA_USER_ID is not None:
        return user_id in (HAKIM_USER_ID, FATIMA_USER_ID)
    return True

def identify_user(user_id: int, user_first_name: str = "") -> str:
    """Returns 'fatima', 'hakim', or 'guest'"""
    if FATIMA_USER_ID is not None and user_id == FATIMA_USER_ID:
        return "fatima"
    if HAKIM_USER_ID is not None and user_id == HAKIM_USER_ID:
        return "hakim"
    # Fallback heuristic based on Telegram first name
    lower_first = user_first_name.lower()
    if "fatima" in lower_first or "fatim" in lower_first:
        return "fatima"
    if "hakim" in lower_first or "abdel" in lower_first:
        return "hakim"
    return "guest"
