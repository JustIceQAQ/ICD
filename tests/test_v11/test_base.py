import pytest

from helpers.icd.v11.base import (
    ICD11Y2023_01,
    ICD11Y2024_01,
    ICD11Y2025_01,
    ICD11Y2026_01,
)
from helpers.icd.v11.schemas import Root


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "icd",
    [
        ICD11Y2024_01,
        ICD11Y2025_01,
        ICD11Y2023_01,
        ICD11Y2026_01,
    ],
)
async def test_get_dataset(icd):
    icd11 = icd()
    dataset = await icd11.get_dataset()
    assert isinstance(dataset, Root) is True
