#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 10:22:41 2022

@author: yannick
"""

from binance.client import Client
import time
import matplotlib.pyplot as plt

api_key = "GjwGiZnhWcMUQyxJqNzHU5WiZkicRF00iLMZONYrvSWmwlk4DRnSBm98tnSE3xzF"
api_secret = "teJ7r78Xn3kNKFV80YZNpdyIo1shEVmu6Yaeb8EGktH7ZTVoBjk4eWgRELGgtpvm"
binance_client = Client(api_key, api_secret)
leverage = 20
dollar = 100
t0 = time.time()
btc_price = []
time_btc = []
trade_price = []
time_trade = []

btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
btc_prevprice = btc_newprice
btc_wallet = True
btc_crisis = False
trade_price.append(btc_newprice)
time_trade.append(time.time()-t0)
            
while True :
    try :
        btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
        btc_price.append(btc_newprice)
        time_btc.append(time.time()-t0)
                
        # btc bot
        if btc_newprice > btc_prevprice*1.001 and btc_wallet == False:
            dollar += dollar * (btc_newprice/btc_prevprice-1)*20
            btc_prevprice = btc_newprice
            print("sell btc, btc_price =",btc_newprice,"wallet =",dollar,'\n')
            trade_price.append(btc_newprice)
            time_trade.append(time.time()-t0)
        elif (btc_newprice*1.001 < btc_prevprice and btc_wallet == True) or btc_wallet == "unactivated":
            if btc_crisis == False:
                t1 = time.time()
                btc_wallet = "unactivated"
                btc_crisis = True
                print("lowering the price of the btc for",60,'sec\n')
                trade_price.append(btc_newprice)
                time_trade.append(time.time()-t0)
            if btc_crisis == True and time.time()-t1>60:
                btc_crisis = False
                btc_wallet = False
                btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
            if btc_newprice*1.003 < btc_prevprice:
                if btc_crisis == False:
                    t1 = time.time()
                    btc_wallet = "unactivated"
                    btc_crisis = True
                    print("lowering the price of the btc for",120,'sec\n')
                    trade_price.append(btc_newprice)
                    time_trade.append(time.time()-t0)
                if btc_crisis == True and time.time()-t1>120:
                    btc_crisis = False
                    btc_wallet = False
                    btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
                if btc_newprice*1.01< btc_newprice:
                    if btc_crisis == False:
                        t1 = time.time()
                        btc_wallet = "unactivated"
                        btc_crisis = True
                        print("lowering the price of the btc for",120,'sec\n')
                        trade_price.append(btc_newprice)
                        time_trade.append(time.time()-t0)
                    if btc_crisis == True and time.time()-t1>120:
                        btc_crisis = False
                        btc_wallet = True
                        btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
            if btc_crisis == False :
                btc_prevprice = btc_newprice
                print("buy btc, btc_price =",btc_newprice,'\n')
                btc_wallet = False
                trade_price.append(btc_newprice)
                time_trade.append(time.time()-t0)
        elif btc_newprice > btc_prevprice and btc_wallet == True:
            time.sleep(5)
            btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
            if btc_newprice > btc_prevprice : 
                btc_prevprice = btc_newprice
                trade_price.append(btc_newprice)
                time_trade.append(time.time()-t0)
        elif btc_newprice*1.05 < btc_prevprice and btc_wallet == False:
            print("We've been fucked ... but it could have been much worse !\n")
            dollar += dollar * (btc_newprice/btc_prevprice-1)*20
            btc_prevprice = btc_newprice
            print("sell btc, btc_price =",btc_newprice,"wallet =",dollar,'\n')    
            btc_wallet = True
            trade_price.append(btc_newprice)
            time_trade.append(time.time()-t0)
            
    except KeyboardInterrupt:
        fig, ax = plt.subplots(1, figsize=(8, 6))
        ax.plot(time_btc, btc_price, color="blue", label="btc_price")
        ax.plot(time_trade, trade_price, color="red", label="btc_trade")
        plt.show()