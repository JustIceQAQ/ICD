import pytest
from helpers.icd.v11.base import ICD11
import hashlib


@pytest.mark.asyncio
async def test_get_token():
    icd11 = ICD11()
    await icd11.get_token()
    assert "authorization" in icd11.get_headers()


@pytest.mark.asyncio
async def test_get_datasets():
    icd11 = ICD11()
    await icd11.get_datasets()


def testr_hash():
    url = "httpswww.twitch.tvshuteye_orange"
    print(hashlib.sha256(url.encode()).hexdigest())
