#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 12:33:03 2022

@author: yannick
"""

from binance.client import Client
import time

api_key = "GjwGiZnhWcMUQyxJqNzHU5WiZkicRF00iLMZONYrvSWmwlk4DRnSBm98tnSE3xzF"
api_secret = "teJ7r78Xn3kNKFV80YZNpdyIo1shEVmu6Yaeb8EGktH7ZTVoBjk4eWgRELGgtpvm"
binance_client = Client(api_key, api_secret)
bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
bnb_prevprice = bnb_newprice
wallet = True

while True :
    try :
        bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
        
        if bnb_prevprice > bnb_newprice*1.003 and wallet == True:
            time.sleep(180)
            if bnb_prevprice > bnb_newprice*1.01:
                time.sleep(180)
                if bnb_prevprice > bnb_newprice*1.001:
                    binance_client.futures_create_order(symbol='BNBUSDT',type='MARKET',side='BUY',quantity=0.1)
                    wallet = False
                    print("buy")
                    bnb_prevprice = bnb_newprice
        elif bnb_newprice*1.001 < bnb_prevprice and wallet==True:
            binance_client.futures_create_order(symbol='BNBUSDT',type='MARKET',side='BUY',quantity=0.1)
            wallet = False
            print("buy")
            bnb_prevprice = bnb_newprice
        elif bnb_newprice > bnb_prevprice*1.0015 and wallet==False:
            binance_client.futures_create_order(symbol='BNBUSDT',type='MARKET',side='SELL',quantity=0.1)
            wallet = True
            print("sell")
            bnb_prevprice = bnb_newprice
        elif bnb_newprice > bnb_prevprice and wallet==True:
            bnb_prevprice = bnb_newprice
        time.sleep(30)

    except KeyboardInterrupt:
        if wallet == False:
            while bnb_newprice < bnb_prevprice*1.001:
                bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
            binance_client.futures_create_order(symbol='BNBUSDT',type='MARKET',side='SELL',quantity=0.8)
        break