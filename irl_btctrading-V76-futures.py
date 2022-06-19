#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 18:42:29 2022

@author: yannick
"""
#fork from irl_bitcoin-V15.py

import requests
import time
from binance.client import Client

time0 = time.time()
api_key = "GjwGiZnhWcMUQyxJqNzHU5WiZkicRF00iLMZONYrvSWmwlk4DRnSBm98tnSE3xzF"
api_secret = "teJ7r78Xn3kNKFV80YZNpdyIo1shEVmu6Yaeb8EGktH7ZTVoBjk4eWgRELGgtpvm"
binance_client = Client(api_key, api_secret)

wallet = 100
bitcoin_new = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
bitcoin_old = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
portfolio = 100/bitcoin_new
W = 100
Wallet = []
n = 0
t = []
btc_value = []

while wallet<1100:
    bitcoin_old = bitcoin_new
    bitcoin_new = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
    if bitcoin_new > bitcoin_old*1.0015 :
        wallet = portfolio*bitcoin_new -0.1
        n += 1
        t.append(n)
        Wallet.append(wallet)
        print('bitcoin =',bitcoin_new)
        print('temps = ', n)
        print('wallet = ',wallet)
    if bitcoin_old > bitcoin_new*1.0015 :
        portfolio = (wallet-0.1)/bitcoin_new
        print('bitcoin =',bitcoin_new)
        print('temps = ', n)
        print('wallet = ',wallet)
    time.sleep(1)
    btc_value.append(bitcoin_new)
time1 = time.time()
print('tenps total = ',time1-time0)
