#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 18:12:28 2022

@author: yannick
"""

from binance.client import Client
import time

api_key = "wsWyaiQ0dlAWj4eFE4AdvbOtmtnj2sKTMv3f53CRy6NsGIBdTZy3ZxUggAMOZr1f"
api_secret = "AlBOMFfj60b6xjWldKv6Vex5l4y4REqrU2e17XIbeRmAJVZ4Jakh7CdgSu5U5mid"
binance_client = Client(api_key, api_secret)
btc_wallet = True
btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
btc_prevprice = btc_newprice
btc_min = btc_newprice
btc_max = btc_prevprice

def getwallet(currency):
    account_info = binance_client.futures_account()
    av_balance = None
    for asset in account_info["assets"]:
        if asset["asset"] == currency:
            av_balance = float(asset["marginBalance"])
    return av_balance

wallet = getwallet("USDT")
binance_client.futures_change_leverage(symbol='BTCUSDT', leverage=20)
btc_buysell = round((wallet-1)*20/btc_newprice,3)

def buy (btc_wallet,btc_buysell,btc_newprice):
    #binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='BUY',quantity=btc_buysell)
    print('buy',btc_newprice)
    return (False,btc_newprice,btc_newprice) # = (btc_wallet,btc_prevprive,btc_min)
    
def sell (btc_wallet,btc_buysell,btc_newprice,wallet):
    #binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
    print('sell',btc_newprice,wallet,'\n')
    return (True,btc_newprice,btc_newprice,round((wallet-1)*20/btc_newprice,3)) # = (btc_wallet,btc_prevprice,btc_max,btc_buysell)
    
print("TO THE MOON !!!\n")
while True :
    try :
        btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
        wallet = getwallet("USDT")
        
        if btc_wallet == True and btc_newprice*1.005 < btc_prevprice and btc_newprice > btc_min*1.0035 :
            (btc_wallet,btc_prevprive,btc_min) = buy(btc_wallet,btc_buysell,btc_newprice)
            
        elif btc_wallet == False and btc_newprice > btc_prevprice*1.005 and btc_newprice*1.002 < btc_max :
            (btc_wallet,btc_prevprice,btc_max,btc_buysell) = sell(btc_wallet,btc_buysell,btc_newprice,wallet)
            
        elif btc_wallet == True and btc_newprice < btc_min :
            btc_min = btc_newprice
        
        elif btc_wallet == False and btc_newprice > btc_max :
            btc_max = btc_newprice
            
        time.sleep(2.5)
    
    except KeyboardInterrupt :
        print("Code stopped !, Here is your wallet,",wallet)
        break
    
    except Exception as e:
        print('\n',e,'\n')
        time.sleep(1)
        pass
        
