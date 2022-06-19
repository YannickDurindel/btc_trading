#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 16:41:27 2022

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
        
        if len(btc_pastprice)> 151:
            slope = []
            for i in range(1,151):
                slope.append(btc_pastprice[-i]/btc_pastprice[-i-1])
            trend_long = (sum(slope[0:150])/150-1)*10000
            trend_middle = (sum(slope[90:150])/60-1)*10000
            trend_short = (sum(slope[138:150])/12-1)*10000
        if len(btc_pastprice)<151 and len(btc_pastprice)>61 :
            slope = []
            for i in range(1,61):
                slope.append(btc_pastprice[-i]/btc_pastprice[-i-1])
            trend_middle = (sum(slope[0:60])/60-1)*10000
            trend_short = (sum(slope[48:60])/12-1)*10000
        if len(btc_pastprice)<151 and len(btc_pastprice)>12 :
            slope = []
            for i in range(1,13):
                slope.append(btc_pastprice[-i]/btc_pastprice[-i-1])
            trend_short = (sum(slope[0:12])/12-1)*10000
            
        if btc_newprice > btc_prevprice*1.005 and  btc_wallet == False and trend_short < 2 and trend_middle < 0.7 and trend_long < 0.3 :
            #binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
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
                
        elif btc_newprice*1.005 < btc_max and btc_wallet == True and trend_short > -2 and trend_middle > -0.7 and trend_long > -0.3 :
            #binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='BUY',quantity=btc_buysell)
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
                
        elif btc_newprice*1.04 < btc_prevprice and btc_wallet == False:
            #binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
            print("sell, CRISIS !!!")
            message += "sell,CRISIS !!!, wallet = "+str(getwallet("USDT"))+", the low gap was "+str(btc_prevprice/btc_min)+", btc price = "+str(btc_newprice)+"\n"
            btc_prevprice = btc_newprice
            btc_max = btc_newprice
            btc_wallet = True
            btc_buysell = round((wallet-1)*leverage/btc_newprice,3)
        time.sleep(15)

    except Exception as e:
        e = e
        time.sleep(1)
        pass

    except KeyboardInterrupt:
        if btc_wallet == False:
            while btc_newprice > btc_prevprice and trend_short < 2 and trend_middle < 0.7 and trend_long < 0.3 : 
                #binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
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