#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 08:48:09 2022

@author: yannick
"""

# BEWARE !!!  this code doesn't have a hellcase manager !!!

from binance.client import Client
import matplotlib.pyplot as plt
import time


def curve (x,y):
    plt.plot(x, y)
    plt.xlabel('Time  (s)')
    plt.ylabel('bitcoin value (USDT)')
    plt.title('bitcoin curve')
    plt.show()

# init
api_key = "M9FsR6XdaZKkIhHmKeCsGSdjYzVWIWGlnsMxM1n6NnTViEaOoKXsPb0ItO4usCuD"
api_secret = "3syXcf4fZ1Q0h51HNxYN8msjOe5RXzmyMm11KZvCnTCf3XGjK2nn4M0dK51qFu5i"
client = Client(api_key, api_secret)

def getbitcoin():
    btc_price = float(client.get_symbol_ticker(symbol="BTCUSDT")['price'])
    return btc_price
        
def feedback():
    print("bitcoin price (EUR) : ",btc_new)
    print("wallet = ",wallet,'EUR')
    print('interest = ',100*(wallet/walletinit)-100,'%')
    print('\n')
    
t0 = time.time()
x = [0]
y = [getbitcoin()] 
btc_old = getbitcoin()
btc_hist = btc_old
wallet = 40
walletinit = wallet
portfolio = 0
while wallet<=80 :
    try:
        btc_new = getbitcoin()
        x.append(time.time()-t0)
        y.append(btc_new)
        if btc_new > btc_old*1.0004 and wallet == 0:
            wallet = portfolio * btc_new/1.0002
            portfolio = 0
            btc_hist = btc_old
            btc_old = btc_new
            print("sell")
            feedback()
        if btc_new*1.0001 < btc_old and portfolio == 0 :
            interest = 100*(wallet/walletinit)-100
            walletsafe = wallet
            loss = 100*(wallet/walletsafe)-100
            portfolio = wallet / btc_new*1.0002
            wallet = 0
            btc_hist = btc_old
            btc_old = btc_new
            print('buy')
            print("bitcoin price (EUR) : ",btc_new)
            print('\n')    
    except KeyboardInterrupt:
        curve(x,y)
            

print('succed !!!')
feedback()