#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 22:32:28 2022

@author: yannick
"""

from BinanceFuturesPy.futurespy import Client
from binance.client import Client as ClientReal

api_key = "M9FsR6XdaZKkIhHmKeCsGSdjYzVWIWGlnsMxM1n6NnTViEaOoKXsPb0ItO4usCuD"
api_secret = "teJ7r78Xn3kNKFV80YZNpdyIo1shEVmu6Yaeb8EGktH7ZTVoBjk4eWgRELGgtpvm"

client = Client(api_key, api_secret, testnet=True)
clientreal = ClientReal(api_key, api_secret)

print(client.futures_account_balance())