# ICD Web Crawler

---

## ICD-10

----

- [ICD-10 Version:2008](https://icd.who.int/browse10/2008/en)
- [ICD-10 Version:2010](https://icd.who.int/browse10/2010/en)
- [ICD-10 Version:2014](https://icd.who.int/browse10/2014/en)
- [ICD-10 Version:2015](https://icd.who.int/browse10/2015/en)
- [ICD-10 Version:2016](https://icd.who.int/browse10/2016/en)
- [ICD-10 Version:2019](https://icd.who.int/browse10/2019/en)

```python
from helpers.icd.v10 import ICD10Y2008 # or ICD10

ccd = ICD10Y2008()
# is same as ICD10(2008)

ccd.get_dataset()
# return DataSet format

```

---

## ICD-11

----

- [ICD-11: 2025-01](https://icd.who.int/browse/2025-01/mms/en)
