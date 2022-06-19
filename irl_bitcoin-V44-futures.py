#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 23:01:49 2022

@author: yannick
"""

from binance.client import Client
api_key = "GjwGiZnhWcMUQyxJqNzHU5WiZkicRF00iLMZONYrvSWmwlk4DRnSBm98tnSE3xzF"
api_secret = "teJ7r78Xn3kNKFV80YZNpdyIo1shEVmu6Yaeb8EGktH7ZTVoBjk4eWgRELGgtpvm"
binance_client = Client(api_key, api_secret)

btc_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])

def getwallet(currency):
    account_info = binance_client.futures_account()
    av_balance = None
    for asset in account_info["assets"]:
        if asset["asset"] == currency:
            av_balance = float(asset["marginBalance"])
    return av_balance

binance_client.futures_change_leverage(symbol='BTCUSDT', leverage=1)

binance_client.futures_create_order(symbol='ETHUSDT',type='MARKET',side='BUY',quantity=0.1)
