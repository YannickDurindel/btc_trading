#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 15:29:58 2021

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
portfolio = 100/getbitcoin()
W = 100
Wallet = []
n = 0
t = []
btc_value = []
bitcoin = getbitcoin()
min = bitcoin
max = bitcoin + 50

while wallet<101:
    bitcoin = getbitcoin()
    if bitcoin >= max :
        wallet = portfolio*bitcoin
        portfolio = 0
        min = bitcoin - 20
        max += 1
        print("MAX !      MAX !        MAX !        MAX !")
    if bitcoin <= min :
        portfolio = wallet/bitcoin
        wallet = 0
        min -= 1
        max = bitcoin + 20
        print("MIN !        MIN !        MIN !       MIN !")
    if bitcoin > max:
        max = bitcoin
        min = bitcoin - 20
    if bitcoin < min :
        min = bitcoin
        max = bitcoin + 20
    if wallet == 0:
        W = portfolio*bitcoin
        print("wallet=0")
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
    curve(t,btc_value)

curve(t,Wallet)