#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 12:46:30 2021

@author: yannick
"""

import requests
import time
import matplotlib.pyplot as plt

def getbitcoin():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    return int(data["bpi"]["USD"]["rate"][0:2]+data["bpi"]["USD"]["rate"][3:6]+data["bpi"]["USD"]["rate"][7:13])*0.0001

bitcoin_old = getbitcoin()
while getbitcoin() == bitcoin_old :
    bitcoin_new = getbitcoin()
if bitcoin_new>bitcoin_old :
    groth = True
else :
    groth = False
    
wallet = 10
portfolio = wallet/bitcoin_new
print('wallet = ',wallet)
print("portfolio = ",portfolio)
print('bitcoin = ',bitcoin_new)
print('groth = ',groth)
n = 0
x = []
y = []


def curve (x,y):
    plt.plot(x, y)
    plt.xlabel('Time  (s)')
    plt.ylabel('avg Bitcoin value  (USD)')
    plt.title('Bitcoin curve')
    plt.show()


while n<500 :
    bitcoin_old = bitcoin_new
    bitcoin_new = getbitcoin()
    print('bitcoin_old = ',bitcoin_old)
    print('bitcoin_new = ',bitcoin_new)
    print('time (s) = ',n)
    if bitcoin_new>bitcoin_old*1.001 and groth == False :
        portfolio = wallet/bitcoin_new
        wallet = 0
        groth = True
    if bitcoin_new*1.001<bitcoin_old and groth == True :
        wallet = portfolio*bitcoin_new
        portfolio = 0
        groth = False
    x.append(n)
    y.append(bitcoin_new)
    n+=1
    time.sleep(1)

if wallet == 0:
    print('wallet = ',portfolio*bitcoin_new)
else :
    print('wallet = ',wallet)

curve(x,y)