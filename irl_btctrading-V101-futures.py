#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 2 21:58:21 2022

@author: yannick
"""

from binance.client import Client
import time

api_key = "wsWyaiQ0dlAWj4eFE4AdvbOtmtnj2sKTMv3f53CRy6NsGIBdTZy3ZxUggAMOZr1f"
api_secret = "AlBOMFfj60b6xjWldKv6Vex5l4y4REqrU2e17XIbeRmAJVZ4Jakh7CdgSu5U5mid"
binance_client = Client(api_key, api_secret)
print("this is mad ...")

def getwallet(currency):
    account_info = binance_client.futures_account()
    av_balance = None
    for asset in account_info["assets"]:
        if asset["asset"] == currency:
            av_balance = float(asset["marginBalance"])
    return av_balance
wallet = getwallet("USDT")

btc_wallet = True
btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
btc_prevprice = btc_newprice
btc_min = btc_newprice
btc_max = btc_prevprice
wallet = getwallet("USDT")
binance_client.futures_change_leverage(symbol='BTCUSDT', leverage=20)
btc_buysell = round((wallet-1)*20/btc_newprice,3)
def buy_btc (btc_wallet,btc_buysell,btc_newprice):
    #binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='BUY',quantity=btc_buysell)
    print('buy btc',btc_newprice)
    return (False,btc_newprice,btc_newprice) # = (btc_wallet,btc_prevprive,btc_min)
def sell_btc (btc_wallet,btc_buysell,btc_newprice,wallet):
    #binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
    print('sell btc',btc_newprice,wallet,'\n')
    return (True,btc_newprice,btc_newprice,round((wallet-1)*20/btc_newprice,3)) # = (btc_wallet,btc_prevprice,btc_max,btc_buysell)

eth_wallet = True
eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
eth_prevprice = eth_newprice
eth_min = eth_newprice
eth_max = eth_prevprice
wallet = getwallet("USDT")
binance_client.futures_change_leverage(symbol='ETHUSDT', leverage=20)
eth_buysell = round((wallet-1)*20/eth_newprice,3)
def buy_eth (eth_wallet,eth_buysell,eth_newprice):
    #binance_client.futures_create_order(symbol='ETHUSDT',type='MARKET',side='BUY',quantity=eth_buysell)
    print('buy eth',eth_newprice)
    return (False,eth_newprice,eth_newprice) # = (eth_wallet,eth_prevprive,eth_min)
def sell_eth (eth_wallet,eth_buysell,eth_newprice,wallet):
    #binance_client.futures_create_order(symbol='ETHUSDT',type='MARKET',side='SELL',quantity=eth_buysell)
    print('sell eth',eth_newprice,wallet,'\n')
    return (True,eth_newprice,eth_newprice,round((wallet-1)*20/eth_newprice,3)) # = (eth_wallet,eth_prevprice,eth_max,eth_buysell)

xrp_wallet = True
xrp_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
xrp_prevprice = xrp_newprice
xrp_min = xrp_newprice
xrp_max = xrp_prevprice
wallet = getwallet("USDT")
binance_client.futures_change_leverage(symbol='XRPUSDT', leverage=20)
xrp_buysell = round((wallet-1)*20/xrp_newprice,3)
def buy_xrp (xrp_wallet,xrp_buysell,xrp_newprice):
    #binance_client.futures_create_order(symbol='XRPUSDT',type='MARKET',side='BUY',quantity=xrp_buysell)
    print('buy xrp',xrp_newprice)
    return (False,xrp_newprice,xrp_newprice) # = (xrp_wallet,xrp_prevprive,xrp_min)
def sell_xrp (xrp_wallet,xrp_buysell,xrp_newprice,wallet):
    #binance_client.futures_create_order(symbol='XRPUSDT',type='MARKET',side='SELL',quantity=xrp_buysell)
    print('sell xrp',xrp_newprice,wallet,'\n')
    return (True,xrp_newprice,xrp_newprice,round((wallet-1)*20/xrp_newprice,3)) # = (xrp_wallet,xrp_prevprice,xrp_max,xrp_buysell)

ada_wallet = True
ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
ada_prevprice = ada_newprice
ada_min = ada_newprice
ada_max = ada_prevprice
wallet = getwallet("USDT")
binance_client.futures_change_leverage(symbol='ADAUSDT', leverage=20)
ada_buysell = round((wallet-1)*20/ada_newprice,3)
def buy_ada (ada_wallet,ada_buysell,ada_newprice):
    #binance_client.futures_create_order(symbol='ADAUSDT',type='MARKET',side='BUY',quantity=ada_buysell)
    print('buy ada',ada_newprice)
    return (False,ada_newprice,ada_newprice) # = (ada_wallet,ada_prevprive,ada_min)
def sell_ada (ada_wallet,ada_buysell,ada_newprice,wallet):
    #binance_client.futures_create_order(symbol='ADAUSDT',type='MARKET',side='SELL',quantity=ada_buysell)
    print('sell ada',ada_newprice,wallet,'\n')
    return (True,ada_newprice,ada_newprice,round((wallet-1)*20/ada_newprice,3)) # = (ada_wallet,ada_prevprice,ada_max,ada_buysell)

bnb_wallet = True
bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
bnb_prevprice = bnb_newprice
bnb_min = bnb_newprice
bnb_max = bnb_prevprice
wallet = getwallet("USDT")
binance_client.futures_change_leverage(symbol='BNBUSDT', leverage=20)
bnb_buysell = round((wallet-1)*20/bnb_newprice,3)
def buy_bnb (bnb_wallet,bnb_buysell,bnb_newprice):
    #binance_client.futures_create_order(symbol='BNBUSDT',type='MARKET',side='BUY',quantity=bnb_buysell)
    print('buy bnb',bnb_newprice)
    return (False,bnb_newprice,bnb_newprice) # = (bnb_wallet,bnb_prevprive,bnb_min)
def sell_bnb (bnb_wallet,bnb_buysell,bnb_newprice,wallet):
    #binance_client.futures_create_order(symbol='BNBUSDT',type='MARKET',side='SELL',quantity=bnb_buysell)
    print('sell bnb',bnb_newprice,wallet,'\n')
    return (True,bnb_newprice,bnb_newprice,round((wallet-1)*20/bnb_newprice,3)) # = (bnb_wallet,bnb_prevprice,bnb_max,bnb_buysell)

print("TO THE MOON !!!\n")
while True :
    try :
        btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
        eth_newprice = float(binance_client.futures_symbol_ticker(symbol='ETHUSDT')['price'])
        xrp_newprice = float(binance_client.futures_symbol_ticker(symbol='XRPUSDT')['price'])
        ada_newprice = float(binance_client.futures_symbol_ticker(symbol='ADAUSDT')['price'])
        bnb_newprice = float(binance_client.futures_symbol_ticker(symbol='BNBUSDT')['price'])
        if btc_wallet == False:
            wallet = wallet*(btc_newprice/btc_prevprice*20)-19
        elif eth_wallet == False:
            wallet = wallet*(eth_newprice/eth_prevprice*20)-19
        elif xrp_wallet == False:
            wallet = wallet*(xrp_newprice/xrp_prevprice*20)-19
        elif ada_wallet == False:
            wallet = wallet*(ada_newprice/ada_prevprice*20)-19
        elif bnb_wallet == False:
            wallet = wallet*(bnb_newprice/bnb_prevprice*20)-19
            
        #btc bot
        if btc_wallet == True and btc_newprice*1.005 < btc_prevprice and btc_newprice > btc_min*1.0035 :
            (btc_wallet,btc_prevprive,btc_min) = buy_btc(btc_wallet,btc_buysell,btc_newprice)
        elif btc_wallet == False and btc_newprice > btc_prevprice*1.005 and btc_newprice*1.002 < btc_max :
            (btc_wallet,btc_prevprice,btc_max,btc_buysell) = sell_btc(btc_wallet,btc_buysell,btc_newprice,wallet)
        elif btc_wallet == True and btc_newprice < btc_min :
            btc_min = btc_newprice
        elif btc_wallet == False and btc_newprice > btc_max :
            btc_max = btc_newprice
            
        #eth bot
        if eth_wallet == True and eth_newprice*1.005 < eth_prevprice and eth_newprice > eth_min*1.0035 :
            (eth_wallet,eth_prevprive,eth_min) = buy_eth(eth_wallet,eth_buysell,eth_newprice)
        elif eth_wallet == False and eth_newprice > eth_prevprice*1.005 and eth_newprice*1.002 < eth_max :
            (eth_wallet,eth_prevprice,eth_max,eth_buysell) = sell_eth(eth_wallet,eth_buysell,eth_newprice,wallet)
        elif eth_wallet == True and eth_newprice < eth_min :
            eth_min = eth_newprice
        elif eth_wallet == False and eth_newprice > eth_max :
            eth_max = eth_newprice

        #xrp bot
        if xrp_wallet == True and xrp_newprice*1.005 < xrp_prevprice and xrp_newprice > xrp_min*1.0035 :
            (xrp_wallet,xrp_prevprive,xrp_min) = buy_xrp(xrp_wallet,xrp_buysell,xrp_newprice)
        elif xrp_wallet == False and xrp_newprice > xrp_prevprice*1.005 and xrp_newprice*1.002 < xrp_max :
            (xrp_wallet,xrp_prevprice,xrp_max,xrp_buysell) = sell_xrp(xrp_wallet,xrp_buysell,xrp_newprice,wallet)
        elif xrp_wallet == True and xrp_newprice < xrp_min :
            xrp_min = xrp_newprice
        elif xrp_wallet == False and xrp_newprice > xrp_max :
            xrp_max = xrp_newprice
        
        #ada bot
        if ada_wallet == True and ada_newprice*1.005 < ada_prevprice and ada_newprice > ada_min*1.0035 :
            (ada_wallet,ada_prevprive,ada_min) = buy_ada(ada_wallet,ada_buysell,ada_newprice)
        elif ada_wallet == False and ada_newprice > ada_prevprice*1.005 and ada_newprice*1.002 < ada_max :
            (ada_wallet,ada_prevprice,ada_max,ada_buysell) = sell_ada(ada_wallet,ada_buysell,ada_newprice,wallet)
        elif ada_wallet == True and ada_newprice < ada_min :
            ada_min = ada_newprice
        elif ada_wallet == False and ada_newprice > ada_max :
            ada_max = ada_newprice
        
        #bnb bot
        if bnb_wallet == True and bnb_newprice*1.005 < bnb_prevprice and bnb_newprice > bnb_min*1.0035 :
            (bnb_wallet,bnb_prevprive,bnb_min) = buy_bnb(bnb_wallet,bnb_buysell,bnb_newprice)
        elif bnb_wallet == False and bnb_newprice > bnb_prevprice*1.005 and bnb_newprice*1.002 < bnb_max :
            (bnb_wallet,bnb_prevprice,bnb_max,bnb_buysell) = sell_bnb(bnb_wallet,bnb_buysell,bnb_newprice,wallet)
        elif bnb_wallet == True and bnb_newprice < bnb_min :
            bnb_min = bnb_newprice
        elif bnb_wallet == False and bnb_newprice > bnb_max :
            bnb_max = bnb_newprice
        
    except KeyboardInterrupt :
        print("Code stopped !, Here is your wallet,",wallet)
        break
    
    except Exception as e:
        print('\n',e,'\n')
        time.sleep(1)
        pass
