"""
Utility helpers for the URL shortener:
- URL validation
- Short-code generation (6 alphanumeric chars)
- Timestamp helper
"""

import secrets
import string 
import datetime
from urllib.parse import urlparse 

SHORT_CODE_LENGTH = 6 
MAX_URL_LENGTH = 2000 

def is_valid_url(url: str) -> bool:
    if not url or not isinstance(url, str):
        return False 
    
    url = url.strip()
    if len(url) > MAX_URL_LENGTH:
        return False
    
    parsed = urlparse(url)
        # urlparse (from Python’s urllib.parse module) breaks a URL into parts:
        # scheme (http, https),
        # netloc (example.com),
        # path (/page),
        # query (?id=1), etc.
    if parsed.scheme not in ("http", "https"):
        return False 
    if not parsed.netloc:
        return False 
    
    # Reject whitespace inside URL
    if any(c.isspace() for c in url):
        return False 

    return True 

def normalize_url(url: str) -> str:
    return url.strip()


def generate_short_code(length: int = SHORT_CODE_LENGTH) -> str:
    alphabet = string.ascii_letters + string.digits 
    return "".join(secrets.choice(alphabet) for _ in range(length))

def now_iso() -> str:
    return datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

