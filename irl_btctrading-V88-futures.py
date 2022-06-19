#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 14:20:17 2022

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
btc_buysell = round((wallet-1)*leverage/btc_newprice,3)
btc_pastprice = []

while True :
    try :
        btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
        wallet = getwallet("USDT")
        btc_pastprice.append(btc_newprice)
        if len(btc_pastprice)> 30:
            slope = []
            for i in range(1,31):
                slope.append((btc_pastprice[-i]/btc_pastprice[-i-1]-1)*10000)
            trend = sum(slope)/len(slope)
        if btc_newprice > btc_prevprice*1.005 and trend > -0.75 :
            binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
            print("sell")
            message += "sell, wallet = "+str(getwallet("USDT"))+", the low gap was "+str(btc_prevprice/btc_min)+", btc price = "+str(btc_newprice)+"\n"
            btc_prevprice = btc_newprice
            btc_max = btc_newprice
            btc_wallet = True
            btc_buysell = round((wallet-1)*leverage/btc_newprice,3)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
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
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
        elif btc_newprice > btc_max :
            btc_max = btc_newprice
            if btc_wallet == True :
                tbuy = time.time()
        elif btc_newprice < btc_min  :
            btc_min = btc_newprice
            if btc_wallet == False :
                tsell = time.time()
        elif btc_newprice*1.04 < btc_prevprice and btc_wallet == False:
            binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
            print("sell")
            message += "sell, wallet = "+str(getwallet("USDT"))+", the low gap was "+str(btc_prevprice/btc_min)+", btc price = "+str(btc_newprice)+"\n"
            btc_prevprice = btc_newprice
            btc_max = btc_newprice
            btc_wallet = True
            btc_buysell = round((wallet-1)*leverage/btc_newprice,3)
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