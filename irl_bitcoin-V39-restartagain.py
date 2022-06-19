#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 23:29:18 2022

@author: yannick
"""

from binance.client import Client
import time
from csv import writer
import csv

api_key = "M9FsR6XdaZKkIhHmKeCsGSdjYzVWIWGlnsMxM1n6NnTViEaOoKXsPb0ItO4usCuD"
api_secret = "3syXcf4fZ1Q0h51HNxYN8msjOe5RXzmyMm11KZvCnTCf3XGjK2nn4M0dK51qFu5i"
client = Client(api_key, api_secret)
btc_newprice = float(client.get_symbol_ticker(symbol="BTCUSDT")['price'])
wallet = float(client.get_asset_balance(asset='USDT')['free'])
portfolio = float(client.get_asset_balance(asset='BTC')['free'])
balance_init = float(client.get_asset_balance(asset='USDT')['free']) + float(client.get_asset_balance(asset='BTC')['free'])*float(client.get_symbol_ticker(symbol="BTCUSDT")['price']) + float(client.get_asset_balance(asset='BNB')['free'])*float(client.get_symbol_ticker(symbol="BNBUSDT")['price'])
highlimit = 1.002
lowlimit = 1.002
with open('performances.csv', 'r') as P:
  perf = csv.reader(P)
  Perf = list(perf)
  n = int(Perf[len(Perf)-1][0])
  t_init = float(Perf[len(Perf)-1][1])
  t0 = t_init
  btc_prevprice = float(Perf[len(Perf)-1][4])
  fees = float(Perf[len(Perf)-1][5])
  groth = float(Perf[len(Perf)-1][7])
  P.close()
  

while True :
    try :
        btc_newprice = float(client.get_symbol_ticker(symbol="BTCUSDT")['price'])
        wallet = float(client.get_asset_balance(asset='USDT')['free'])
        portfolio = float(client.get_asset_balance(asset='BTC')['free'])
    
        if btc_newprice*lowlimit < btc_prevprice and wallet > portfolio*btc_newprice :
            print('buy, wallet =',wallet,'\n')
            client.create_order(symbol="BTCUSDT",side='buy',type='MARKET',quantity=round((wallet/btc_newprice)-0.00001,5))
            btc_prevprice = btc_newprice
            balance = float(client.get_asset_balance(asset='USDT')['free']) + float(client.get_asset_balance(asset='BTC')['free'])*float(client.get_symbol_ticker(symbol="BTCUSDT")['price']) + float(client.get_asset_balance(asset='BNB')['free'])*float(client.get_symbol_ticker(symbol="BNBUSDT")['price'])
            fees += 0.075
            t0 = time.time()
            with open('performances.csv', 'a', newline='') as P:  
                Perf = writer(P)
                Perf.writerow([n , time.time()-t_init , wallet , portfolio , btc_newprice , fees , balance , groth])  
                P.close()
        
        elif btc_newprice > btc_prevprice*highlimit and wallet < portfolio*btc_newprice :
            fees += 0.075
            print('sell, interest =',(balance*100/balance_init)-100,' total fees =',fees,' final gain = ',((wallet+portfolio*btc_newprice)*100/balance_init)-100-fees,'\n')
            client.create_order(symbol="BTCUSDT",side='sell',type='MARKET',quantity=round(portfolio-0.00001,5))
            btc_prevprice = btc_newprice
            balance = float(client.get_asset_balance(asset='USDT')['free']) + float(client.get_asset_balance(asset='BTC')['free'])*float(client.get_symbol_ticker(symbol="BTCUSDT")['price']) + float(client.get_asset_balance(asset='BNB')['free'])*float(client.get_symbol_ticker(symbol="BNBUSDT")['price'])
            with open('performances.csv', 'a', newline='') as P:  
                Perf = writer(P)
                Perf.writerow([n , time.time()-t_init , wallet , portfolio , btc_newprice , fees , balance , groth])  
                P.close()
                
        if wallet > portfolio*btc_newprice and btc_newprice > btc_prevprice+150 :
            btc_prevprice = btc_newprice
            groth += 150
        
            if groth >= 4050 :
                print('waiting for thr btc price to lower, gonna take a while. Watch the curve !')
                while btc_newprice > btc_prevprice - groth :
                    btc_newprice = float(client.get_symbol_ticker(symbol="BTCUSDT")['price'])
                    time.sleep(30)
                groth = 0
                print('buy, wallet =',wallet,'\n')
                client.create_order(symbol="BTCUSDT",side='buy',type='MARKET',quantity=round((wallet/btc_newprice)-0.00001,5))
                btc_prevprice = btc_newprice
                balance = float(client.get_asset_balance(asset='USDT')['free']) + float(client.get_asset_balance(asset='BTC')['free']) + float(client.get_asset_balance(asset='BNB')['free'])
                fees += 0.075
                t0 = time.time()
                with open('performances.csv', 'a', newline='') as P:  
                    Perf = writer(P)
                    Perf.writerow([n , time.time()-t_init , wallet , portfolio , btc_newprice , fees , balance , groth])  
                    P.close()
        
        n += 1
        time.sleep(0.5)
    
    except KeyboardInterrupt :
        break