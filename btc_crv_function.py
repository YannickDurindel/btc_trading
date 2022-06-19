#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 14:20:31 2022

@author: yannick
"""

import requests
import time
import matplotlib.pyplot as plt
    
def btc_crv():
    t = []
    btc_val = []
    t0 = time.time()
    t.append(t0)
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    btc_val.append(int(data["bpi"]["EUR"]["rate"][0:2]+data["bpi"]["EUR"]["rate"][3:6]+data["bpi"]["EUR"]["rate"][7:13])*0.0001)
    plt.plot(t, btc_val)
    plt.xlabel('Time  (s)')
    plt.ylabel('bitcoin value (EUR)')
    plt.title("bitcoin curve")
    plt.show()
            
btc_crv()