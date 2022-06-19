#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 20:08:12 2022

@author: yannick
"""

from binance.client import Client
import time
import smtplib, ssl

api_key = "wsWyaiQ0dlAWj4eFE4AdvbOtmtnj2sKTMv3f53CRy6NsGIBdTZy3ZxUggAMOZr1f"
api_secret = "AlBOMFfj60b6xjWldKv6Vex5l4y4REqrU2e17XIbeRmAJVZ4Jakh7CdgSu5U5mid"
binance_client = Client(api_key, api_secret)
btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
btc_prevprice = btc_newprice
btc_min = btc_newprice
btc_max = btc_newprice
leverage = 20
btc_wallet = True
tbuy = time.time()
tsell = time.time()
port = 465  
smtp_server = "smtp.gmail.com"
sender_email = "yannick.durindel@gmail.com"  
receiver_email = "yannick.durindel@gmail.com"
password = "Pyfgcrl8!"
message = ""
tmail = time.time()
print("TO THE MOON !!!\n")
def getwallet(currency):
    account_info = binance_client.futures_account()
    av_balance = None
    for asset in account_info["assets"]:
        if asset["asset"] == currency:
            av_balance = float(asset["marginBalance"])
    return av_balance
wallet = getwallet("USDT")
binance_client.futures_change_leverage(symbol='BTCUSDT', leverage=leverage)
btc_buysell = round((wallet/2)*leverage/btc_newprice,3)

while True :
    try :
        if tmail+3600*12 > time.time():
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            tmail = time.time()
        btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
        wallet = getwallet("USDT")
        if btc_newprice > btc_prevprice*1.005 and btc_wallet == False:
            if time.time()-tsell < 1200 :
                tsell = time.time()
                btc_max = btc_newprice
                while time.time() < tsell+1200 :
                    btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
                    if btc_newprice > btc_max :
                        btc_max = btc_newprice
                    elif btc_newprice <= btc_prevprice*1.005 :
                        tsell = 0
                    elif btc_newprice*1.002 < btc_max :
                        tsell =0
            binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
            print("sell")
            message += "sell, wallet = "+str(getwallet("USDT"))+", the low gap was "+str(btc_prevprice/btc_min)+", btc price = "+str(btc_newprice)+"\n"
            btc_prevprice = btc_newprice
            btc_max = btc_newprice
            btc_wallet = True
            btc_buysell = round((wallet/2)*leverage/btc_newprice,3)
        elif btc_newprice*1.005 < btc_max and btc_wallet == True:
            if time.time()-tbuy < 1200 :
                tbuy = time.time()
                btc_min = btc_newprice
                while time.time() < tbuy+1200 :
                    btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
                    if btc_newprice < btc_min :
                        btc_min = btc_newprice
                    elif btc_newprice*1.005 >= btc_prevprice :
                        tbuy = 0
                    elif btc_newprice > btc_min*1.002 :
                        tbuy =0
            binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='BUY',quantity=btc_buysell)
            print("buy")
            message += "buy, the high gap was "+str(btc_max/btc_prevprice)+", btc price = "+str(btc_newprice)+"\n"
            btc_prevprice = btc_newprice
            btc_wallet = False
            btc_min = btc_newprice
        elif btc_newprice > btc_max :
            btc_max = btc_newprice
            if btc_wallet == True :
                tbuy = time.time()
        elif btc_newprice < btc_min  :
            btc_min = btc_newprice
            if btc_wallet == False :
                tsell = time.time()
        elif btc_newprice*1.015 < btc_prevprice and btc_wallet == False:
            binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
            print("sell")
            message += "sell, wallet = "+str(getwallet("USDT"))+", the low gap was "+str(btc_prevprice/btc_min)+", btc price = "+str(btc_newprice)+"\n"
            btc_prevprice = btc_newprice
            btc_max = btc_newprice
            btc_wallet = True
            btc_buysell = round((wallet/2)*leverage/btc_newprice,3)
        time.sleep(5)

    except Exception as e:
        time.sleep(1)
        pass

    except KeyboardInterrupt:
        if btc_wallet == False:
            binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
            print("sell")
            message += "sell, wallet = "+str(getwallet("USDT"))+", the low gap was "+str(btc_prevprice/btc_min)+", btc price = "+str(btc_newprice)+"\n"
            btc_prevprice = btc_newprice
            btc_max = btc_newprice
            btc_wallet = True
            btc_buysell = round((wallet/2)*leverage/btc_newprice,3)
        break
    
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)