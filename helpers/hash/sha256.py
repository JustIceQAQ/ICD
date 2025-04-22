import base64
import hashlib
from functools import lru_cache
import json


@lru_cache()
def get_hash(value: str):
    return hashlib.sha256(value.encode()).hexdigest()


class Base64Helper:
    @staticmethod
    def encode(value: dict) -> str:
        return base64.b64encode(json.dumps(value).encode()).decode()

    @staticmethod
    def decode(value: str) -> dict:
        return json.loads(base64.b64decode(value))
