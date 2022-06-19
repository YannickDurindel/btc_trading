#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 10:57:15 2021

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

t = []
btc_value = []
wallet = 100
walletlist = []
walletlist.append(wallet)
portfolio = wallet/getbitcoin()
print('wallet = ',wallet)
print("portfolio = ",portfolio)
print('bitcoin = ',getbitcoin())
max = getbitcoin()
min = getbitcoin()*0.99995

for i in range(1000):
    t.append(i)
    btc_value.append(getbitcoin())    
    print('bitcoin =',getbitcoin())
    print('temps = ',i)
    print('wallet = ',wallet)
    if getbitcoin() == min:
        portfolio = wallet/getbitcoin()
        wallet = 0
        walletlist.append(portfolio*getbitcoin())
        min = getbitcoin()
        max = getbitcoin()+50
    if getbitcoin() == max:
        wallet = portfolio*getbitcoin()
        portfolio = 0
        walletlist.append(wallet)
        min = getbitcoin()-50
        max = getbitcoin()
    #time.sleep(0.5)
    curve(t,btc_value)
        
if wallet == 0:
    print('wallet = ',getbitcoin())
else :
    print('wallet = ',wallet)

curve(t,wallet)