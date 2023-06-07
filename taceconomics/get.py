# -*- coding: utf-8 -*-

import pandas as pd
import requests
import taceconomics


API     = "https://api.taceconomics.io/v2"
HEADERS = {'Content-Type': 'application/json', 'Accept':'application/json'}


def get(code):

    headers = HEADERS.copy()
    headers.update({"Authorization": "Bearer {}".format(taceconomics.api_key)})
    
    try:
        res = requests.get(f"{API}/data/{code}", headers=headers)
        res = res.json()
        if "errors" in res:
            return None
        if "data" in res:
            df = pd.DataFrame(res["data"])
            df.set_index('timestamp', inplace=True)
            df.columns = [code.lower()]
            return df

    except Exception as e:
        print(e)
        return None

    return None
  
def getpath(path):
    headers = HEADERS.copy()
    headers.update({"Authorization": "Bearer {}".format(taceconomics.api_key)})
    
    try:
        res = requests.get(f"{API}/{path}", headers=headers)
        if res.status_code == 200:
          res = res.json()
          return res

    except Exception as e:
        print(e)
        return None

    return None
 
