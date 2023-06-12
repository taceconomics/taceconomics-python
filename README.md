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
brent = taceconomics.getdata("eia/BREPUUS/wld")
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
| start_date | Set the starting date of the queried datas | date on format '%yyyy-%MM-%dd' |
| end_date | Set the ending date of the queried datas | date on format '%yyyy-%MM-%dd' |
| collapse | returned frequency of the query | one of 'A','Q','M','D'. Default base frequency of the indicator |
| collapse_mode | aggregation mode if needed | one of 'mean','start_of_period','end_of_period','median'. Default 'mean' |
| transform | transformation to apply to the query | one of 'diff','diff_yoy','growth','growth_yoy'|

```python
brent = taceconomics.getdata("eia/BREPUUS/wld?start_date=2020&frequency=Q")
brent
```
You can also search for a specific symbol, dataset, country or list all results for a keywords.

PATH | Description |
|---|---|
| data/search | starting path to look for a specific search |

OPTION | Description | value | 
|---|---|---|
| q | look for all results containing the specified keyword(s) | a (list of) keyword(s) (ex : brent) |
| symbol | list of all symbols containing the specified string | a string ( ex : brent) |
| dataset | list of all symbols in the specified dataset | a string (ex : weo) |
| country | list of all symbols available for the specified country | a country ISO 3 code (ex : FRA) |
```python
taceconomics.get("data/search?q=brent")["data"]
taceconomics.get("data/search?dataset=eia")["data"]
```
