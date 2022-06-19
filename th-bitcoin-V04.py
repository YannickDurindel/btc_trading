#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 10:08:05 2021

@author: yannick
"""

import requests
import time
import matplotlib.pyplot as plt

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
bitcoin_old = int(data["bpi"]["USD"]["rate"][0:2]+data["bpi"]["USD"]["rate"][3:6]+data["bpi"]["USD"]["rate"][7:13])*0.0001
bitcoin_new = int(data["bpi"]["USD"]["rate"][0:2]+data["bpi"]["USD"]["rate"][3:6]+data["bpi"]["USD"]["rate"][7:13])*0.0001
wallet = 10
portfolio = 10/bitcoin_new
print('wallet = ',wallet)
print("portfolio = ",portfolio)
print('bitcoin = ',bitcoin_new)
n = 0
x = []
y = []

while bitcoin_new == bitcoin_old :
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    bitcoin_new = int(data["bpi"]["USD"]["rate"][0:2]+data["bpi"]["USD"]["rate"][3:6]+data["bpi"]["USD"]["rate"][7:13])*0.0001
    
if bitcoin_new>bitcoin_old :
    groth = True
else :
    groth = False
print('groth = ',groth)


while n<15 :
    bitcoin_old = bitcoin_new
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    bitcoin_new = int(data["bpi"]["USD"]["rate"][0:2]+data["bpi"]["USD"]["rate"][3:6]+data["bpi"]["USD"]["rate"][7:13])*0.0001
    print('bitcoin_old = ',bitcoin_old)
    print('bitcoin_new = ',bitcoin_new)
    print('time (s) = ',n)
    if bitcoin_new>bitcoin_old and groth == False :
        portfolio = wallet/bitcoin_new
        wallet = 0
        groth = True
    if bitcoin_new<bitcoin_old and groth == True :
        wallet = portfolio*bitcoin_new
        portfolio = 0
        groth = False
    x.append(n)
    y.append(bitcoin_new)
    n+=1
    time.sleep(1)

print('wallet = ',wallet)
print("portfolio = ",portfolio)

plt.plot(x, y)
plt.xlabel('Time  (s)')
plt.ylabel('avg Bitcoin value  (USD)')
plt.title('Bitcoin curve')
plt.show()