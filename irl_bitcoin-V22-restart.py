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

def getbitcoin():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    return int(data["bpi"]["EUR"]["rate"][0:2]+data["bpi"]["EUR"]["rate"][3:6]+data["bpi"]["EUR"]["rate"][7:13])*0.0001

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
    
def btc_crv():
    t = []
    btc_val = []
    t0 = time.time()
    t.append(t0)
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    btc_val.append(int(data["bpi"]["EUR"]["rate"][0:2]+data["bpi"]["EUR"]["rate"][3:6]+data["bpi"]["EUR"]["rate"][7:13])*0.0001)
    plt.plot(t, btc_val)
    plt.xlabel('Time  (s)')
    plt.ylabel('bitcoin value (EUR)')
    plt.title("bitcoin curve")
    plt.show()
        
tinit = time.time()
st = 0
n = 0
nmax = random.randint(20,30)*2
btc_old = getbitcoin()
btc_hist = btc_old
wallet = 4000
walletinit = wallet
portfolio = 0
while n < nmax :
    t0 = time.time()
    btc_new = getbitcoin()
    btc_crv()
    if btc_new > btc_old and wallet == 0:
        wallet = portfolio * btc_new - 0.01
        portfolio = 0
        btc_hist = btc_old
        btc_old = btc_new
        n+=1
        print("sell")
        feedback()
    if btc_new < btc_old and portfolio == 0 :
        portfolio = (wallet-0.01) / btc_new
        wallet = 0
        btc_hist = btc_old
        btc_old = btc_new
        n+=1
        print('buy')
        print("bitcoin price (EUR) : ",btc_new)
        print('actions = ',n,'/',nmax)
        print('\n')
    HoldOn(t0,1)
    st+=1

print('succed !!!')
feedback()