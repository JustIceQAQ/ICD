from typing import Self

import httpx2 as httpx

from helpers.cache import DiskCache
from helpers.communication.base64 import Base64Helper
from helpers.hash.sha256 import get_hash


class CacheHttpX:
    def __init__(self, *args, **kwargs):
        self.cache = DiskCache()
        self.client = httpx.AsyncClient(*args, **kwargs)

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.aclose()

    async def get_response_json(self, url: str, *args, **kwargs) -> dict:
        hash_url = get_hash(url)
        get_cache_value = await self.cache.get(hash_url)
        if get_cache_value:
            return Base64Helper.decode(get_cache_value)
        response = await self.client.get(url, *args, **kwargs)
        while response.is_redirect:
            response = await self.client.get(response.next_request.url, *args, **kwargs)
        response.raise_for_status()
        data = response.json()
        encoded_data = Base64Helper.encode(data)
        await self.cache.set(hash_url, encoded_data)
        return data
