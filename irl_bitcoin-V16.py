#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 17:59:55 2021

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

def curve (x,y,title,yname):
    plt.plot(x, y)
    plt.xlabel('Time  (s)')
    plt.ylabel(yname)
    plt.title(title)
    plt.show()

wallet = 1000
bitcoin_new = getbitcoin()
bitcoin_old = getbitcoin()
portfolio = 1000/bitcoin_new
W = 1000
Wallet = [1000]
n = 0
t = [0]
btc_value = [bitcoin_new]

while True:
    try :
        bitcoin_old = bitcoin_new
        bitcoin_new = getbitcoin()
        n += 1
        if bitcoin_old <= bitcoin_new and (bitcoin_old*portfolio)+0.2 < bitcoin_new*portfolio :
            wallet = portfolio*bitcoin_new -0.1
            Wallet.append(wallet)
            t.append(n)
            btc_value.append(bitcoin_new)
            curve(t,Wallet,'Wallet (USD)','Money I own (USD)')
        if bitcoin_old >= bitcoin_new :
            portfolio = (wallet-0.1)/bitcoin_new
        print('bitcoin =',bitcoin_new)
        print('temps = ', n)
        print('wallet = ',wallet)
        time.sleep(1)
    except KeyboardInterrupt :
        if wallet == 0:
            while bitcoin_new <= bitcoin_old :
                wallet = portfolio*bitcoin_new - 0.1
        break

time1 = time.time()
print('temps total = ',time1-time0)
curve(t,btc_value,'Bitcoin Curve (USD)','Bitcoin Value (USD)')