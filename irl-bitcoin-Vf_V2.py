#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 17:44:15 2021

@author: yannick
"""

import requests
from coinbase.wallet.client import Client
import time

def getbitcoin():
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = response.json()
    return int(data["bpi"]["USD"]["rate"][0:2]+data["bpi"]["USD"]["rate"][3:6]+data["bpi"]["USD"]["rate"][7:13])*0.0001
    
api_key = "QvlHIa2QowcadkiG"
api_secret = "zfW0BlnUNnSxhlyEyulVhdxgOq3pQeV9"
client = Client(api_key,api_secret,api_version='2021-12-09')
account = client.get_primary_account()
payment_method = client.get_payment_methods()
wallet = 1000
bitcoin_new = getbitcoin()
bitcoin_old = getbitcoin()
portfolio = 1000/bitcoin_new

while True:
    try :
        bitcoin_old = bitcoin_new
        bitcoin_new = getbitcoin()
        if bitcoin_old <= bitcoin_new  :
            wallet = account.sell(amount=str(portfolio),currency="BTC",payment_method=payment_method.id)
            portfolio = 0
        if bitcoin_old >= bitcoin_new :
            portfolio = account.buy(amount=str(wallet/bitcoin_new),currency="BTC",payment_method=payment_method.id)
            wallet = 0
        time.sleep(1)
    except KeyboardInterrupt :
        if wallet == 0:
            while bitcoin_new <= bitcoin_old :
                time.sleep(1)
            wallet = account.sell(amount=str(portfolio),currency="BTC",payment_method=payment_method.id)
        break
print(wallet)