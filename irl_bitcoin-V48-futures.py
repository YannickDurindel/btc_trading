#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 21:53:02 2022

@author: yannick
"""

from binance.client import Client
import time

api_key = "GjwGiZnhWcMUQyxJqNzHU5WiZkicRF00iLMZONYrvSWmwlk4DRnSBm98tnSE3xzF"
api_secret = "teJ7r78Xn3kNKFV80YZNpdyIo1shEVmu6Yaeb8EGktH7ZTVoBjk4eWgRELGgtpvm"
binance_client = Client(api_key, api_secret)
ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
ada_prevprice = ada_newprice
wallet = True

while True :
    try :
        ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
        
        if ada_prevprice > ada_newprice*1.003 and wallet == True:
            time.sleep(180)
            if ada_prevprice > ada_newprice*1.01:
                time.sleep(180)
                if ada_prevprice > ada_newprice*1.0015:
                    binance_client.futures_create_order(symbol='ADAUSDT',type='MARKET',side='BUY',quantity=50)
                    print("buy")
                    ada_prevprice = ada_newprice
        elif ada_newprice*1.001 < ada_prevprice and wallet==True:
            binance_client.futures_create_order(symbol='ADAUSDT',type='MARKET',side='BUY',quantity=50)
            wallet = False
            print("buy")
            ada_prevprice = ada_newprice
        elif ada_newprice > ada_prevprice*1.0015 and wallet==False:
            binance_client.futures_create_order(symbol='ADAUSDT',type='MARKET',side='SELL',quantity=50)
            wallet = True
            print("sell")
            ada_prevprice = ada_newprice
        elif ada_newprice > ada_prevprice and wallet==True:
            ada_prevprice = ada_newprice
        time.sleep(30)

    except KeyboardInterrupt:
        if wallet == False:
            while ada_newprice < ada_prevprice*1.001:
                ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
            binance_client.futures_create_order(symbol='ADAUSDT',type='MARKET',side='SELL',quantity=100)
        break