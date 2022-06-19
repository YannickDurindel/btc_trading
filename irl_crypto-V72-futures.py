#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 18:30:16 2022

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
btc_buysell = round((wallet/2)*leverage/btc_newprice,3)

while True :
    try :
        btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])

        # btc bot
        if btc_newprice > btc_prevprice*1.002 and btc_wallet == False:
            wallet = getwallet("USDT")
            binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
            btc_prevprice = btc_newprice
            btc_wallet = True
            print("sell btc, btc_price =",btc_newprice,"wallet =",getwallet("USDT"),'\n')
            with open('performances.csv', 'a', newline='') as P:  
                Perf = writer(P)
                Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice])  
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
                binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='BUY',quantity=btc_buysell)
                btc_prevprice = btc_newprice
                print("buy btc, btc_price =",btc_newprice,'\n')
                btc_wallet = False
                crisis_counter = 0
                with open('performances.csv', 'a', newline='') as P:  
                    Perf = writer(P)
                    Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice])  
                    P.close()
        elif btc_newprice > btc_prevprice and btc_wallet == True:
            time.sleep(5)
            btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
            if btc_newprice > btc_prevprice : 
                btc_prevprice = btc_newprice
        elif btc_newprice*1.05 < btc_prevprice and btc_wallet == False:
            print("We've been fucked ... but it could have been much worse !\n")
            wallet = getwallet("USDT")
            binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
            btc_prevprice = btc_newprice
            print("sell btc, btc_price =",btc_newprice,"wallet =",getwallet("USDT"),'\n')    
            btc_wallet = True
            with open('performances.csv', 'a', newline='') as P:  
                Perf = writer(P)
                Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice])  
                P.close()
            btc_buysell = round(100*leverage/btc_prevprice,3)
            
    except Exception as e:
        print("Error:", e,'\n')
        time.sleep(5)
        pass
        
    except KeyboardInterrupt:
        loss = wallet * (btc_newprice/btc_prevprice-1)*leverage
        print ("if you quit, you'll loose",loss,"$ equals to a malus of",(wallet+loss)/wallet-1)
        print("do you want to quit now ?")
        wait = input("y/n ?")
    
        if wait == "y":
            if btc_wallet==False:
                wallet = getwallet("USDT")
                binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
                btc_prevprice = btc_newprice
                print("sell btc, btc_price =",btc_newprice,"wallet =",getwallet("USDT"),'\n')    
                btc_wallet = True
                with open('performances.csv', 'a', newline='') as P:  
                    Perf = writer(P)
                    Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice])  
                    P.close()
        else :
            print("You made the good choice, but you'll have to wait a bit")
            while btc_wallet == False :
                try :
                    btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
                    
                    if btc_newprice > btc_prevprice*1.00001 and btc_wallet == False:
                        wallet = getwallet("USDT")
                        binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
                        btc_prevprice = btc_newprice
                        print("sell btc, btc_price =",btc_newprice,"wallet =",getwallet("USDT"),'\n')    
                        btc_wallet = True
                        with open('performances.csv', 'a', newline='') as P:  
                            Perf = writer(P)
                            Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice])  
                            P.close()
                    
                except Exception as e:
                    print("Error:", e,'\n')
                    time.sleep(5)
                    pass
                
                except KeyboardInterrupt :
                    if btc_wallet==False:
                        wallet = getwallet("USDT")
                        binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
                        btc_prevprice = btc_newprice
                        print("sell btc, btc_price =",btc_newprice,"wallet =",getwallet("USDT"),'\n')    
                        btc_wallet = True
                        with open('performances.csv', 'a', newline='') as P:  
                            Perf = writer(P)
                            Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice])  
                            P.close()
                            
        
        tf = time.time()
        print("it took",tf-t0,"to raise",getwallet("USDT")-530,"%")
        with open('performances.csv', 'a', newline='') as P:  
            Perf = writer(P)
            Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice])  
            P.close()
        break