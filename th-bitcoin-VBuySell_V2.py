#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 08:06:01 2021

@author: yannick
"""

import hmac, hashlib, time, requests, os
from coinbase.wallet.client import Client

api_key = "QvlHIa2QowcadkiG"
api_secret = "zfW0BlnUNnSxhlyEyulVhdxgOq3pQeV9"
btc_id = "3EeyuD2vw7NJreEiHQcGseVSHCn5zNDE2t"
usdt_id = "0xd3d3Dd3B72Ca085787A1a0FCfA36956c7267f6ba"

client = Client(api_key,api_secret,api_version='2021-12-09')

payment_methods = client.get_payment_methods()

account = client.get_primary_account()
payment_method = client.get_payment_methods()[0]

usdt_acct_id = os.environ.get('USDT_ID')
btc_acct_id = os.environ.get('BTC_ID')

transfer = client.transfer_money(btc_id, to=usdt_id, amount=0b101, currency="USDT")