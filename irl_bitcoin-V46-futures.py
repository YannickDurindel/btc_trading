#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 10:02:00 2022

@author: yannick
"""

from binance.client import Client
import time

api_key = "GjwGiZnhWcMUQyxJqNzHU5WiZkicRF00iLMZONYrvSWmwlk4DRnSBm98tnSE3xzF"
api_secret = "teJ7r78Xn3kNKFV80YZNpdyIo1shEVmu6Yaeb8EGktH7ZTVoBjk4eWgRELGgtpvm"
binance_client = Client(api_key, api_secret)
XRP_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
XRP_prevprice = XRP_newprice
wallet = False

while True :
    try :
        XRP_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])

        if XRP_prevprice > XRP_newprice*1.003 and wallet == True:
            time.sleep(180)
            if XRP_prevprice > XRP_newprice*1.001:
                time.sleep(180)
                if XRP_prevprice > XRP_newprice*1.0015:
                    binance_client.futures_create_order(symbol='XRPUSDT',type='MARKET',side='BUY',quantity=15)
                    wallet = False
                    print("buy")
                    XRP_prevprice = XRP_newprice
        elif XRP_newprice*1.001 < XRP_prevprice and wallet==True:
            binance_client.futures_create_order(symbol='XRPUSDT',type='MARKET',side='BUY',quantity=15)
            wallet = False
            print("buy")
            XRP_prevprice = XRP_newprice
        elif XRP_newprice > XRP_prevprice*1.0015 and wallet==False:
            binance_client.futures_create_order(symbol='XRPUSDT',type='MARKET',side='SELL',quantity=15)
            wallet = True
            print("sell")
            XRP_prevprice = XRP_newprice
        elif XRP_newprice > XRP_prevprice and wallet==True:
            XRP_prevprice = XRP_newprice
        time.sleep(30)           

    except KeyboardInterrupt:
        if wallet == False:
            while XRP_newprice < XRP_prevprice*1.001:
                XRP_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
            binance_client.futures_create_order(symbol='XRPUSDT',type='MARKET',side='SELL',quantity=30)
        break
    
#https://www.binance.com/en/trade/BTC_BUSD?layout=pro