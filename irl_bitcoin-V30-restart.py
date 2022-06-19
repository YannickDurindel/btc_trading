#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 12:22:05 2022

@author: yannick
"""

# code like the 26 but with the api applied

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
    
def buy(btc_new):
    wallet = float(client.get_asset_balance(asset='USDT')['free'])
    client.create_order(symbol="BTCUSDT",side='buy',type='MARKET',quantity=round(wallet*0.99/btc_new,5))

def sell():
    portfolio = float(client.get_asset_balance(asset='BTC')['free'])
    client.create_order(symbol="BTCUSDT",side='sell',type='MARKET',quantity=round(portfolio,5))
    
t0 = time.time()
x = [0]
y = [getbitcoin()] 
btc_old = getbitcoin()
btc_hist = btc_old
wallet = float(client.get_asset_balance(asset='USDT')['free'])
walletinit = wallet
portfolio = float(client.get_asset_balance(asset='BTC')['free'])
while wallet<=30 :
    try:
        btc_new = getbitcoin()
        x.append(time.time()-t0)
        y.append(btc_new)
        if btc_new > btc_old*1.00012 and wallet < 1:
            sell()
            btc_hist = btc_old
            btc_old = btc_new
            print("sell")
            feedback()
        if btc_new*1.00012 < btc_old and portfolio < 0.0001 :
            interest = 100*(wallet/walletinit)-100
            walletsafe = wallet
            loss = 100*(wallet/walletsafe)-100
            buy(btc_new)
            btc_hist = btc_old
            btc_old = btc_new
            print('buy')
            print("bitcoin price (EUR) : ",btc_new)
            print('\n')
        if btc_new*0.999 < btc_old and btc_old < btc_hist :
            print('the hell case happens !!!','\n')
            print("bitcoin price hist (EUR) : ",btc_hist,'\n')
            compteur = 0
            curve(x,y)
            while btc_new <= btc_hist :
                loss = 100*(wallet/walletsafe)-100
                try:
                    if btc_new != getbitcoin() and compteur <= 100 :
                        btc_new = getbitcoin()
                        print("bitcoin price (EUR) : ",btc_new,'over',btc_hist,'  ;  ',compteur,'/100','\n')
                        compteur += 1
                    elif btc_new != getbitcoin() and compteur > 100 and loss+0.001 < interest :
                        buy(btc_new)
                        interest = 100*(wallet/walletinit)-100
                        loss = 100*(wallet/walletsafe)-100
                        print('buy')
                        print("bitcoin price (EUR) : ",btc_new)
                        print("your previous gain were : ",interest)
                        print('you just lost ',loss,'%')
                        print('you have left ',interest-loss,'\n')
                        btc_new = btc_hist+1
                    elif btc_new != getbitcoin() and compteur > 100 and loss > interest :
                        btc_new = getbitcoin()
                        print("bitcoin price (EUR) : ",btc_new,'over',btc_hist,'interest-loss = ',interest-loss,'\n')
                        compteur += 1
                except KeyboardInterrupt:
                    wallet = portfolio*btc_new/1.0002
                    print("KeyboardInterrrupt !\n")
                    print("wallet =",wallet)
                    print("interest -->",100*(wallet/walletinit)-100,'%')
                    if 100*(wallet/walletinit)-100 < 0:
                        print("L O S E R !!!")
                    break
            btc_hist = btc_new
            btc_old = btc_new
            print('the crisis is over !','\n')
    
    except KeyboardInterrupt:
        curve(x,y)
        feedback()
            

print('succed !!!')
feedback()