#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 17:18:50 2021

@author: yannick
"""

import requests
import time
import matplotlib.pyplot as plt

def getbitcoin():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    return int(data["bpi"]["USD"]["rate"][0:2]+data["bpi"]["USD"]["rate"][3:6]+data["bpi"]["USD"]["rate"][7:13])*0.0001

def curve (x,y):
    plt.plot(x, y)
    plt.xlabel('Time  (s)')
    plt.ylabel('avg Bitcoin value  (USD)')
    plt.title('Bitcoin curve')
    plt.show()

wallet = 100
portfolio = 0
W = 100
Wallet = []
n = 0
t = []
btc_value = []
bitcoin = getbitcoin()
min = bitcoin
max = bitcoin + 20
test = 0        # 0 = position normale ; 1 = max ; 2 = min

while wallet<110:
    bitcoin = getbitcoin()
    if bitcoin >= max and test == 0 :
        wallet = portfolio*bitcoin
#        portfolio = 0
        min = bitcoin - 30
        max -= 1
        test = 1
        print("MAX !      MAX !        MAX !        MAX !")
    if bitcoin <= min and test == 0:
        portfolio = wallet/bitcoin
#        wallet = 0
        min += 1
        max = bitcoin + 30
        test = 2
        print("MIN !        MIN !        MIN !       MIN !")
    if bitcoin <= max and bitcoin >= min :
        test = 0
    if bitcoin > max :
        max = bitcoin
        min = bitcoin - 30
    if bitcoin < min :
        min = bitcoin
        max = bitcoin + 30
    if wallet == 0:
        W = portfolio*bitcoin
    else :
        W = wallet
    Wallet.append(W)
    print('bitcoin =',bitcoin)
    print('temps = ', n)
    print('wallet = ',W)
    time.sleep(1)
    n += 1
    t.append(n)
    btc_value.append(bitcoin)
    curve(t,Wallet)

curve(t,btc_value)