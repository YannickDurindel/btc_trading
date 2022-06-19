#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 16:17:01 2022

@author: yannick
"""

from binance.client import Client
import time

api_key = "GjwGiZnhWcMUQyxJqNzHU5WiZkicRF00iLMZONYrvSWmwlk4DRnSBm98tnSE3xzF"
api_secret = "teJ7r78Xn3kNKFV80YZNpdyIo1shEVmu6Yaeb8EGktH7ZTVoBjk4eWgRELGgtpvm"
binance_client = Client(api_key, api_secret)

eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
eth_prevprice = eth_newprice
eth_wallet = True

xrp_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
xrp_prevprice = xrp_newprice
xrp_wallet = True

ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
ada_prevprice = ada_newprice
ada_wallet = True

bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
bnb_prevprice = bnb_newprice
bnb_wallet = True

leverage = 20
dollar = 100 + 744.3389638734106 
t0 = time.time() - 29906.933003425598


while True :
    try :
        eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
        xrp_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
        ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
        bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
        
        # eth bot
        if eth_newprice > eth_prevprice*1.001 and eth_wallet == False:
            dollar += dollar * (eth_newprice/eth_prevprice-1)*20
            eth_prevprice = eth_newprice
            print("sell ETH, eth_price =",eth_newprice,"wallet =",dollar,'\n')
            eth_wallet = True
        elif eth_newprice*1.001 < eth_prevprice and eth_wallet == True:
            time.sleep(30)
            eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
            if eth_newprice*1.003 < eth_prevprice:
                print("lowering the standards of ETH ... please wait - lvl1 \n")
                time.sleep(120)
                eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
                if eth_newprice*1.01< eth_newprice:
                    print("lvl2")
                    time.sleep(120)
                    eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
                    eth_prevprice = eth_newprice
            eth_prevprice = eth_newprice
            print("buy ETH, eth_price =",eth_newprice,'\n')
            eth_wallet = False
        elif eth_newprice > eth_prevprice and eth_wallet == True:
            time.sleep(5)
            eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
            if eth_newprice > eth_prevprice : 
                eth_prevprice = eth_newprice
        
        #xrp bot
        if xrp_newprice > xrp_prevprice*1.001 and xrp_wallet == False:
            dollar += dollar * (xrp_newprice/xrp_prevprice-1)*leverage
            xrp_prevprice = xrp_newprice
            print("sell XRP, xrp_price =",xrp_newprice,"wallet =",dollar,'\n')
            xrp_wallet = True
        elif xrp_newprice*1.001 < xrp_prevprice and xrp_wallet == True:
            time.sleep(30)
            xrp_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
            if xrp_newprice*1.003 < xrp_prevprice:
                print("lowering the standards of XRP ... please wait - lvl1\n")
                time.sleep(120)
                xrp_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
                if xrp_newprice*1.01< xrp_newprice:
                    print("lvl2")
                    time.sleep(120)
                    xrp_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
                    xrp_prevprice = xrp_newprice
            xrp_prevprice = xrp_newprice
            print("buy XRP, xrp_price =",xrp_newprice,'\n')
            xrp_wallet = False
        elif xrp_newprice > xrp_prevprice and xrp_wallet == True:
            time.sleep(5)
            xrp_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
            if xrp_newprice > xrp_prevprice : 
                xrp_prevprice = xrp_newprice
            
        #ada bot
        if ada_newprice > ada_prevprice*1.001 and ada_wallet == False:
            dollar += dollar * (ada_newprice/ada_prevprice-1)*leverage
            ada_prevprice = ada_newprice
            print("sell ADA, ada_price =",ada_newprice,"wallet =",dollar,'\n')
            ada_wallet = True
        elif ada_newprice*1.001 < ada_prevprice and ada_wallet == True:
            time.sleep(30)
            ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
            if ada_newprice*1.003 < ada_prevprice:
                print("lowering the standards of ADA ... please wait - lvl1\n")
                time.sleep(120)
                ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
                if ada_newprice*1.01< ada_newprice:
                    print("lvl2")
                    time.sleep(120)
                    ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
                    ada_prevprice = ada_newprice
            ada_prevprice = ada_newprice
            print("buy ADA, ada_price =",ada_newprice,'\n')
            ada_wallet = False
        elif ada_newprice > ada_prevprice and ada_wallet == True:
            time.sleep(5)
            ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
            if ada_newprice > ada_prevprice : 
                ada_prevprice = ada_newprice
            
        # bnb bot
        if bnb_newprice > bnb_prevprice*1.001 and bnb_wallet == False:
            dollar += dollar * (bnb_newprice/bnb_prevprice-1)*leverage
            bnb_prevprice = bnb_newprice
            print("sell BNB, bnb_price =",bnb_newprice,"wallet =",dollar,'\n')
            bnb_wallet = True
        elif bnb_newprice*1.001 < bnb_prevprice and bnb_wallet == True:
            time.sleep(30)
            bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
            if bnb_newprice*1.003 < bnb_prevprice:
                print("lowering the standards of BNB ... please wait - lvl1\n")
                time.sleep(120)
                bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
                if bnb_newprice*1.01< bnb_newprice:
                    print("lvl2")
                    time.sleep(120)
                    bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
                    bnb_prevprice = bnb_newprice
            bnb_prevprice = bnb_newprice
            print("buy BNB, bnb_price =",bnb_newprice,'\n')
            bnb_wallet = False
        elif bnb_newprice > bnb_prevprice and bnb_wallet == True:
            time.sleep(5)
            bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
            if bnb_newprice > bnb_prevprice : 
                bnb_prevprice = bnb_newprice
        
    except KeyboardInterrupt:
        
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
        print("it took",tf-t0,"to raise",(dollar/100)-1,"%")
        break