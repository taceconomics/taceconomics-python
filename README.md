# TAC ECONOMICS Python Package

This is TAC ECONOMICS' Python package. This package uses the TAC ECONOMICS API.

License provided by MIT.

For more information please contact info@taceconomics.com

# Installation

The installation process varies depending on your python version and system used. However in most cases the following should work:

```sh
pip install --upgrade git+https://github.com/taceconomics/taceconomics-python.git
```

Alternatively on some systems python3 may use a different pip executable and may need to be installed via an alternate pip command. For example:

```sh
pip3 install --upgrade git+https://github.com/taceconomics/taceconomics-python.git
```

# Usage

The library needs to be configured with your account's secret key which is available on the website. Either set it as the TACECONOMICS_API_KEY environment variable before using the library:

```python
import taceconomics

# you api_key
taceconomics.api_key = "sk_..."

# get EIA data
brent = taceconomics.get("eia/BREPUUS/wld")
print(brent)
```


# Direct Queries

In case you cannot install TAC ECONOMICS Python library, please use the following code to query our API:

```python
import requests
import pandas as pd

def query(symbol, api_key):
    res = requests.get(f"https://api.taceconomics.io/v2/data/{symbol}?api_key={api_key}").json()
    if "data" in res:
        data = pd.json_normalize(res, record_path=['data'])
        data.timestamp = pd.to_datetime(data['timestamp'])
        data.set_index('timestamp', inplace=True)
        return data
    return None

# you api_key
api_key = "sk_..."

# get EIA data
brent = taceconomics.get("eia/BREPUUS/wld")
print(brent)
```

# List of all Available path 

you can make a query by using the basic url path(https://api.taceconomics.io/) whith :

PATH | Description |
|---|---|
| data/datasets | List all available datasets |
| data/countries | List all countries |
| data/regions | List all regions defined |
| data/dataset_id | List all symbols for the dataset_id |
| data/dataset_id/symbol/country_id | Get data for the specified symbol and country |

When querying datas, you have a list of defined options :

OPTION | Description | value | 
|---|---|---|
| api_key | Set your apikey | Your TACECONOMICS_APIKEY |
| start_date | Set the starting date of the queried datas | date on format '%YYYY-%MM-%d' |
| end_date | Set the ending date of the queried datas | date on format '%YYYY-%MM-%d' |
| frequency | returned frequency of the query | one of 'A','Q','M','D'. Default base frequency of the indicator |
| agg_mode | aggregation mode if needed | one of 'mean','start_of_period','end_of_period','median'. Default 'mean' |

```python
brent = taceconomics.get("eia/BREPUUS/wld?start_date=2020&frequency=Q")
brent
```
