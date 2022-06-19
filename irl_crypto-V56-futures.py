#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 13:33:28 2022

@author: yannick
"""

from binance.client import Client
import time

api_key = "GjwGiZnhWcMUQyxJqNzHU5WiZkicRF00iLMZONYrvSWmwlk4DRnSBm98tnSE3xzF"
api_secret = "teJ7r78Xn3kNKFV80YZNpdyIo1shEVmu6Yaeb8EGktH7ZTVoBjk4eWgRELGgtpvm"
binance_client = Client(api_key, api_secret)
leverage = 20
dollar = 100 + 427.3929625438559
t0 = time.time()-26728.209102869034

btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
btc_prevprice = btc_newprice
btc_wallet = True
btc_crisis = False
btc_crisis_counter = False

eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
eth_prevprice = eth_newprice
eth_wallet = True
eth_crisis = False
eth_crisis_counter = False

xrp_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
xrp_prevprice = xrp_newprice
xrp_wallet = True
xrp_crisis = False
xrp_crisis_counter = False

ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
ada_prevprice = ada_newprice
ada_wallet = True
ada_crisis = False
ada_crisis_counter = False

bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
bnb_prevprice = bnb_newprice
bnb_wallet = True
bnb_crisis = False
bnb_crisis_counter = False




while True :
    try :
        btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
        eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
        xrp_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
        ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
        bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
        
        # btc bot
        if btc_newprice > btc_prevprice*1.001 and btc_wallet == False:
            dollar += dollar * (btc_newprice/btc_prevprice-1)*20
            btc_prevprice = btc_newprice
            print("sell btc, btc_price =",btc_newprice,"wallet =",dollar,'\n')
        elif btc_newprice*1.001 < btc_prevprice and btc_wallet == True:
            if btc_crisis == False:
                t1 = time.time()
                btc_wallet = "unactivated"
                btc_crisis = True
                btc_crisis_counter = False
                print("lowering the price of the btc for",60,'sec')
            if btc_crisis == True and time.time()-t1>60:
                btc_crisis = False
                btc_crisis_counter = True
                btc_wallet = False
                btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
            if btc_newprice*1.003 < btc_prevprice:
                if btc_crisis == False:
                    t1 = time.time()
                    btc_wallet = "unactivated"
                    btc_crisis = True
                    btc_crisis_counter = False
                    print("lowering the price of the btc for",120,'sec')
                if btc_crisis == True and time.time()-t1>120:
                    btc_crisis = False
                    btc_crisis_counter = True
                    btc_wallet = False
                    btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
                if btc_newprice*1.01< btc_newprice:
                    if btc_crisis == False:
                        t1 = time.time()
                        btc_wallet = "unactivated"
                        btc_crisis = True
                        btc_crisis_counter = False
                        print("lowering the price of the btc for",120,'sec')
                    if btc_crisis == True and time.time()-t1>120:
                        btc_crisis = False
                        btc_crisis_counter = True
                        btc_wallet = False
                        btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
            if btc_crisis_counter == True :
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
        
        # eth bot
        if eth_newprice > eth_prevprice*1.001 and eth_wallet == False:
            dollar += dollar * (eth_newprice/eth_prevprice-1)*20
            eth_prevprice = eth_newprice
            print("sell ETH, eth_price =",eth_newprice,"wallet =",dollar,'\n')
        elif eth_newprice*1.001 < eth_prevprice and eth_wallet == True:
            if eth_crisis == False:
                t1 = time.time()
                eth_wallet = "unactivated"
                eth_crisis = True
                eth_crisis_counter = False
                print("lowering the price of the eth for",60,'sec')
            if eth_crisis == True and time.time()-t1>60:
                eth_crisis = False
                eth_crisis_counter = True
                eth_wallet = False
                eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
            if eth_newprice*1.003 < eth_prevprice:
                if eth_crisis == False:
                    t1 = time.time()
                    eth_wallet = "unactivated"
                    eth_crisis = True
                    eth_crisis_counter = False
                    print("lowering the price of the eth for",120,'sec')
                if eth_crisis == True and time.time()-t1>120:
                    eth_crisis = False
                    eth_crisis_counter = True
                    eth_wallet = False
                    eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
                if eth_newprice*1.01< eth_newprice:
                    if eth_crisis == False:
                        t1 = time.time()
                        eth_wallet = "unactivated"
                        eth_crisis = True
                        eth_crisis_counter = False
                        print("lowering the price of the eth for",120,'sec')
                    if eth_crisis == True and time.time()-t1>120:
                        eth_crisis = False
                        eth_crisis_counter = True
                        eth_wallet = False
                        eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
            if eth_crisis_counter == True :
                eth_prevprice = eth_newprice
                print("buy ETH, eth_price =",eth_newprice,'\n')
                eth_wallet = False
        elif eth_newprice > eth_prevprice and eth_wallet == True:
            time.sleep(5)
            eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
            if eth_newprice > eth_prevprice : 
                eth_prevprice = eth_newprice
        elif eth_newprice*1.05 < eth_prevprice and eth_wallet == False:
            print("We've been fucked ... but it could have been much worse !\n")
            dollar += dollar * (eth_newprice/eth_prevprice-1)*20
            eth_prevprice = eth_newprice
            print("sell ETH, eth_price =",eth_newprice,"wallet =",dollar,'\n')    
            eth_wallet = True
        
        #xrp bot
        if xrp_newprice > xrp_prevprice*1.001 and xrp_wallet == False:
            dollar += dollar * (xrp_newprice/xrp_prevprice-1)*leverage
            xrp_prevprice = xrp_newprice
            print("sell XRP, xrp_price =",xrp_newprice,"wallet =",dollar,'\n')
            xrp_wallet = True
        elif xrp_newprice*1.001 < xrp_prevprice and xrp_wallet == True:
            if xrp_crisis == False:
                t1 = time.time()
                xrp_wallet = "unactivated"
                xrp_crisis = True
                xrp_crisis_counter = False
                print("lowering the price of the xrp for",60,'sec')
            if xrp_crisis == True and time.time()-t1>60:
                xrp_crisis = False
                xrp_crisis_counter = True
                xrp_wallet = False
                xrp_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
            if xrp_newprice*1.003 < xrp_prevprice:
                if xrp_crisis == False:
                    t1 = time.time()
                    xrp_wallet = "unactivated"
                    xrp_crisis = True
                    xrp_crisis_counter = False
                    print("lowering the price of the xrp for",120,'sec')
                if xrp_crisis == True and time.time()-t1>120:
                    xrp_crisis = False
                    xrp_crisis_counter = True
                    xrp_wallet = False
                    xrp_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
                if xrp_newprice*1.01< xrp_newprice:
                    if xrp_crisis == False:
                        t1 = time.time()
                        xrp_wallet = "unactivated"
                        xrp_crisis = True
                        xrp_crisis_counter = False
                        print("lowering the price of the xrp for",120,'sec')
                    if xrp_crisis == True and time.time()-t1>120:
                        xrp_crisis = False
                        xrp_crisis_counter = True
                        xrp_wallet = False
                        xrp_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
            if xrp_crisis_counter == True :
                xrp_prevprice = xrp_newprice
                print("buy xrp, xrp_price =",xrp_newprice,'\n')
                xrp_wallet = False
        elif xrp_newprice > xrp_prevprice and xrp_wallet == True:
            time.sleep(5)
            xrp_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
            if xrp_newprice > xrp_prevprice : 
                xrp_prevprice = xrp_newprice
        elif xrp_newprice*1.05 < xrp_prevprice and xrp_wallet == False:
            print("We've been fucked ... but it could have been much worse !\n")
            dollar += dollar* (xrp_newprice/xrp_prevprice-1)*leverage
            xrp_prevprice = xrp_newprice
            print("sell XRP, xrp_price =",xrp_newprice,"wallet =",dollar,'\n')
            xrp_wallet = True
            
        #ada bot
        if ada_newprice > ada_prevprice*1.001 and ada_wallet == False:
            dollar += dollar * (ada_newprice/ada_prevprice-1)*leverage
            ada_prevprice = ada_newprice
            print("sell ADA, ada_price =",ada_newprice,"wallet =",dollar,'\n')
            ada_wallet = True
        elif ada_newprice*1.001 < ada_prevprice and ada_wallet == True:
            if ada_crisis == False:
                t1 = time.time()
                ada_wallet = "unactivated"
                ada_crisis = True
                ada_crisis_counter = False
                print("lowering the price of the ada for",60,'sec')
            if ada_crisis == True and time.time()-t1>60:
                ada_crisis = False
                ada_crisis_counter = True
                ada_wallet = False
                ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
            if ada_newprice*1.003 < ada_prevprice:
                if ada_crisis == False:
                    t1 = time.time()
                    ada_wallet = "unactivated"
                    ada_crisis = True
                    ada_crisis_counter = False
                    print("lowering the price of the ada for",120,'sec')
                if ada_crisis == True and time.time()-t1>120:
                    ada_crisis = False
                    ada_crisis_counter = True
                    ada_wallet = False
                    ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
                if ada_newprice*1.01< ada_newprice:
                    if ada_crisis == False:
                        t1 = time.time()
                        ada_wallet = "unactivated"
                        ada_crisis = True
                        ada_crisis_counter = False
                        print("lowering the price of the ada for",120,'sec')
                    if ada_crisis == True and time.time()-t1>120:
                        ada_crisis = False
                        ada_crisis_counter = True
                        ada_wallet = False
                        ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
            if ada_crisis_counter == True :
                ada_prevprice = ada_newprice
                print("buy ada, ada_price =",ada_newprice,'\n')
                ada_wallet = False
        elif ada_newprice > ada_prevprice and ada_wallet == True:
            time.sleep(5)
            ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
            if ada_newprice > ada_prevprice : 
                ada_prevprice = ada_newprice
        elif ada_newprice*1.05 < ada_prevprice and ada_wallet == False:
            print("We've been fucked ... but it could have been much worse !\n")
            dollar += dollar * (ada_newprice/ada_prevprice-1)*leverage
            ada_prevprice = ada_newprice
            print("sell ADA, ada_price =",ada_newprice,"wallet =",dollar,'\n')
            ada_wallet = True
            
        # bnb bot
        if bnb_newprice > bnb_prevprice*1.001 and bnb_wallet == False:
            dollar += dollar * (bnb_newprice/bnb_prevprice-1)*leverage
            bnb_prevprice = bnb_newprice
            print("sell BNB, bnb_price =",bnb_newprice,"wallet =",dollar,'\n')
            bnb_wallet = True
        elif bnb_newprice*1.001 < bnb_prevprice and bnb_wallet == True:
            if bnb_crisis == False:
                t1 = time.time()
                bnb_wallet = "unactivated"
                bnb_crisis = True
                bnb_crisis_counter = False
                print("lowering the price of the bnb for",60,'sec')
            if bnb_crisis == True and time.time()-1>60:
                bnb_crisis = False
                bnb_crisis_counter = True
                bnb_wallet = False
                bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
            if bnb_newprice*1.003 < bnb_prevprice:
                if bnb_crisis == False:
                    t1 = time.time()
                    bnb_wallet = "unactivated"
                    bnb_crisis = True
                    bnb_crisis_counter = False
                    print("lowering the price of the bnb for",120,'sec')
                if bnb_crisis == True and time.time()-t1>120:
                    bnb_crisis = False
                    bnb_crisis_counter = True
                    bnb_wallet = False
                    bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
                if bnb_newprice*1.01< bnb_newprice:
                    if bnb_crisis == False:
                        t1 = time.time()
                        bnb_wallet = "unactivated"
                        bnb_crisis = True
                        bnb_crisis_counter = False
                        print("lowering the price of the bnb for",120,'sec')
                    if bnb_crisis == True and time.time()-t1>120:
                        bnb_crisis = False
                        bnb_crisis_counter = True
                        bnb_wallet = False
                        bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
            if bnb_crisis_counter == True :
                bnb_prevprice = bnb_newprice
                print("buy bnb, bnb_price =",bnb_newprice,'\n')
                bnb_wallet = False
        elif bnb_newprice > bnb_prevprice and bnb_wallet == True:
            time.sleep(5)
            bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
            if bnb_newprice > bnb_prevprice : 
                bnb_prevprice = bnb_newprice
        elif bnb_newprice*1.05 < bnb_prevprice and bnb_wallet == False:
            print("We've been fucked ... but it could have been much worse !\n")
            dollar += dollar * (bnb_newprice/bnb_prevprice-1)*leverage
            bnb_prevprice = bnb_newprice
            print("sell BNB, bnb_price =",bnb_newprice,"wallet =",dollar,'\n')
            bnb_wallet = True
        
    except KeyboardInterrupt:
        
        if btc_wallet==False:
            dollar += dollar * (btc_newprice/btc_prevprice-1)*leverage
            btc_prevprice = btc_newprice
            print("sell BTC, btc_price =",btc_newprice,"wallet =",dollar,'\n')    
            btc_wallet = True
        
        if eth_wallet==False:
            dollar += dollar * (eth_newprice/eth_prevprice-1)*leverage
            eth_prevprice = eth_newprice
            print("sell ETH, eth_price =",eth_newprice,"wallet =",dollar,'\n')    
            eth_wallet = True
        
        if xrp_wallet==False:
            dollar += dollar * (xrp_newprice/xrp_prevprice-1)*leverage
            xrp_prevprice = xrp_newprice
            print("sell XRP, xrp_price =",xrp_newprice,"wallet =",dollar,'\n')
            xrp_wallet = True
            
        if ada_wallet==False:
            dollar += dollar * (ada_newprice/ada_prevprice-1)*leverage
            ada_prevprice = ada_newprice
            print("sell ADA, ada_price =",ada_newprice,"wallet =",dollar,'\n')
            
        if bnb_wallet==False:
            dollar += dollar * (bnb_newprice/bnb_prevprice-1)*leverage
            bnb_prevprice = bnb_newprice
            print("sell BNB, bnb_price =",bnb_newprice,"wallet =",dollar,'\n')
            bnb_wallet = True
        
        tf = time.time()
        print("it took",tf-t0,"to raise",((dollar/100)-1)*100,"%")
        break