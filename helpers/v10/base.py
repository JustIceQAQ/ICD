import asyncio
import json
import pathlib
from functools import partial
from typing import Any
from helpers.v10.schemas import DataSet
import aiofiles

import httpx

LANGUAGE = "en"


class ICD10:
    def __init__(self, year: int):
        self.year = year
        self._base_url = f"https://icd.who.int/browse10/{year}/{LANGUAGE}"
        self._root_url = f"{self._base_url}/JsonGetRootConcepts?useHtml=false"
        self._children_url = (
            self._base_url + "/JsonGetChildrenConcepts?"
            "ConceptId={children_id}"
            "&useHtml=false"
            "&showAdoptedChildren=false"
        )
        self._headers = {
            "x-requested-with": "XMLHttpRequest",
            "referer": self._base_url,
        }
        self._cache_file = f"icd10_{year}_{LANGUAGE}.json"
        self._cache: list[DataSet] | None = None
        self._file_folder = pathlib.Path(__file__).parent.parent.parent / "dataset"

    async def _load(self):
        if pathlib.Path(self._file_folder / self._cache_file).is_file():
            async with aiofiles.open(self._file_folder / self._cache_file, "r") as file:
                raw_data = json.loads(await file.read())
            self._cache = [DataSet.model_validate(item) for item in raw_data]

    async def _dump(self):
        if not pathlib.Path(self._file_folder / self._cache_file).is_file():
            (self._file_folder / self._cache_file).touch(exist_ok=True)
        async with aiofiles.open(self._file_folder / self._cache_file, "w") as file:
            json_str = json.dumps(
                [item.model_dump(by_alias=True) for item in self._cache], indent=4
            )
            await file.write(json_str)

    async def get_dataset(self) -> list[DataSet]:
        await self._load()
        if self._cache:
            return self._cache
        root_data = await self.get_root_item()
        tasks = []
        for item in root_data:
            tasks.append(self.get_children(item))
        await asyncio.gather(*tasks)
        self._cache = root_data
        await self._dump()
        return root_data

    async def _get_url(self, url: str) -> list[dict[str, Any]]:
        async with httpx.AsyncClient(
            timeout=None, headers=self._headers, verify=False
        ) as client:
            response = await client.get(url)
            response.raise_for_status()
        return response.json()

    async def get_root_item(self) -> list[DataSet]:
        this_url = self._root_url
        response_json = await self._get_url(this_url)
        return [DataSet.model_validate(item) for item in response_json]

    async def get_children_item(self, children_id: str) -> list[DataSet]:
        this_url = self._children_url.format(children_id=children_id)
        response_json = await self._get_url(this_url)
        return [DataSet.model_validate(item) for item in response_json]

    async def get_children(self, dataset: DataSet):
        this_url = self._children_url.format(children_id=dataset.id)
        response_json = await self._get_url(this_url)
        dataset.items = [DataSet.model_validate(item) for item in response_json]
        tasks = []
        for item in dataset.items:
            if not item.is_leaf:
                tasks.append(self.get_children(item))

        if tasks:
            await asyncio.gather(*tasks)


ICD10Y2008 = partial(ICD10, year=2008)
ICD10Y2010 = partial(ICD10, year=2010)
ICD10Y2014 = partial(ICD10, year=2014)
ICD10Y2015 = partial(ICD10, year=2015)
ICD10Y2016 = partial(ICD10, year=2016)
ICD10Y2019 = partial(ICD10, year=2019)
