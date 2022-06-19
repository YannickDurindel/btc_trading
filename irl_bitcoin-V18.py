#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 18:26:24 2021

@author: yannick
"""

import requests
import time
import matplotlib.pyplot as plt

time0 = time.time()

def getbitcoin():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    return int(data["bpi"]["EUR"]["rate"][0:2]+data["bpi"]["EUR"]["rate"][3:6]+data["bpi"]["EUR"]["rate"][7:13])*0.0001

def curve (x,y,title,yname):
    plt.plot(x, y)
    plt.xlabel('Time  (s)')
    plt.ylabel(yname)
    plt.title(title)
    plt.show()

wallet = 4000
bitcoin_new = getbitcoin()
bitcoin_old = getbitcoin()
portfolio = 4000/bitcoin_new
W = 4000
Wallet = []
n = 0
t = []
btc_value = []

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
            curve(t,Wallet,'Wallet (EUR)','Money I own (EUR)')
        if bitcoin_old >= bitcoin_new :
            portfolio = (wallet-0.1)/bitcoin_new
        print('bitcoin =',bitcoin_new)
        print('temps = ', n)
        print('wallet = ',wallet)
        time.sleep(1)
    except KeyboardInterrupt :
        if wallet == 0:
            while bitcoin_new <= bitcoin_old :
                wallet = portfolio*bitcoin_new - 1
        break

time1 = time.time()
print('temps total = ',time1-time0)
curve(t,btc_value,'Bitcoin Curve (EUR)','Bitcoin Value (EUR)')