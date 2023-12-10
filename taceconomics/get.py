# -*- coding: utf-8 -*-

import pandas as pd
import requests
import taceconomics


API     = "https://api.taceconomics.io/v2"
HEADERS = {'Content-Type': 'application/json', 'Accept':'application/json'}


  
def get(path):
    headers = HEADERS.copy()
    headers.update({"Authorization": "Bearer {}".format(taceconomics.api_key)})
    
    try:
        res = requests.get(f"{API}/{path}", headers=headers, proxies={"http": taceconomics.proxy, "https": taceconomics.proxy} if taceconomics.proxy else None)
        if res.status_code == 200:
          res = res.json()
          return res

    except Exception as e:
        print(e)
        return None

    return None
 


def getdata(code):

    res = get(f"data/{code}")
       
    try:
        if res["data"] is None:
            return None
          
        df = pd.DataFrame(res["data"])
        df.set_index('timestamp', inplace=True)
        df.columns = [code.lower()]
        return df

    except Exception as e:
        print(e)
        return None

    return None
