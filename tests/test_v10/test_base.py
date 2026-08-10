import hashlib

import pytest

from helpers.icd.v10 import (
    ICD10Y2008,
    ICD10Y2010,
    ICD10Y2014,
    ICD10Y2015,
    ICD10Y2016,
    ICD10Y2019,
)
from helpers.icd.v10.schemas import DataSet


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "icd",
    [
        ICD10Y2008,
        ICD10Y2019,
        ICD10Y2016,
        ICD10Y2015,
        ICD10Y2014,
        ICD10Y2010,
    ],
)
async def test_get_dataset(icd):
    icd10 = icd()
    dataset = await icd10.get_dataset()
    assert isinstance(dataset, list) is True
    for item in dataset:
        assert isinstance(item, DataSet) is True


def testr_hash():
    url = "httpswww.twitch.tvshuteye_orange"
    print(hashlib.sha256(url.encode()).hexdigest())
