#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 21:58:21 2022

@author: yannick
"""

from binance.client import Client
import time
from csv import writer
import csv

api_key = "wsWyaiQ0dlAWj4eFE4AdvbOtmtnj2sKTMv3f53CRy6NsGIBdTZy3ZxUggAMOZr1f"
api_secret = "AlBOMFfj60b6xjWldKv6Vex5l4y4REqrU2e17XIbeRmAJVZ4Jakh7CdgSu5U5mid"
binance_client = Client(api_key, api_secret)
leverage = 20
t_init = time.time()
with open('performances.csv', 'r') as P:
  perf = csv.reader(P)
  Perf = list(perf)
  wallet = float(Perf[len(Perf)-1][1])
  t0 = float(Perf[len(Perf)-1][0])
  P.close()
  
def getwallet(currency):
    account_info = binance_client.futures_account()
    av_balance = None
    for asset in account_info["assets"]:
        if asset["asset"] == currency:
            av_balance = float(asset["marginBalance"])
    return av_balance
wallet = getwallet("USDT")

btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
btc_prevprice = btc_newprice
btc_wallet = True
btc_crisis = False
crisis_counter_btc = 0
binance_client.futures_change_leverage(symbol='BTCUSDT', leverage=leverage)
btc_buysell = round((wallet/10)*leverage/btc_newprice,3)

eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
eth_prevprice = eth_newprice
eth_wallet = True
eth_crisis = False
crisis_counter_eth = 0
binance_client.futures_change_leverage(symbol='ETHUSDT', leverage=leverage)
eth_buysell = round((wallet/10)*leverage/eth_newprice,3)

xrp_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
xrp_prevprice = xrp_newprice
xrp_wallet = True
xrp_crisis = False
crisis_counter_xrp = 0
binance_client.futures_change_leverage(symbol='XRPUSDT', leverage=leverage)
xrp_buysell = round((wallet/10)*leverage/xrp_newprice,1)

ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
ada_prevprice = ada_newprice
ada_wallet = True
ada_crisis = False
crisis_counter_ada = 0
binance_client.futures_change_leverage(symbol='ADAUSDT', leverage=leverage)
ada_buysell = round((wallet/10)*leverage/ada_newprice,0)

bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
bnb_prevprice = bnb_newprice
bnb_wallet = True
bnb_crisis = False
crisis_counter_bnb = 0
binance_client.futures_change_leverage(symbol='BNBUSDT', leverage=leverage)
bnb_buysell = round((wallet/10)*leverage/bnb_newprice,2)


while True :
    try :
        btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
        eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
        xrp_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
        ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
        bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
        
        # btc bot
        if btc_newprice > btc_prevprice*1.002 and btc_wallet == False:
            wallet = getwallet("USDT")
            #binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
            btc_prevprice = btc_newprice
            btc_wallet = True
            print("sell btc, btc_price =",btc_newprice,"wallet =",getwallet("USDT"),'\n')
            with open('performances.csv', 'a', newline='') as P:  
                Perf = writer(P)
                Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                P.close()
            btc_buysell = btc_buysell
        elif (btc_newprice*1.0015 < btc_prevprice and btc_wallet == True) or (btc_wallet == "unactivated" and btc_newprice*1.0015 < btc_prevprice):
            if btc_crisis == False:
                t1 = time.time()
                btc_wallet = "unactivated"
                btc_crisis = True
                crisis_counter = 1
                print("lowering the price of the btc for",60,'sec\n')
            if btc_crisis == True and time.time()-t1>60:
                btc_crisis = False
                btc_wallet = False
                btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
            if btc_newprice*1.003 < btc_prevprice or (btc_wallet == "unactivated" and crisis_counter == 2):
                if btc_crisis == False:
                    t1 = time.time()
                    btc_wallet = "unactivated"
                    btc_crisis = True
                    crisis_counter = 2
                    print("lowering the price of the btc for",120,'sec\n')
                if btc_crisis == True and time.time()-t1>120:
                    btc_crisis = False
                    btc_wallet = False
                    btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
                if btc_newprice*1.01< btc_newprice or (btc_wallet == "unactivated" and crisis_counter == 3):
                    if btc_crisis == False:
                        t1 = time.time()
                        btc_wallet = "unactivated"
                        btc_crisis = True
                        crisis_counter = 3
                        print("lowering the price of the btc for",120,'sec\n')
                    if btc_crisis == True and time.time()-t1>120:
                        btc_crisis = False
                        btc_wallet = True
                        btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
            if btc_crisis == False :
                wallet = getwallet("USDT")
                #binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='BUY',quantity=btc_buysell)
                btc_prevprice = btc_newprice
                print("buy btc, btc_price =",btc_newprice,'\n')
                btc_wallet = False
                crisis_counter = 0
                with open('performances.csv', 'a', newline='') as P:  
                    Perf = writer(P)
                    Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                    P.close()
        elif btc_newprice > btc_prevprice and btc_wallet == True:
            time.sleep(5)
            btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
            if btc_newprice > btc_prevprice : 
                btc_prevprice = btc_newprice
        elif btc_newprice*1.05 < btc_prevprice and btc_wallet == False:
            print("We've been fucked ... but it could have been much worse !\n")
            wallet = getwallet("USDT")
            #binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
            btc_prevprice = btc_newprice
            print("sell btc, btc_price =",btc_newprice,"wallet =",getwallet("USDT"),'\n')    
            btc_wallet = True
            with open('performances.csv', 'a', newline='') as P:  
                Perf = writer(P)
                Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                P.close()
            btc_buysell = round(100*leverage/btc_prevprice,3)
        
        # eth bot
        if eth_newprice > eth_prevprice*1.002 and eth_wallet == False:
            wallet = getwallet("USDT")
            #binance_client.futures_create_order(symbol='ETHUSDT',type='MARKET',side='SELL',quantity=eth_buysell)
            eth_prevprice = eth_newprice
            eth_wallet = True
            print("sell eth, btc_price =",eth_newprice,"wallet =",getwallet("USDT"),'\n')
            with open('performances.csv', 'a', newline='') as P:  
                Perf = writer(P)
                Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                P.close()
            btc_buysell = round((wallet/10)*leverage/btc_newprice,3)
        elif (eth_newprice*1.0015 < eth_prevprice and eth_wallet == True) or (eth_wallet == "unactivated" and eth_newprice*1.0015 < eth_prevprice):
            if eth_crisis == False:
                t1 = time.time()
                eth_wallet = "unactivated"
                eth_crisis = True
                crisis_counter = 1
                print("lowering the price of the eth for",60,'sec\n')
            if eth_crisis == True and time.time()-t1>60:
                eth_crisis = False
                eth_wallet = False
                eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
            if eth_newprice*1.003 < eth_prevprice or (eth_wallet == "unactivated" and crisis_counter == 2):
                if eth_crisis == False:
                    t1 = time.time()
                    eth_wallet = "unactivated"
                    eth_crisis = True
                    crisis_counter = 2
                    print("lowering the price of the eth for",120,'sec\n')
                if eth_crisis == True and time.time()-t1>120:
                    eth_crisis = False
                    eth_wallet = False
                    eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
                if eth_newprice*1.01< eth_newprice or (eth_wallet == "unactivated" and crisis_counter == 3):
                    if eth_crisis == False:
                        t1 = time.time()
                        eth_wallet = "unactivated"
                        eth_crisis = True
                        crisis_counter = 3
                        print("lowering the price of the eth for",120,'sec\n')
                    if eth_crisis == True and time.time()-t1>120:
                        eth_crisis = False
                        eth_wallet = True
                        eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
            if eth_crisis == False :
                wallet = getwallet("USDT")
                #binance_client.futures_create_order(symbol='ETHUSDT',type='MARKET',side='BUY',quantity=eth_buysell)
                eth_prevprice = eth_newprice
                print("buy eth, eth_price =",eth_newprice,'\n')
                eth_wallet = False
                crisis_counter = 0
                with open('performances.csv', 'a', newline='') as P:  
                    Perf = writer(P)
                    Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                    P.close()
        elif eth_wallet == "unactivated" and eth_newprice > eth_prevprice:
            eth_newprice = eth_prevprice
        elif eth_newprice > eth_prevprice and eth_wallet == True:
            time.sleep(5)
            eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
            if eth_newprice > eth_prevprice : 
                eth_prevprice = eth_newprice
        elif eth_newprice*1.05 < eth_prevprice and eth_wallet == False:
            print("We've been fucked ... but it could have been much worse !\n")
            wallet = getwallet("USDT")
            #binance_client.futures_create_order(symbol='ETHUSDT',type='MARKET',side='SELL',quantity=eth_buysell)
            eth_prevprice = eth_newprice
            print("sell eth, btc_price =",eth_newprice,"wallet =",getwallet("USDT"),'\n')    
            eth_wallet = True
            with open('performances.csv', 'a', newline='') as P:  
                Perf = writer(P)
                Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                P.close()
            btc_buysell = round((wallet/10)*leverage/btc_newprice,3)
        
        # xrp bot
        if xrp_newprice > xrp_prevprice*1.002 and xrp_wallet == False:
            wallet = getwallet("USDT")
            #binance_client.futures_create_order(symbol='XRPUSDT',type='MARKET',side='SELL',quantity=xrp_buysell)
            xrp_prevprice = xrp_newprice
            xrp_wallet = True
            print("sell xrp, xrp_price =",xrp_newprice,"wallet =",getwallet("USDT"),'\n')
            with open('performances.csv', 'a', newline='') as P:  
                Perf = writer(P)
                Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                P.close()
            xrp_buysell = round((wallet/10)*leverage/xrp_newprice,1)
        elif (xrp_newprice*1.0015 < xrp_prevprice and xrp_wallet == True) or (xrp_wallet == "unactivated" and xrp_newprice*1.0015 < xrp_prevprice):
            if xrp_crisis == False:
                t1 = time.time()
                xrp_wallet = "unactivated"
                xrp_crisis = True
                crisis_counter = 1
                print("lowering the price of the xrp for",60,'sec\n')
            if xrp_crisis == True and time.time()-t1>60:
                xrp_crisis = False
                xrp_wallet = False
                xrp_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
            if xrp_newprice*1.003 < xrp_prevprice or (xrp_wallet == "unactivated" and crisis_counter == 2):
                if xrp_crisis == False:
                    t1 = time.time()
                    xrp_wallet = "unactivated"
                    xrp_crisis = True
                    crisis_counter = 2
                    print("lowering the price of the xrp for",120,'sec\n')
                if xrp_crisis == True and time.time()-t1>120:
                    xrp_crisis = False
                    xrp_wallet = False
                    xrp_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
                if xrp_newprice*1.01< xrp_newprice or (xrp_wallet == "unactivated" and crisis_counter == 3):
                    if xrp_crisis == False:
                        t1 = time.time()
                        xrp_wallet = "unactivated"
                        xrp_crisis = True
                        crisis_counter = 3
                        print("lowering the price of the xrp for",120,'sec\n')
                    if xrp_crisis == True and time.time()-t1>120:
                        xrp_crisis = False
                        xrp_wallet = True
                        xrp_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
            if xrp_crisis == False :
                wallet = getwallet("USDT")
                #binance_client.futures_create_order(symbol='XRPUSDT',type='MARKET',side='BUY',quantity=xrp_buysell)
                xrp_prevprice = xrp_newprice
                print("buy xrp, xrp_price =",xrp_newprice,'\n')
                xrp_wallet = False
                crisis_counter = 0
                with open('performances.csv', 'a', newline='') as P:  
                    Perf = writer(P)
                    Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                    P.close()
        elif xrp_wallet == "unactivated" and xrp_newprice > xrp_prevprice:
            xrp_newprice = xrp_prevprice
        elif xrp_newprice > xrp_prevprice and xrp_wallet == True:
            time.sleep(5)
            xrp_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
            if xrp_newprice > xrp_prevprice : 
                xrp_prevprice = xrp_newprice
        elif xrp_newprice*1.05 < xrp_prevprice and xrp_wallet == False:
            print("We've been fucked ... but it could have been much worse !\n")
            wallet = getwallet("USDT")
            #binance_client.futures_create_order(symbol='XRPUSDT',type='MARKET',side='SELL',quantity=xrp_buysell)
            xrp_prevprice = xrp_newprice
            print("sell xrp, xrp_price =",xrp_newprice,"wallet =",getwallet("USDT"),'\n')    
            xrp_wallet = True
            with open('performances.csv', 'a', newline='') as P:  
                Perf = writer(P)
                Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                P.close()
            xrp_buysell = round((wallet/10)*leverage/xrp_newprice,1)
            
        # ada bot
        if ada_newprice > ada_prevprice*1.002 and ada_wallet == False:
            wallet = getwallet("USDT")
            #binance_client.futures_create_order(symbol='ADAUSDT',type='MARKET',side='SELL',quantity=ada_buysell)
            ada_prevprice = ada_newprice
            ada_wallet = True
            print("sell ada, ada_price =",ada_newprice,"wallet =",getwallet("USDT"),'\n')
            with open('performances.csv', 'a', newline='') as P:  
                Perf = writer(P)
                Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                P.close()
            ada_buysell = round((wallet/10)*leverage/ada_newprice,0)
        elif (ada_newprice*1.0015 < ada_prevprice and ada_wallet == True) or (ada_wallet == "unactivated" and ada_newprice*1.0015 < ada_prevprice):
            if ada_crisis == False:
                t1 = time.time()
                ada_wallet = "unactivated"
                ada_crisis = True
                crisis_counter = 1
                print("lowering the price of the ada for",60,'sec\n')
            if ada_crisis == True and time.time()-t1>60:
                ada_crisis = False
                ada_wallet = False
                ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
            if ada_newprice*1.003 < ada_prevprice or (ada_wallet == "unactivated" and crisis_counter == 2):
                if ada_crisis == False:
                    t1 = time.time()
                    ada_wallet = "unactivated"
                    ada_crisis = True
                    crisis_counter = 2
                    print("lowering the price of the ada for",120,'sec\n')
                if ada_crisis == True and time.time()-t1>120:
                    ada_crisis = False
                    ada_wallet = False
                    ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
                if ada_newprice*1.01< ada_newprice or (ada_wallet == "unactivated" and crisis_counter == 3):
                    if ada_crisis == False:
                        t1 = time.time()
                        ada_wallet = "unactivated"
                        ada_crisis = True
                        crisis_counter = 3
                        print("lowering the price of the ada for",120,'sec\n')
                    if ada_crisis == True and time.time()-t1>120:
                        ada_crisis = False
                        ada_wallet = True
                        ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
            if ada_crisis == False :
                wallet = getwallet("USDT")
                #binance_client.futures_create_order(symbol='ADAUSDT',type='MARKET',side='BUY',quantity=ada_buysell)
                ada_prevprice = ada_newprice
                print("buy ada, ada_price =",ada_newprice,'\n')
                ada_wallet = False
                crisis_counter = 0
                with open('performances.csv', 'a', newline='') as P:  
                    Perf = writer(P)
                    Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                    P.close()
        elif ada_wallet == "unactivated" and ada_newprice > ada_prevprice:
            ada_newprice = ada_prevprice
        elif ada_newprice > ada_prevprice and ada_wallet == True:
            time.sleep(5)
            ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
            if ada_newprice > ada_prevprice : 
                ada_prevprice = ada_newprice
        elif ada_newprice*1.05 < ada_prevprice and ada_wallet == False:
            print("We've been fucked ... but it could have been much worse !\n")
            wallet = getwallet("USDT")
            #binance_client.futures_create_order(symbol='ADAUSDT',type='MARKET',side='SELL',quantity=ada_buysell)
            ada_prevprice = ada_newprice
            print("sell ada, ada_price =",ada_newprice,"wallet =",getwallet("USDT"),'\n')    
            ada_wallet = True
            with open('performances.csv', 'a', newline='') as P:  
                Perf = writer(P)
                Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                P.close()
            ada_buysell = round((wallet/10)*leverage/ada_newprice,0)
            
        # bnb bot
        if bnb_newprice > bnb_prevprice*1.002 and bnb_wallet == False:
            wallet = getwallet("USDT")
            #binance_client.futures_create_order(symbol='BNBUSDT',type='MARKET',side='SELL',quantity=bnb_buysell)
            bnb_prevprice = bnb_newprice
            bnb_wallet = True
            print("sell bnb, bnb_price =",bnb_newprice,"wallet =",getwallet("USDT"),'\n')
            with open('performances.csv', 'a', newline='') as P:  
                Perf = writer(P)
                Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                P.close()
            bnb_buysell = round((wallet/10)*leverage/bnb_newprice,2)
        elif (bnb_newprice*1.0015 < bnb_prevprice and bnb_wallet == True) or (bnb_wallet == "unactivated" and bnb_newprice*1.0015 < bnb_prevprice):
            if bnb_crisis == False:
                t1 = time.time()
                bnb_wallet = "unactivated"
                bnb_crisis = True
                crisis_counter = 1
                print("lowering the price of the bnb for",60,'sec\n')
            if bnb_crisis == True and time.time()-t1>60:
                bnb_crisis = False
                bnb_wallet = False
                bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
            if bnb_newprice*1.003 < bnb_prevprice or (bnb_wallet == "unactivated" and crisis_counter == 2):
                if bnb_crisis == False:
                    t1 = time.time()
                    bnb_wallet = "unactivated"
                    bnb_crisis = True
                    crisis_counter = 2
                    print("lowering the price of the bnb for",120,'sec\n')
                if bnb_crisis == True and time.time()-t1>120:
                    bnb_crisis = False
                    bnb_wallet = False
                    bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
                if bnb_newprice*1.01< bnb_newprice or (bnb_wallet == "unactivated" and crisis_counter == 3):
                    if bnb_crisis == False:
                        t1 = time.time()
                        bnb_wallet = "unactivated"
                        bnb_crisis = True
                        crisis_counter = 3
                        print("lowering the price of the bnb for",120,'sec\n')
                    if bnb_crisis == True and time.time()-t1>120:
                        bnb_crisis = False
                        bnb_wallet = True
                        bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
            if bnb_crisis == False :
                wallet = getwallet("USDT")
                #binance_client.futures_create_order(symbol='BNBUSDT',type='MARKET',side='BUY',quantity=bnb_buysell)
                bnb_prevprice = bnb_newprice
                print("buy bnb, bnb_price =",bnb_newprice,'\n')
                bnb_wallet = False
                crisis_counter = 0
                with open('performances.csv', 'a', newline='') as P:  
                    Perf = writer(P)
                    Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                    P.close()
        elif bnb_wallet == "unactivated" and bnb_newprice > bnb_prevprice:
            bnb_newprice = bnb_prevprice
        elif bnb_newprice > bnb_prevprice and bnb_wallet == True:
            time.sleep(5)
            bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
            if bnb_newprice > bnb_prevprice : 
                bnb_prevprice = bnb_newprice
        elif bnb_newprice*1.05 < bnb_prevprice and bnb_wallet == False:
            print("We've been fucked ... but it could have been much worse !\n")
            wallet = getwallet("USDT")
            #binance_client.futures_create_order(symbol='BNBUSDT',type='MARKET',side='SELL',quantity=bnb_buysell)
            bnb_prevprice = bnb_newprice
            print("sell bnb, bnb_price =",bnb_newprice,"wallet =",getwallet("USDT"),'\n')    
            bnb_wallet = True
            with open('performances.csv', 'a', newline='') as P:  
                Perf = writer(P)
                Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                P.close()
            bnb_buysell = round((wallet/10)*leverage/bnb_newprice,2)
        time.sleep(0.5)
        
    except Exception as e:
        print("Error:", e,'\n')
        time.sleep(5)
        pass
        
    except KeyboardInterrupt:
        loss = wallet * (btc_newprice/btc_prevprice-1)*leverage + wallet * (eth_newprice/eth_prevprice-1)*leverage + wallet * (xrp_newprice/xrp_prevprice-1)*leverage + wallet * (ada_newprice/ada_prevprice-1)*leverage + wallet * (bnb_newprice/bnb_prevprice-1)*leverage
        print ("if you quit, you'll loose",loss,"$ equals to a malus of",(wallet+loss)/wallet-1)
        print("do you want to quit now ?")
        wait = input("y/n ?")
        
        if wait == "y":
            if btc_wallet==False:
                wallet = getwallet("USDT")
                #binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
                btc_prevprice = btc_newprice
                print("sell btc, btc_price =",btc_newprice,"wallet =",getwallet("USDT"),'\n')    
                btc_wallet = True
                with open('performances.csv', 'a', newline='') as P:  
                    Perf = writer(P)
                    Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                    P.close()
                
            if eth_wallet==False:
                wallet = getwallet("USDT")
                #binance_client.futures_create_order(symbol='ETHUSDT',type='MARKET',side='SELL',quantity=eth_buysell)
                eth_prevprice = eth_newprice
                print("sell eth, btc_price =",eth_newprice,"wallet =",getwallet("USDT"),'\n')    
                eth_wallet = True
                with open('performances.csv', 'a', newline='') as P:  
                    Perf = writer(P)
                    Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                    P.close()
        
            if xrp_wallet==False:
                wallet = getwallet("USDT")
                #binance_client.futures_create_order(symbol='XRPUSDT',type='MARKET',side='SELL',quantity=xrp_buysell)
                xrp_prevprice = xrp_newprice
                print("sell XRP, xrp_price =",xrp_newprice,"wallet =",getwallet("USDT"),'\n')
                xrp_wallet = True
                with open('performances.csv', 'a', newline='') as P:  
                    Perf = writer(P)
                    Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                    P.close()
            
            if ada_wallet==False:
                wallet = getwallet("USDT")
                #binance_client.futures_create_order(symbol='ADAUSDT',type='MARKET',side='SELL',quantity=ada_buysell)
                ada_prevprice = ada_newprice
                print("sell ADA, ada_price =",ada_newprice,"wallet =",getwallet("USDT"),'\n')
                ada_wallet = True
                with open('performances.csv', 'a', newline='') as P:  
                    Perf = writer(P)
                    Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                    P.close()
                
            if bnb_wallet==False:
                wallet = getwallet("USDT")
                #binance_client.futures_create_order(symbol='BNBUSDT',type='MARKET',side='SELL',quantity=bnb_buysell)
                bnb_prevprice = bnb_newprice
                print("sell BNB, bnb_price =",bnb_newprice,"wallet =",getwallet("USDT"),'\n')
                bnb_wallet = True
                with open('performances.csv', 'a', newline='') as P:  
                    Perf = writer(P)
                    Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                    P.close()
                
        else :
            print("You made the good choice, but you'll have to wait a bit")
            while btc_wallet == False or eth_wallet == False or ada_wallet == False or xrp_wallet == False or bnb_wallet == False :
                try :
                    btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
                    eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
                    xrp_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
                    ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
                    bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
            
                    if btc_newprice > btc_prevprice*1.00001 and btc_wallet == False:
                        wallet = getwallet("USDT")
                        #binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
                        btc_prevprice = btc_newprice
                        print("sell btc, btc_price =",btc_newprice,"wallet =",getwallet("USDT"),'\n')    
                        btc_wallet = True
                        with open('performances.csv', 'a', newline='') as P:  
                            Perf = writer(P)
                            Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                            P.close()
                        
                    if eth_newprice > eth_prevprice*1.00001 and eth_wallet == False:
                        wallet = getwallet("USDT")
                        #binance_client.futures_create_order(symbol='ETHUSDT',type='MARKET',side='SELL',quantity=eth_buysell)
                        eth_prevprice = eth_newprice
                        print("sell eth, btc_price =",eth_newprice,"wallet =",getwallet("USDT"),'\n')    
                        eth_wallet = True
                        with open('performances.csv', 'a', newline='') as P:  
                            Perf = writer(P)
                            Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                            P.close()
                    
                    if xrp_newprice > xrp_prevprice*1.00001 and xrp_wallet == False:
                        wallet = getwallet("USDT")
                        #binance_client.futures_create_order(symbol='XRPUSDT',type='MARKET',side='SELL',quantity=round(100*leverage/xrp_prevprice,1))
                        xrp_prevprice = xrp_newprice
                        print("sell XRP, xrp_price =",xrp_newprice,"wallet =",getwallet("USDT"),'\n')    
                        xrp_wallet = True
                        with open('performances.csv', 'a', newline='') as P:  
                            Perf = writer(P)
                            Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                            P.close()

                    if ada_newprice > ada_prevprice*1.00001 and ada_wallet == False:
                        wallet = getwallet("USDT")
                        #binance_client.futures_create_order(symbol='ADAUSDT',type='MARKET',side='SELL',quantity=ada_buysell)
                        ada_prevprice = ada_newprice
                        print("sell ADA, ada_price =",ada_newprice,"wallet =",getwallet("USDT"),'\n')    
                        ada_wallet = True
                        with open('performances.csv', 'a', newline='') as P:  
                            Perf = writer(P)
                            Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                            P.close()
                    
                    if bnb_newprice > bnb_prevprice*1.00001 and bnb_wallet == False:
                        wallet = getwallet("USDT")
                        #binance_client.futures_create_order(symbol='BNBUSDT',type='MARKET',side='SELL',quantity=bnb_buysell)
                        bnb_prevprice = bnb_newprice
                        print("sell bnb, bnb_price =",bnb_newprice,"wallet =",getwallet("USDT"),'\n')    
                        bnb_wallet = True
                        with open('performances.csv', 'a', newline='') as P:  
                            Perf = writer(P)
                            Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                            P.close()
                            
                except KeyboardInterrupt :
                    if btc_wallet==False:
                        wallet = getwallet("USDT")
                        #binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
                        btc_prevprice = btc_newprice
                        print("sell btc, btc_price =",btc_newprice,"wallet =",getwallet("USDT"),'\n')    
                        btc_wallet = True
                        with open('performances.csv', 'a', newline='') as P:  
                            Perf = writer(P)
                            Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                            P.close()
                
                    if eth_wallet==False:
                        wallet = getwallet("USDT")
                        #binance_client.futures_create_order(symbol='ETHUSDT',type='MARKET',side='SELL',quantity=eth_buysell)
                        eth_prevprice = eth_newprice
                        print("sell eth, btc_price =",eth_newprice,"wallet =",getwallet("USDT"),'\n')    
                        eth_wallet = True
                        with open('performances.csv', 'a', newline='') as P:  
                            Perf = writer(P)
                            Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                            P.close()
        
                    if xrp_wallet==False:
                        wallet = getwallet("USDT")
                        #binance_client.futures_create_order(symbol='XRPUSDT',type='MARKET',side='SELL',quantity=xrp_buysell)
                        xrp_prevprice = xrp_newprice
                        print("sell XRP, xrp_price =",xrp_newprice,"wallet =",getwallet("USDT"),'\n')
                        xrp_wallet = True
                        with open('performances.csv', 'a', newline='') as P:  
                            Perf = writer(P)
                            Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                            P.close()
            
                    if ada_wallet==False:
                        wallet = getwallet("USDT")
                        #binance_client.futures_create_order(symbol='ADAUSDT',type='MARKET',side='SELL',quantity=ada_buysell)
                        ada_prevprice = ada_newprice
                        print("sell ADA, ada_price =",ada_newprice,"wallet =",getwallet("USDT"),'\n')
                        ada_wallet = True
                        with open('performances.csv', 'a', newline='') as P:  
                            Perf = writer(P)
                            Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                            P.close()
                
                    if bnb_wallet==False:
                        wallet = getwallet("USDT")
                        #binance_client.futures_create_order(symbol='BNBUSDT',type='MARKET',side='SELL',quantity=bnb_buysell)
                        bnb_prevprice = bnb_newprice
                        print("sell BNB, bnb_price =",bnb_newprice,"wallet =",getwallet("USDT"),'\n')
                        bnb_wallet = True
                        with open('performances.csv', 'a', newline='') as P:  
                            Perf = writer(P)
                            Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
                            P.close()
                    break
        
        
        tf = time.time()
        print("it took",tf-t0,"to raise",getwallet("USDT")-530,"%")
        with open('performances.csv', 'a', newline='') as P:  
            Perf = writer(P)
            Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice,eth_newprice,xrp_newprice,ada_newprice,bnb_newprice])  
            P.close()
        break
