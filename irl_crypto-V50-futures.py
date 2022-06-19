#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 08:48:28 2022

@author: yannick
"""

from binance.client import Client
import time

api_key = "GjwGiZnhWcMUQyxJqNzHU5WiZkicRF00iLMZONYrvSWmwlk4DRnSBm98tnSE3xzF"
api_secret = "teJ7r78Xn3kNKFV80YZNpdyIo1shEVmu6Yaeb8EGktH7ZTVoBjk4eWgRELGgtpvm"
binance_client = Client(api_key, api_secret)
ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
ada_prevprice = ada_newprice
leverage = 20
dollar = 100
ada_wallet = True


while True :
    try :
        ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
        if ada_newprice > ada_prevprice*1.001 and ada_wallet == False:
            dollar += dollar * (ada_newprice/ada_prevprice-1)*leverage
            ada_prevprice = ada_newprice
            print("sell, ada_price =",ada_newprice,"ada_wallet =",dollar,'\n')
            ada_wallet = True
        elif ada_newprice*1.001 < ada_prevprice and ada_wallet == True:
            time.sleep(30)
            ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
            if ada_newprice*1.003 < ada_prevprice:
                time.sleep(120)
                ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
                if ada_newprice*1.01< ada_newprice:
                    time.sleep(120)
                    ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
                    ada_prevprice = ada_newprice
            ada_prevprice = ada_newprice
            print("buy, ada_price =",ada_newprice,'\n')
            ada_wallet = False
        elif ada_newprice > ada_prevprice and ada_wallet == True:
            time.sleep(5)
            ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
            if ada_newprice > ada_prevprice : 
                ada_prevprice = ada_newprice
        elif ada_newprice*1.01 < ada_prevprice and ada_wallet == False:
            print("hellcase")
            dollar += dollar * (ada_newprice/ada_prevprice-1)*leverage
            ada_prevprice = ada_newprice
            print("sell, ada_price =",ada_newprice,"ada_wallet =",dollar,'\n')
            ada_wallet = True
        
    except KeyboardInterrupt:
        if ada_wallet==False:
            dollar += dollar * (ada_newprice/ada_prevprice-1)*leverage
            ada_prevprice = ada_newprice
            print("sell, ada_price =",ada_newprice,"ada_wallet =",dollar,'\n')
        break