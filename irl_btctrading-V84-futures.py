#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 10:46:39 2022

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
btc_wallet = True
tbuy = time.time()
tsell = time.time()
port = 465  
smtp_server = "smtp.gmail.com"
sender_email = "@gmail.com"  
receiver_email = "@gmail.com"
password = ""
message = ""
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
            #sell
            print("sell, wallet =",getwallet("USDT"),"the low gap was",btc_prevprice/btc_min,"\n")
            message += "sell, wallet = "+str(getwallet("USDT"))+", the low gap was "+str(btc_prevprice/btc_min)+"\n"
            btc_prevprice = btc_newprice
            btc_max = btc_newprice
            btc_wallet = True
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
            #buy
            print("buy, the high gap was",btc_max/btc_prevprice,"\n")
            message += "buy, the high gap was "+str(btc_max/btc_prevprice)+"\n"
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
            #sell            
            print("sell, wallet =",getwallet("USDT"),"the low gap was",btc_prevprice/btc_min,"\n")
            message += "sell, wallet = "+str(getwallet("USDT"))+", the low gap was "+str(btc_prevprice/btc_min)+"\n"
            btc_prevprice = btc_newprice
            btc_max = btc_newprice
            btc_wallet = True
        time.sleep(5)

    except Exception as e:
        #print("Error:", e,'\n')
        e+=" "
        time.sleep(1)
        pass

    except KeyboardInterrupt:
        if btc_wallet == False:
            print("sell, wallet =",getwallet("USDT"),"the low gap was",btc_prevprice/btc_min,"\n")
            message += "sell, wallet = "+str(getwallet("USDT"))+", the low gap was "+str(btc_prevprice/btc_min)+"\n"
            btc_prevprice = btc_newprice
            btc_max = btc_newprice
            btc_wallet = True
        break
    
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
