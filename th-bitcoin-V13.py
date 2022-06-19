#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 10:39:52 2021

@author: yannick
"""

import requests
import time
import matplotlib.pyplot as plt

time0 = time.time()

def getbitcoin():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    return int(data["bpi"]["USD"]["rate"][0:2]+data["bpi"]["USD"]["rate"][3:6]+data["bpi"]["USD"]["rate"][7:13])*0.0001

def curve (x,y):
    plt.plot(x, y)
    plt.xlabel('Time  (s)')
    plt.ylabel('Money  (USD)')
    plt.title('Wallet')
    plt.show()

wallet = 1000
bitcoin_new = getbitcoin()
bitcoin_old = getbitcoin()
bitcoin_min = getbitcoin()
portfolio = 1000/bitcoin_new
W = 1000
Wallet = [1000]
n = 0
t = [0]
btc_value = []

while True:
    try :
        bitcoin_old = bitcoin_new
        bitcoin_new = getbitcoin()
    
        if bitcoin_old < bitcoin_new and bitcoin_new >= bitcoin_min :
            wallet = portfolio*bitcoin_new
            t.append(n)
            Wallet.append(W)
            curve(t,Wallet)
            bitcoin_min = getbitcoin()
        
        if bitcoin_old > bitcoin_new and bitcoin_new < bitcoin_min :
            while bitcoin_new < bitcoin_min :
                time.sleep(1)
                bitcoin_new = getbitcoin()
            portfolio = wallet/bitcoin_new
            bitcoin_min = getbitcoin()
        
        if bitcoin_old > bitcoin_new and bitcoin_new >= bitcoin_min:
            portfolio = wallet/bitcoin_new
            bitcoin_top = getbitcoin()
        
        if wallet == 0:
            W = portfolio*bitcoin_new
        
        else :
            W = wallet
        
        print('bitcoin =',bitcoin_new)
        print('temps = ', n)
        print('wallet = ',W)
        time.sleep(1)
        n += 1
        btc_value.append(bitcoin_new)
    
    except KeyboardInterrupt: 
        if wallet == 0:
            wallet = portfolio*bitcoin_new
        break
    
time1 = time.time()
print('temps total = ',time1-time0)
curve(t,btc_value)