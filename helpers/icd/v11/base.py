import asyncio
import json
import pathlib
from functools import partial

import aiofiles
import httpx

from helpers.cache_httpx import CacheHttpX
from helpers.fake_useragent.helper import get_random_user_agent
from helpers.icd.v11.schemas import BrowseGt, Root


class ICD11:
    def __init__(self, year: int | None = 2025, version: str | None = "01"):
        self._root_url = f"https://id.who.int/icd/release/11/{year}-{version}/mms"
        self._headers = {
            "referer": "https://icd.who.int/",
            "user-agent": get_random_user_agent(),
            "api-version": "v2",
            "accept-language": "en",
            "accept": "application/json",
        }
        self._cache_file = f"icd11_{year}_{version}.json"
        self._cache: Root | None = None
        self._file_folder = (
            pathlib.Path(__file__).parent.parent.parent.parent / "dataset"
        )

    async def _load(self):
        if pathlib.Path(self._file_folder / self._cache_file).is_file():
            async with aiofiles.open(
                self._file_folder / self._cache_file, "r", encoding="utf-8"
            ) as file:
                raw_data = json.loads(await file.read())
            self._cache = Root.model_validate(raw_data)

    async def _dump(self):
        if not pathlib.Path(self._file_folder / self._cache_file).is_file():
            (self._file_folder / self._cache_file).touch(exist_ok=True)
        async with aiofiles.open(
            self._file_folder / self._cache_file, "w", encoding="utf-8"
        ) as file:
            json_str = self._cache.model_dump_json(indent=4, by_alias=True)
            await file.write(json_str)

    def get_headers(self) -> dict:
        return self._headers

    async def get_token(self):
        browse_gt_url = "https://icd.who.int/browse/gt"
        async with httpx.AsyncClient(
            headers=self.get_headers(), verify=False
        ) as client:
            response = await client.get(browse_gt_url)
        data = BrowseGt.model_validate(response.json())
        if data.token is None:
            raise RuntimeError("Browse GT token not found")
        self._headers["authorization"] = f"Bearer {data.token}"

    async def _get_root_data(self) -> Root:
        async with CacheHttpX(verify=False) as client:
            response_json = await client.get_response_json(
                self._root_url, headers=self.get_headers()
            )
        return Root.model_validate_source(response_json)

    async def _get_children_data(self, data):
        async with CacheHttpX(verify=False, timeout=None) as client:
            response_json = await client.get_response_json(
                data.url, headers=self.get_headers()
            )

        new_data = data.model_validate_source(response_json)

        if hasattr(new_data, "child") and new_data.child:
            new_data.child = await asyncio.gather(
                *[self._get_children_data(child) for child in new_data.child]
            )

        return new_data

    async def get_dataset(self):
        await self._load()
        if self._cache:
            return self._cache
        await self.get_token()
        root_data = await self._get_root_data()
        root_data.child = await asyncio.gather(
            *[self._get_children_data(child) for child in root_data.child[:1]]
        )
        self._cache = root_data
        await self._dump()
        return root_data


ICD11Y2026_01 = partial(ICD11, year=2026, version="01")
ICD11Y2025_01 = partial(ICD11, year=2025, version="01")
ICD11Y2024_01 = partial(ICD11, year=2024, version="01")
ICD11Y2023_01 = partial(ICD11, year=2023, version="01")

__all__ = [
    "ICD11Y2026_01",
    "ICD11Y2025_01",
    "ICD11Y2024_01",
    "ICD11Y2023_01",
    "ICD11",
]
