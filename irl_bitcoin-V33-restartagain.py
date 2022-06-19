#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 12:12:55 2022

@author: yannick
"""

from binance.client import Client
import time

api_key = "M9FsR6XdaZKkIhHmKeCsGSdjYzVWIWGlnsMxM1n6NnTViEaOoKXsPb0ItO4usCuD"
api_secret = "3syXcf4fZ1Q0h51HNxYN8msjOe5RXzmyMm11KZvCnTCf3XGjK2nn4M0dK51qFu5i"
client = Client(api_key, api_secret)
btc_newprice = float(client.get_symbol_ticker(symbol="BTCUSDT")['price'])
btc_prevprice = btc_newprice
wallet = float(client.get_asset_balance(asset='USDT')['free'])
walletinit = wallet
portfolio = float(client.get_asset_balance(asset='BTC')['free'])
fees = 0
hellcase_loss = 0
highlimit = 1.0015
lowlimit = 1.001
highlimit_init = highlimit
timer = 0
t0 = time.time()

while wallet <= 30 :
    btc_newprice = float(client.get_symbol_ticker(symbol="BTCUSDT")['price'])
    wallet = float(client.get_asset_balance(asset='USDT')['free'])
    portfolio = float(client.get_asset_balance(asset='BTC')['free'])
    
    if btc_newprice*highlimit < btc_prevprice and wallet > portfolio*btc_newprice :
        print('buy, wallet =',wallet,'\n')
        client.create_order(symbol="BTCUSDT",side='buy',type='MARKET',quantity=round(wallet*0.985/btc_newprice,5))
        btc_prevprice = btc_newprice
        fees += 0.075
        highlimit = highlimit_init
        timer = 0
        t0 = time.time()
        
    elif btc_newprice > btc_prevprice*lowlimit and wallet < portfolio*btc_newprice :
        fees += 0.075
        print('sell, interest =',(wallet*100/walletinit)-100,' total fees =',fees,' final gain = ',(wallet*100/walletinit)-100-fees,'\n')
        client.create_order(symbol="BTCUSDT",side='sell',type='MARKET',quantity=round(portfolio*0.99,5))
        btc_prevprice = btc_newprice
        
    elif wallet > portfolio*btc_newprice and btc_newprice > btc_prevprice :
        btc_prevprice = btc_newprice
        #print("sold but the bitcoin price rised, edit the metric !")
        
    if wallet < portfolio*btc_newprice :
        timer += time.time() - t0
    
    if timer > 120 :
        highlimit = 1.00075
        
    time.sleep(0.5)