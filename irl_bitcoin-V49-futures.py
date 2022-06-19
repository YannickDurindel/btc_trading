#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 13:31:48 2022

@author: yannick
"""

from binance.client import Client
import time

api_key = "GjwGiZnhWcMUQyxJqNzHU5WiZkicRF00iLMZONYrvSWmwlk4DRnSBm98tnSE3xzF"
api_secret = "teJ7r78Xn3kNKFV80YZNpdyIo1shEVmu6Yaeb8EGktH7ZTVoBjk4eWgRELGgtpvm"
binance_client = Client(api_key, api_secret)
eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
eth_prevprice = eth_newprice
leverage = 20
dollar = 100
wallet = True


while True :
    try :
        eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
        if eth_newprice > eth_prevprice*1.001 and wallet == False:
            dollar += dollar * (eth_newprice/eth_prevprice-1)*20
            eth_prevprice = eth_newprice
            print("sell, eth_price =",eth_newprice,"wallet =",dollar,'\n')
            wallet = True
        elif eth_newprice*1.001 < eth_prevprice and wallet == True:
            time.sleep(30)
            eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
            if eth_newprice*1.003 < eth_prevprice:
                time.sleep(120)
                eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
                if eth_newprice*1.01< eth_newprice:
                    time.sleep(120)
                    eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
                    eth_prevprice = eth_newprice
            eth_prevprice = eth_newprice
            print("buy, eth_price =",eth_newprice,'\n')
            wallet = False
        elif eth_newprice > eth_prevprice and wallet == True:
            time.sleep(5)
            eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
            if eth_newprice > eth_prevprice : 
                eth_prevprice = eth_newprice
        elif eth_newprice*1.01 < eth_prevprice and wallet == False:
            print("hellcase")
            dollar += dollar * (eth_newprice/eth_prevprice-1)*20
            eth_prevprice = eth_newprice
            print("sell, eth_price =",eth_newprice,"wallet =",dollar,'\n')    
            wallet = True
        
    except KeyboardInterrupt:
        if wallet==False:
            ddollar = dollar * (eth_newprice/eth_prevprice-1)*20
            eth_prevprice = eth_newprice
            print("sell, eth_price =",eth_newprice,"wallet =",dollar,'\n')    
            wallet = True
        break