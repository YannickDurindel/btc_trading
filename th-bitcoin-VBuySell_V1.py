#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 18:29:26 2021

@author: yannick
"""

from coinbase.wallet.client import Client

api_key = "QvlHIa2QowcadkiG"
api_secret = "zfW0BlnUNnSxhlyEyulVhdxgOq3pQeV9"

client = Client(api_key,api_secret,api_version='2021-12-09')

payment_methods = client.get_payment_methods()

account = client.get_primary_account()
payment_method = client.get_payment_methods()[0]


buy_price  = client.get_buy_price(currency='EUR')
sell_price = client.get_sell_price(currency='EUR')


buy = account.buy(amount='0.0001',currency="BTC",payment_method=payment_method.id)

sell = account.sell(amount='0.0001',currency="BTC",payment_method=payment_method.id)

print("haha, we just stole you 2 f*cking dollars !")