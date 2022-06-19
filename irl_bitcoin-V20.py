#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 13:30:29 2022

@author: yannick
"""

import requests
import time
import matplotlib.pyplot as plt
import random

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

wallet = 0
bitcoin_new = getbitcoin()
bitcoin_old = getbitcoin()
portfolio = 4000/bitcoin_new
W = 4000
Wallet = []
n = 0
t_btc = []
t_wallet = []
btc_value = []

while True :
    try :
        actions = 0
        actionsmax = random.randint(20,30)*2
        while actions <= actionsmax:
            try :
                bitcoin_new = getbitcoin()
                n += 1
                if bitcoin_new != bitcoin_old:
                    btc_value.append(bitcoin_new)
                    t_btc.append(n)
                if bitcoin_old*1.001 < bitcoin_new and (bitcoin_old*portfolio)+0.2 < bitcoin_new*portfolio and wallet == 0 :
                    wallet = portfolio*bitcoin_new -0.1
                    portfolio = 0
                    actions += 1
                    bitcoin_old = bitcoin_new
                    Wallet.append(wallet)
                    t_wallet.append(n)
                    curve(t_wallet,wallet,'Wallet (EUR)','Money I own (EUR)')
                    print('bitcoin =',bitcoin_new)
                    print('temps = ', n)
                    print('wallet = ',wallet)
                    print(actions,'/',actionsmax)
                if bitcoin_old > bitcoin_new and portfolio == 0 :
                    portfolio = (wallet-0.1)/bitcoin_new
                    wallet = 0
                    bitcoin_old = bitcoin_new
                    actions += 1
                time.sleep(1)
            except KeyboardInterrupt :
                print("I'm trading bitch, don't interrupt me !")
                print("you have 5 sec to force")
                try:
                    time.sleep(5)
                except KeyboardInterrupt:
                        break
                    
        time1 = time.time()
        print('bitcoin =',bitcoin_new)
        print('total time = ',time1-time0)
        print('final wallet = ',wallet)
        print(actionsmax,'actions done')
        curve(t_btc,btc_value,'Bitcoin Curve (EUR)','Bitcoin Value (EUR)')
    
    except KeyboardInterrupt:
        time1 = time.time()
        print('bitcoin =',bitcoin_new)
        print('total time = ',time1-time0)
        print('final wallet = ',wallet)
        print(actionsmax,'actions done')
        curve(t_btc,btc_value,'Bitcoin Curve (EUR)','Bitcoin Value (EUR)')
        break
        break