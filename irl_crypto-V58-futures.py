#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:06:45 2022

@author: yannick
"""

from binance.client import Client
import time

api_key = "GjwGiZnhWcMUQyxJqNzHU5WiZkicRF00iLMZONYrvSWmwlk4DRnSBm98tnSE3xzF"
api_secret = "teJ7r78Xn3kNKFV80YZNpdyIo1shEVmu6Yaeb8EGktH7ZTVoBjk4eWgRELGgtpvm"
binance_client = Client(api_key, api_secret)
leverage = 20
dollar = 100
t0 = time.time()

btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
btc_prevprice = btc_newprice
btc_wallet = True
btc_crisis = False

while True :
    try :
        btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])

        # btc bot
        if btc_newprice > btc_prevprice*1.001 and btc_wallet == False:
            dollar += dollar * (btc_newprice/btc_prevprice-1)*20
            btc_prevprice = btc_newprice
            print("sell btc, btc_price =",btc_newprice,"wallet =",dollar,'\n')
        elif (btc_newprice*1.001 < btc_prevprice and btc_wallet == True) or btc_wallet == "unactivated":
            if btc_crisis == False:
                t1 = time.time()
                btc_wallet = "unactivated"
                btc_crisis = True
                print("lowering the price of the btc for",60,'sec\n')
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
                    if btc_crisis == True and time.time()-t1>120:
                        btc_crisis = False
                        btc_wallet = False
                        btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
            if btc_crisis == False :
                btc_prevprice = btc_newprice
                print("buy btc, btc_price =",btc_newprice,'\n')
                btc_wallet = False
        elif btc_newprice > btc_prevprice and btc_wallet == True:
            time.sleep(5)
            btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
            if btc_newprice > btc_prevprice : 
                btc_prevprice = btc_newprice
        elif btc_newprice*1.05 < btc_prevprice and btc_wallet == False:
            print("We've been fucked ... but it could have been much worse !\n")
            dollar += dollar * (btc_newprice/btc_prevprice-1)*20
            btc_prevprice = btc_newprice
            print("sell btc, btc_price =",btc_newprice,"wallet =",dollar,'\n')    
            btc_wallet = True
            
    except KeyboardInterrupt:
        wait = input("The assessment of 'you can wait' is True or False ?")

        if wait == False:
            if btc_wallet==False:
                dollar += dollar * (btc_newprice/btc_prevprice-1)*leverage
                btc_prevprice = btc_newprice
                print("sell BTC, btc_price =",btc_newprice,"wallet =",dollar,'\n')    
                btc_wallet = True
        
        else :
            while btc_wallet == False :
                print("you'll have to wait a bit")
                btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
                
                if btc_newprice > btc_prevprice*1.0001:
                    dollar += dollar * (btc_newprice/btc_prevprice-1)*leverage
                    btc_prevprice = btc_newprice
                    print("sell BTC, btc_price =",btc_newprice,"wallet =",dollar,'\n')    
                    btc_wallet = True
                    
        tf = time.time()
        print("it took",tf-t0,"to raise",((dollar/100)-1)*100,"%")
        break