#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 13:19:39 2022

@author: yannick
"""

from binance.client import Client

api_key = "GjwGiZnhWcMUQyxJqNzHU5WiZkicRF00iLMZONYrvSWmwlk4DRnSBm98tnSE3xzF"
api_secret = "teJ7r78Xn3kNKFV80YZNpdyIo1shEVmu6Yaeb8EGktH7ZTVoBjk4eWgRELGgtpvm"
binance_client = Client(api_key, api_secret)
leverage = 20
dollar = 100


btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
btc_prevprice = btc_newprice
btc_wallet = True
            
while True :
    try :
        btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
                
        # btc bot
        if btc_newprice > btc_prevprice and btc_wallet == False:
            dollar += dollar * (btc_newprice/btc_prevprice-1)*20
            btc_prevprice = btc_newprice
            btc_wallet = True
            print("sell btc, btc_price =",btc_newprice,"wallet =",dollar,'\n')
        elif btc_newprice < btc_prevprice and btc_wallet == True:
            btc_prevprice = btc_newprice
            print("buy btc, btc_price =",btc_newprice,'\n')
            btc_wallet = False
        elif btc_newprice > btc_prevprice and btc_wallet == True :
            btc_prevprice = btc_newprice

    except KeyboardInterrupt:
        dollar += dollar * (btc_newprice/btc_prevprice-1)*20
        btc_prevprice = btc_newprice
        btc_wallet = True
        print("sell btc, btc_price =",btc_newprice,"wallet =",dollar,'\n')
        break