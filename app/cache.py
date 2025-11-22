# app/cache.py
import time

CACHE = {}

def get_cache(key):
    val = CACHE.get(key)
    if not val:
        return None
    value, expiry = val
    if time.time() > expiry:
        return None
    return value

def set_cache(key, value, ttl=3600):
    CACHE[key] = (value, time.time() + ttl)
