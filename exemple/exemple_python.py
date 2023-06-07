import taceconomics
import itertools
import pandas as pd
import os
import requests

pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 10)


# you api_key
taceconomics.api_key = "YOUR_API_KEY"

######################################################################
#                             Basic Usage
######################################################################
# Search data of interest
search = "brent"
s = taceconomics.get(f"data/search?q={search}")["data"]
pd.DataFrame(s)


# Get single data
brent_tac = taceconomics.getdata("stf/brent_f/WLD")
brent_eia = taceconomics.getdata("EIA/BREPUUS/WLD")

# Get single data with additional options
options = "collapse=Q&transform=growth_yoy"
brent_eia = taceconomics.getdata(f"EIA/BREPUUS/WLD?{options}")


# Search all symbol for a defined dataset
ds = "stf"
s = taceconomics.get(f"data/search?dataset={ds}")["data"]
pd.DataFrame(s)



######################################################################
#                        Advanced manipulations
######################################################################


# Define lists of countries and symbols of interest
list_cnt     = ['FRA','DEU','ITA']
list_symbols = ['eurostat/ei_cphi_m_cp-hi00xef_nsa_rt1','eurostat/ei_cphi_m_cp-hi00xes_nsa_rt12']

# Combine those lists
list_codes   = [a + "/" + str(b) for a, b in itertools.product(list_symbols, list_cnt)]

# Get and merge all codes in list_code to a single dataframe
# Set the options if necessary (otherwise options = "")
options = "?collapse=A&transform=diff"
res = None
for code in list_codes:
  xx = taceconomics.getdata(code + options)
  if res is None:
    res = xx
  else:
    res = pd.concat([res, xx], axis=1)
  
# Transform the res dataframe in a panel
res_panel = pd.melt(res.reset_index(), id_vars = "timestamp",var_name='code')

# Add Explicit columns dataset/symbol/country_id based on codes
split_code = res_panel.code.str.split("/")
res_panel["dataset"]    = [x[0] for x in split_code]
res_panel["symbol"]     = [x[1] for x in split_code]
res_panel["country_id"] = [x[2] for x in split_code]


