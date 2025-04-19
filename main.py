import asyncio
from helpers.v10.base import ICD10Y2008, ICD10Y2010, ICD10Y2014, ICD10Y2015, ICD10Y2016, ICD10Y2019


async def main():
    await asyncio.gather(
        ICD10Y2008().get_dataset(),
        ICD10Y2010().get_dataset(),
        ICD10Y2014().get_dataset(),
        ICD10Y2015().get_dataset(),
        ICD10Y2016().get_dataset(),
        ICD10Y2019().get_dataset(),
    )


if __name__ == '__main__':
    asyncio.run(main())
