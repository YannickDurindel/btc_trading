#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 20:36:42 2021

@author: yannick
"""

import matplotlib.pyplot as plt
from binance.client import Client
import time

x = []
y = []
n = 0

# init
api_key = ""
api_secret = ""
client = Client(api_key, api_secret)

#while n<=10 :
while True :
    try :
        btc_price = float(client.get_symbol_ticker(symbol="BTCUSDT")['price'])
        x.append(n)
        n+=1
        y.append(btc_price)
        time.sleep(0.1)
    except KeyboardInterrupt :
        plt.plot(x,y)
        plt.xlabel('')
        plt.ylabel('Bitcoin value  (USD)')
        plt.title('Bitcoin curve')
        plt.show()
