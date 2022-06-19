#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 20:36:42 2021

@author: yannick
"""

import requests
import time
import matplotlib.pyplot as plt
from binance.client import Client

btc = 0
btc_val = []
btc_irt = []
n = 0
x = []
y = []

# init
api_key = "M9FsR6XdaZKkIhHmKeCsGSdjYzVWIWGlnsMxM1n6NnTViEaOoKXsPb0ItO4usCuD"
api_secret = "3syXcf4fZ1Q0h51HNxYN8msjOe5RXzmyMm11KZvCnTCf3XGjK2nn4M0dK51qFu5i"
client = Client(api_key, api_secret)

#while n<=10 :
while n<10 :
    btc_price = float(client.get_symbol_ticker(symbol="BTCUSDT")['price'])
    btc_irt.append(btc_price)
    y.append(btc_price)
    n+=1
    print(n)
    x.append(n)
    #btc_val.append((btc_irt[0]+btc_irt[1]+btc_irt[2]+btc_irt[3]+btc_irt[4])/5)
    
current_time = time.time()
xname = 'Time  (s)' + str(current_time)
plt.plot(x,y)
plt.xlabel(xname)
plt.ylabel('avg Bitcoin value  (USD)')
plt.title('Bitcoin curve')
plt.show()