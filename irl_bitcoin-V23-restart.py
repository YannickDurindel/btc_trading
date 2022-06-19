#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 10:57:01 2022

@author: yannick
"""

import requests
import time
import random
import matplotlib.pyplot as plt
from binance.client import Client

# init
api_key = "M9FsR6XdaZKkIhHmKeCsGSdjYzVWIWGlnsMxM1n6NnTViEaOoKXsPb0ItO4usCuD"
api_secret = "3syXcf4fZ1Q0h51HNxYN8msjOe5RXzmyMm11KZvCnTCf3XGjK2nn4M0dK51qFu5i"
client = Client(api_key, api_secret)

def getbitcoin():
#    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
#    data = response.json()
#    return int(data["bpi"]["EUR"]["rate"][0:2]+data["bpi"]["EUR"]["rate"][3:6]+data["bpi"]["EUR"]["rate"][7:13])*0.0001
    btc_price = float(client.get_symbol_ticker(symbol="BTCUSDT")['price'])
    return btc_price

def HoldOn(t0,dt):
    t1 = time.time()
    while t0 + dt > t1 :
        t1 = time.time()
        
def feedback():
    print("bitcoin price (EUR) : ",btc_new)
    print("wallet = ",wallet,'EUR')
    print("time = ",st,'sec')
    print('actions = ',n,'/',nmax,'    -->',100*n/nmax,'%')
    print('interest = ',100*(wallet/walletinit)-100,'%')
    print('\n')
    
def btc_crv(show):
    t0 = time.time()
    t.append(t0-tinit)
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    btc_val.append(int(data["bpi"]["EUR"]["rate"][0:2]+data["bpi"]["EUR"]["rate"][3:6]+data["bpi"]["EUR"]["rate"][7:13])*0.0001)
    plt.plot(t,btc_val)
    plt.xlabel('Time  (s)')
    plt.ylabel('bitcoin value (EUR)')
    plt.title("bitcoin curve")
    if show == True:
        plt.show()
        
t = []
btc_val = []
tinit = time.time()
st = 0
n = 0
nmax = random.randint(20,30)*2
btc_old = getbitcoin()
btc_hist = btc_old
wallet = 40
walletinit = wallet
portfolio = 0
while wallet<=80 :
    t0 = time.time()
    btc_new = getbitcoin()
    #if btc_new == btc_old :
        #btc_crv(False)
    if btc_new > btc_old*1.0004 and wallet == 0:
        wallet = portfolio * btc_new/1.0002
        portfolio = 0
        btc_hist = btc_old
        btc_old = btc_new
        n+=1
        print("sell")
        feedback()
        #btc_crv(True)
    if btc_new*1.0002 < btc_old and portfolio == 0 :
        portfolio = wallet / btc_new*1.0002
        wallet = 0
        btc_hist = btc_old
        btc_old = btc_new
        n+=1
        print('buy')
        print("bitcoin price (EUR) : ",btc_new)
        print('actions = ',n,'/',nmax)
        print('\n')
        #btc_crv(True)
    if btc_new < btc_old and btc_old < btc_hist :
        print('the hell case happens !!!','\n')
        print("bitcoin price hist (EUR) : ",btc_hist,'\n')
        while btc_new <= btc_hist :
            try:
                if btc_new != getbitcoin() :
                    btc_new = getbitcoin()
                    print("bitcoin price (EUR) : ",btc_new,'over',btc_hist,'\n')
                    #btc_crv(True)
            except KeyboardInterrupt:
                wallet = portfolio*btc_new/1.0002
                print("KeyboardInterrrupt !\n")
                print("wallet =",wallet)
                print("interest -->",100*(wallet/walletinit)-100,'%')
                if 100*(wallet/walletinit)-100 < 0:
                    print("L O S E R !!!")
                break
        btc_hist = btc_new
        print('the crisis is over !','\n')
            
    #HoldOn(t0,1)
    st+=1

print('succed !!!')
feedback()