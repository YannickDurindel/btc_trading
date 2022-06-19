#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 20:16:39 2021

@author: yannick
"""

from coinbase.wallet.client import Client

api_key = "QvlHIa2QowcadkiG"
api_secret = "zfW0BlnUNnSxhlyEyulVhdxgOq3pQeV9"
btc_id = "5b71fc48-3dd3-540c-809b-f8c94d0e68b5"
usdt_id = "2176dca5-980b-5af9-8560-cc67b7d92ece"

client = Client(api_key,api_secret,api_version='2021-12-09')

payment_methods = client.get_payment_methods()

account = client.get_primary_account()
payment_method = client.get_payment_methods()[0]

transfer = account.transfer_money(to=btc_id, amount="5", currency="USDT")