#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 18:21:41 2021

@author: yannick
"""

import requests
import time

def getbitcoin():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    return int(data["bpi"]["USD"]["rate"][0:2]+data["bpi"]["USD"]["rate"][3:6]+data["bpi"]["USD"]["rate"][7:13])*0.0001

wallet = 1000
bitcoin_new = getbitcoin()
bitcoin_old = getbitcoin()
portfolio = 1000/bitcoin_new
W = 1000
time0 = time.time()

while True:
    try :
        bitcoin_old = bitcoin_new
        bitcoin_new = getbitcoin()
        if bitcoin_old <= bitcoin_new  :
            wallet = portfolio*bitcoin_new
        if bitcoin_old >= bitcoin_new :
            portfolio = wallet/bitcoin_new
        if wallet == 0:
            W = portfolio*bitcoin_new
        else :
            W = wallet
        time.sleep(0.87)
        time1 = time.time()
        print('temps = ', time1 - time0)
        print('wallet = ',W)
    except KeyboardInterrupt:
        if wallet == 0:
            wallet = portfolio*bitcoin_new
        break
    
print('temps total = ',time1-time0)