import base64
import json


class Base64Helper:
    @staticmethod
    def encode(value: dict) -> str:
        return base64.b64encode(json.dumps(value).encode()).decode()

    @staticmethod
    def decode(value: str) -> dict:
        return json.loads(base64.b64decode(value))
