#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 21:54:13 2021

@author: yannick
"""

import requests

def getbitcoin():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    return int(data["bpi"]["USD"]["rate"][0:2]+data["bpi"]["USD"]["rate"][3:6]+data["bpi"]["USD"]["rate"][7:13])*0.0001

wallet = 1000
bitcoin_new = getbitcoin()
bitcoin_old = getbitcoin()
bitcoin_min = getbitcoin()
portfolio = 1000/bitcoin_new

while True:
    try :
        bitcoin_old = bitcoin_new
        bitcoin_new = getbitcoin()
    
        if bitcoin_old < bitcoin_new and bitcoin_new >= bitcoin_min :
            wallet = portfolio*bitcoin_new
            bitcoin_min = getbitcoin()
            print(wallet)
        
        if bitcoin_old > bitcoin_new and bitcoin_new < bitcoin_min :
            while bitcoin_new < bitcoin_min :
                bitcoin_new = getbitcoin()
            portfolio = wallet/bitcoin_new
            bitcoin_min = getbitcoin()
        
        if bitcoin_old > bitcoin_new and bitcoin_new >= bitcoin_min:
            portfolio = wallet/bitcoin_new
            bitcoin_top = getbitcoin()
            
    except KeyboardInterrupt: 
        if wallet == 0:
            while bitcoin_new <= bitcoin_old :
                bitcoin_new = getbitcoin()
            wallet = portfolio*bitcoin_new
        break