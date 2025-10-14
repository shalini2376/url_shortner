# TODO: Implement your data models here
# Consider what data structures you'll need for:
# - Storing URL mappings
# - Tracking click counts
# - Managing URL metadata

import threading 

from app.utils import generate_short_code, now_iso

URL_STORE = {} 

# A lock to make operations thread-safe
# A threading lock so multiple requests don’t mess up the data at the same time.
LOCK = threading.Lock()

def create_mapping(long_url):
    with LOCK:
        while True:
            short_code = generate_short_code()
            if short_code not in URL_STORE:
                break
        
        URL_STORE[short_code] = {
            "url": long_url,
            "created_at": now_iso(),
            "clicks": 0,
        }
        return short_code 
    

def get_mapping(short_code):
    return URL_STORE.get(short_code)

def increment_clicks(short_code):
    with LOCK:
        if short_code in URL_STORE:
            URL_STORE[short_code]["clicks"] += 1
            return URL_STORE[short_code]["clicks"]
    return None