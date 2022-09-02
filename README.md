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
taceconomics.api_key = "sk-..."

# get IMF/WEO data
gdp = taceconomics.get("WEO/GDP/BRA")
print(gdp)
```
