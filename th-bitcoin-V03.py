#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:07:36 2021

@author: yannick
"""

import requests
import time
import matplotlib.pyplot as plt

btc = 0
btc_val = []
btc_irt = []
n = 0
x = []
y = []
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
bitcoin_old = int(data["bpi"]["USD"]["rate"][0:2]+data["bpi"]["USD"]["rate"][3:6]+data["bpi"]["USD"]["rate"][7:13])*0.0001
bitcoin_new = int(data["bpi"]["USD"]["rate"][0:2]+data["bpi"]["USD"]["rate"][3:6]+data["bpi"]["USD"]["rate"][7:13])*0.0001
wallet = 10
portfolio = 0

while bitcoin_new == bitcoin_old :
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    bitcoin_new = int(data["bpi"]["USD"]["rate"][0:2]+data["bpi"]["USD"]["rate"][3:6]+data["bpi"]["USD"]["rate"][7:13])*0.0001
    
if bitcoin_new>bitcoin_old :
    groth = True
else :
    groth = False

while n<10 :
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    btc = int(data["bpi"]["USD"]["rate"][0:2]+data["bpi"]["USD"]["rate"][3:6]+data["bpi"]["USD"]["rate"][7:13])*0.0001
    btc_irt.append(btc)
    y.append(btc)
    bitcoin_new = btc
    time.sleep(1)
    bitcoin_old  = bitcoin_new
    n+=1
    print(n)
    x.append(n)
    #btc_val.append((btc_irt[0]+btc_irt[1]+btc_irt[2]+btc_irt[3]+btc_irt[4])/5)
    
plt.plot(x, y)
plt.xlabel('Time  (s)')
plt.ylabel('avg Bitcoin value  (USD)')
plt.title('Bitcoin curve')
plt.show()