#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 22:23:58 2019

@author: nabiilaujeemuddee
"""

import requests
import datetime
import json
from pandas.io.json import json_normalize
import pandas as pd
from datetime import datetime, timedelta
import os
import numpy as np

os.chdir("/Users/HP/")
ydy = (datetime.today() - timedelta(days=1)).strftime('%Y%m%d')

today = (datetime.today()).strftime('%Y%m%d')
print (today)

# All events except Checkout
event_name = ('Susbcription Charged','VideoWatched')
        
data = []
for i in event_name:
    print (i)
    url = 'https://api.clevertap.com/1/events.json?batch_size=6000'

    payload = {"event_name": i, "from": 20200615, "to": 20200722}
    headers = {'X-CleverTap-Account-Id':'464-R89-Z75Z','X-CleverTap-Passcode':'AMA-IQV-STKL', 'content-type': 'application/json'}
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    cursor = json.loads(response.content)

    # GET
    next_cursor = cursor['cursor']

    while next_cursor != None:
        url = "https://api.clevertap.com/1/events.json?cursor=" + next_cursor
        headers = {'X-CleverTap-Account-Id':'464-R89-Z75Z','X-CleverTap-Passcode':'AMA-IQV-STKL', 'content-type': 'application/json'}
        myResponse = requests.get(url, headers=headers, verify=True)
        if (myResponse.ok):

            jData = json.loads(myResponse.content)

            if len(jData) == 3:
                df = pd.DataFrame.from_dict(json_normalize(jData['records']), orient='columns')
                df['Identifier'] = i
                data.append(df)
                next_cursor = jData['next_cursor']

            else:
                break
        else:
            # If response code is not ok (200), print the resulting http error code with description
            myResponse.raise_for_status()

data = pd.concat(data, axis=0, sort=False)
data['date'] = pd.to_datetime(data['ts'], format='%Y%m%d%H%M%S')
data.to_csv('azamtv_clevertap_July130batch_%s.csv'%ydy, sep=',', encoding='utf-8', index=False)

