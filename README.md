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

# get IMF/WEO data
gdp = taceconomics.get("WB/NY.GDP.PCAP.CD/BRA")
print(gdp)
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

# get IMF/WEO data
gdp = query("WB/NY.GDP.PCAP.CD/BRA", api_key)
print(gdp)
```
