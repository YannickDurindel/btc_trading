#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 17:47:30 2021

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
portfolio = 0


while True:
    bitcoin_old = bitcoin_new
    bitcoin_new = getbitcoin()
    if bitcoin_old <= bitcoin_new and (bitcoin_old*portfolio)+0.2 < bitcoin_new*portfolio :
        wallet = portfolio*bitcoin_new -0.1
        print('wallet = ',wallet)
    if bitcoin_old >= bitcoin_new :
        portfolio = (wallet-0.1)/bitcoin_new