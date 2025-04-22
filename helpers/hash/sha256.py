import hashlib
from functools import lru_cache


@lru_cache()
def get_hash(value: str):
    return hashlib.sha256(value.encode()).hexdigest()
