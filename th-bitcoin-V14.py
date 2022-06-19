#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 14:00:57 2021

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
portfolio = 1000/bitcoin_new
W = 1000
Wallet = []
n = 0
t = []
btc_value = []

while wallet<1100:
    bitcoin_old = bitcoin_new
    bitcoin_new = getbitcoin()
    if bitcoin_old <= bitcoin_new  :
        wallet = portfolio*bitcoin_new
        n += 1
        t.append(n)
        Wallet.append(wallet)
        curve(t,Wallet)
    if bitcoin_old >= bitcoin_new :
        portfolio = wallet/bitcoin_new
    print('bitcoin =',bitcoin_new)
    print('temps = ', n)
    print('wallet = ',wallet)
    time.sleep(1)
    btc_value.append(bitcoin_new)
time1 = time.time()
print('tenps total = ',time1-time0)
curve(t,btc_value)