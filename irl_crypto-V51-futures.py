#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 08:49:44 2022

@author: yannick
"""

from binance.client import Client
import time

api_key = "GjwGiZnhWcMUQyxJqNzHU5WiZkicRF00iLMZONYrvSWmwlk4DRnSBm98tnSE3xzF"
api_secret = "teJ7r78Xn3kNKFV80YZNpdyIo1shEVmu6Yaeb8EGktH7ZTVoBjk4eWgRELGgtpvm"
binance_client = Client(api_key, api_secret)
bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
bnb_prevprice = bnb_newprice
leverage = 20
dollar = 100
bnb_wallet = True


while True :
    try :
        bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
        if bnb_newprice > bnb_prevprice*1.001 and bnb_wallet == False:
            dollar += dollar * (bnb_newprice/bnb_prevprice-1)*leverage
            bnb_prevprice = bnb_newprice
            print("sell, bnb_price =",bnb_newprice,"bnb_wallet =",dollar,'\n')
            bnb_wallet = True
        elif bnb_newprice*1.001 < bnb_prevprice and bnb_wallet == True:
            time.sleep(30)
            bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
            if bnb_newprice*1.003 < bnb_prevprice:
                time.sleep(120)
                bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
                if bnb_newprice*1.01< bnb_newprice:
                    time.sleep(120)
                    bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
                    bnb_prevprice = bnb_newprice
            bnb_prevprice = bnb_newprice
            print("buy, bnb_price =",bnb_newprice,'\n')
            bnb_wallet = False
        elif bnb_newprice > bnb_prevprice and bnb_wallet == True:
            time.sleep(5)
            bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
            if bnb_newprice > bnb_prevprice : 
                bnb_prevprice = bnb_newprice
        elif bnb_newprice*1.01 < bnb_prevprice and bnb_wallet == False:
            print("hellcase")
            dollar += dollar * (bnb_newprice/bnb_prevprice-1)*leverage
            bnb_prevprice = bnb_newprice
            print("sell, bnb_price =",bnb_newprice,"bnb_wallet =",dollar,'\n')
            bnb_wallet = True
        
    except KeyboardInterrupt:
        if bnb_wallet==False:
            dollar += dollar * (bnb_newprice/bnb_prevprice-1)*leverage
            bnb_prevprice = bnb_newprice
            print("sell, bnb_price =",bnb_newprice,"bnb_wallet =",dollar,'\n')
            bnb_wallet = True
        break