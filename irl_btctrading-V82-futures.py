#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 19:36:52 2022

@author: yannick
"""

from binance.client import Client
import time

api_key = "wsWyaiQ0dlAWj4eFE4AdvbOtmtnj2sKTMv3f53CRy6NsGIBdTZy3ZxUggAMOZr1f"
api_secret = "AlBOMFfj60b6xjWldKv6Vex5l4y4REqrU2e17XIbeRmAJVZ4Jakh7CdgSu5U5mid"
binance_client = Client(api_key, api_secret)
btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
btc_prevprice = btc_newprice
btc_min = btc_newprice
btc_max = btc_newprice
btc_wallet = True
t0 = time.time()
print("TO THE MOON !!!\n")
def getwallet(currency):
    account_info = binance_client.futures_account()
    av_balance = None
    for asset in account_info["assets"]:
        if asset["asset"] == currency:
            av_balance = float(asset["marginBalance"])
    return av_balance

while True :
    try :
        btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
        wallet = getwallet("USDT")
        if btc_newprice > btc_prevprice*1.005 and btc_wallet == False:
            #buy
            print("sell, wallet =",getwallet("USDT"),"the low gap was",btc_prevprice/btc_min,"\n")
            btc_prevprice = btc_newprice
            btc_max = btc_newprice
            btc_wallet = True
        elif btc_newprice*1.005 < btc_prevprice and btc_wallet == True:
            if time.time()-t0 < 200 :
                t0 = time.time()
                btc_min = btc_newprice
                while time.time() < t0+1200 :
                    btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
                    if btc_newprice < btc_min :
                        btc_min = btc_prevprice
                    elif btc_newprice*1.005 >= btc_prevprice :
                        t0 = 0
                    elif btc_newprice > btc_min*1.002 :
                        t0 =0
            #buy
            print("buy, the high gap was",btc_max/btc_prevprice,"\n")
            btc_prevprice = btc_newprice
            btc_wallet = False
            btc_min = btc_newprice
        elif btc_newprice > btc_max :
            btc_max = btc_newprice
            if btc_wallet == True :
                btc_prevprice = btc_newprice
                t0 = time.time()
        elif btc_newprice < btc_min  :
            btc_min = btc_newprice

    except Exception as e:
        print("Error:", e,'\n')
        time.sleep(1)
        pass

    except KeyboardInterrupt:
        #sell
        break
