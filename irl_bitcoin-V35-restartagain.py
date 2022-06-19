#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 07:50:05 2022

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
btc_prevprice = btc_newprice
wallet = float(client.get_asset_balance(asset='USDT')['free'])
walletinit = wallet
portfolio = float(client.get_asset_balance(asset='BTC')['free'])
portfolioinit = portfolio
fees = 0
hellcase_loss = 0
highlimit = 1.0115
lowlimit = 1.0115
with open('performances.csv', 'r') as P:
  perf = csv.reader(P)
  Perf = list(perf)
  n = int(Perf[len(Perf)-1][0])
  t_init = float(Perf[len(Perf)][1])
  t0 = t_init
  P.close()

while True :
    btc_newprice = float(client.get_symbol_ticker(symbol="BTCUSDT")['price'])
    wallet = float(client.get_asset_balance(asset='USDT')['free'])
    portfolio = float(client.get_asset_balance(asset='BTC')['free'])
    
    if btc_newprice*highlimit < btc_prevprice and wallet > portfolio*btc_newprice :
        print('buy, wallet =',wallet,'\n')
        client.create_order(symbol="BTCUSDT",side='buy',type='MARKET',quantity=round((wallet/btc_newprice)-0.00001,5))
        btc_prevprice = btc_newprice
        fees += 0.075
        t0 = time.time()
        with open('performances.csv', 'a', newline='') as P:  
            Perf = writer(P)
            Perf.writerow([n , time.time()-t_init , wallet , portfolio , btc_newprice , fees])  
            P.close()
        
    elif btc_newprice > btc_prevprice*lowlimit and wallet < portfolio*btc_newprice :
        fees += 0.075
        print('sell, interest =',((wallet+portfolio*btc_newprice)*100/(walletinit+portfolioinit*btc_newprice))-100,' total fees =',fees,' final gain = ',((wallet+portfolio*btc_newprice)*100/(walletinit+portfolioinit*btc_newprice))-100-fees,'\n')
        client.create_order(symbol="BTCUSDT",side='sell',type='MARKET',quantity=round(portfolio-0.00001,5))
        btc_prevprice = btc_newprice
        with open('performances.csv', 'a', newline='') as P:  
            Perf = writer(P)
            Perf.writerow([n , time.time()-t_init , wallet , portfolio , btc_newprice , fees])  
            P.close()
        
    n += 1
    time.sleep(0.5)