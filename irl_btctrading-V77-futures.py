#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 18:55:22 2022

@author: yannick
"""

from binance.client import Client
import time

api_key = "wsWyaiQ0dlAWj4eFE4AdvbOtmtnj2sKTMv3f53CRy6NsGIBdTZy3ZxUggAMOZr1f"
api_secret = "AlBOMFfj60b6xjWldKv6Vex5l4y4REqrU2e17XIbeRmAJVZ4Jakh7CdgSu5U5mid"
binance_client = Client(api_key, api_secret)
btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
btc_prevprice = btc_newprice
W = 100
P = 0
print("TO THE MOON !!!")

while True :
    try:
        btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
        if btc_newprice > btc_prevprice*1.0015 and W == 0:
            W = P*btc_newprice*20
            print("sell, wallet = ",W,"$")
            btc_prevprice = btc_newprice
        elif btc_newprice*1.0015 < btc_prevprice and P == 0:
            P = W/(btc_newprice*20)
            print("buy")
            btc_prevprice = btc_newprice
        elif btc_newprice > btc_prevprice and P == 0:
            btc_prevprice = btc_newprice
        elif btc_newprice*1.002 > btc_prevprice and W == 0:
            W = P*btc_newprice*20
            print("sell, wallet =",W)
        time.sleep(1)
        
    except Exception as e:
        print("Error:", e,'\n')
        time.sleep(1)
        pass
    
    except KeyboardInterrupt:
        W = P*btc_newprice*20
        print("sell, wallet = ",W,"$")
        break