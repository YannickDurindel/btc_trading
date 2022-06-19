#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 09:37:13 2022

@author: yannick
"""

from binance.client import Client
import time

api_key = "GjwGiZnhWcMUQyxJqNzHU5WiZkicRF00iLMZONYrvSWmwlk4DRnSBm98tnSE3xzF"
api_secret = "teJ7r78Xn3kNKFV80YZNpdyIo1shEVmu6Yaeb8EGktH7ZTVoBjk4eWgRELGgtpvm"
binance_client = Client(api_key, api_secret)
btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
btc_prevprice = btc_newprice
wallet = False

while True :
    try :
        btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])

        if btc_prevprice > btc_newprice*1.003 and wallet == True:
            time.sleep(180)
            if btc_prevprice > btc_newprice*1.01:
                time.sleep(180)
                if btc_prevprice > btc_newprice*1.0015:
                    binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='BUY',quantity=0.06)
                    wallet = False
                    print("buy")
                    btc_prevprice = btc_newprice
        elif btc_newprice*1.001 < btc_prevprice and wallet==True:
            binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='BUY',quantity=0.06)
            wallet = False
            print("buy")
        elif btc_newprice > btc_prevprice*1.0015 and wallet==False:
            binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=0.06)
            wallet = True
            print("sell")
        elif btc_newprice > btc_prevprice and wallet==True:
            btc_prevprice = btc_newprice
        time.sleep(30)

    except KeyboardInterrupt:
        if wallet == False:
            while btc_newprice < btc_prevprice*1.001:
                btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
            binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=0.1)
        break
    
#https://www.binance.com/en/trade/btc_BUSD?layout=pro