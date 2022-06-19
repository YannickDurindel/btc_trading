#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 10:16:52 2022

@author: yannick
"""

from binance.client import Client
import time
from csv import writer
import csv
import smtplib, ssl

api_key = "wsWyaiQ0dlAWj4eFE4AdvbOtmtnj2sKTMv3f53CRy6NsGIBdTZy3ZxUggAMOZr1f"
api_secret = "AlBOMFfj60b6xjWldKv6Vex5l4y4REqrU2e17XIbeRmAJVZ4Jakh7CdgSu5U5mid"
binance_client = Client(api_key, api_secret)
leverage = 20
t_init = time.time()
with open('performances.csv', 'r') as P:
  perf = csv.reader(P)
  Perf = list(perf)
  wallet = float(Perf[len(Perf)-1][1])
  t0 = float(Perf[len(Perf)-1][0])
  P.close()
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "yannick.durindel@gmail.com"  # Enter your address
receiver_email = "yannick.durindel@gmail.com"  # Enter receiver address
password = "Pyfgcrl8!"
message = ""
  
def getwallet(currency):
    account_info = binance_client.futures_account()
    av_balance = None
    for asset in account_info["assets"]:
        if asset["asset"] == currency:
            av_balance = float(asset["marginBalance"])
    return av_balance
wallet = getwallet("USDT")
walletseuil = wallet

btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
btc_prevprice = btc_newprice
btc_wallet = True
binance_client.futures_change_leverage(symbol='BTCUSDT', leverage=leverage)
btc_buysell = round((wallet-10)*leverage/btc_newprice,3)
print("TO THE MOON !!!\n")

while True :
    try :
        btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
        if wallet > walletseuil*2:
            context = ssl.create_default_context()
            message = "you just doubled your networh, you earned"+str(wallet-walletseuil)+", your wallet ="+str(wallet)
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, password)
                server.sendmail(sender_email, receiver_email, message)
            walletseuil = getwallet("USDT")
        
        # btc bot
        if btc_newprice > btc_prevprice*1.0015 and btc_wallet == False:
            wallet = getwallet("USDT")
            binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
            btc_prevprice = btc_newprice
            btc_wallet = True
            print("sell btc, btc_price =",btc_newprice,"wallet =",getwallet("USDT"),'lowering to',btc_newprice*1.0015,'\n')
            with open('performances.csv', 'a', newline='') as P:  
                Perf = writer(P)
                Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice])  
                P.close()
            btc_buysell = round((wallet-10)*leverage/btc_newprice,3)
        elif btc_newprice*1.0015 < btc_prevprice and btc_wallet == True:
            time.sleep(60)
            btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
            if btc_newprice*1.002 < btc_prevprice:
                time.sleep(180)
                btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
                if btc_newprice*1.005< btc_newprice:
                    time.sleep(180)
                    btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
                    if btc_newprice*1.008< btc_newprice:
                        time.sleep(180)
                        btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
            if btc_newprice*1.0015 < btc_prevprice :
                wallet = getwallet("USDT")
                binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='BUY',quantity=btc_buysell)
                btc_prevprice = btc_newprice
                print("buy btc, btc_price =",btc_newprice,'rising to',btc_newprice*1.0015,'\n')
                btc_wallet = False
                crisis_counter = 0
                with open('performances.csv', 'a', newline='') as P:  
                    Perf = writer(P)
                    Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice])  
                    P.close()
        elif btc_newprice > btc_prevprice and btc_wallet == True:
            #time.sleep(5)
            btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
            if btc_newprice > btc_prevprice : 
                btc_prevprice = btc_newprice
        elif btc_newprice*1.02 < btc_prevprice and btc_wallet == False:
            print("We've been fucked ... but it could have been much worse !\n")
            wallet = getwallet("USDT")
            binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
            btc_prevprice = btc_newprice
            print("sell btc, btc_price =",btc_newprice,"wallet =",getwallet("USDT"),'\n')    
            btc_wallet = True
            with open('performances.csv', 'a', newline='') as P:  
                Perf = writer(P)
                Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice])  
                P.close()
            btc_buysell = round(100*leverage/btc_prevprice,3)
            time.sleep(300)
            
    except Exception as e:
        print("Error:", e,'\n')
        time.sleep(5)
        pass
        
    except KeyboardInterrupt:
        loss = wallet * (btc_newprice/btc_prevprice-1)*leverage
        print ("if you quit, you'll loose",loss,"$ equals to a malus of",(wallet+loss)/wallet-1)
        print("do you want to quit now ?")
        wait = "n" #input("y/n ?")
    
        if wait == "y":
            if btc_wallet==False:
                wallet = getwallet("USDT")
                binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
                btc_prevprice = btc_newprice
                print("sell btc, btc_price =",btc_newprice,"wallet =",getwallet("USDT"),'\n')    
                btc_wallet = True
                with open('performances.csv', 'a', newline='') as P:  
                    Perf = writer(P)
                    Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice])  
                    P.close()
        else :
            print("You made the good choice, but you'll have to wait a bit")
            print("Ctr+C si tu veux l'arreter, mais que en urgence, sinon tu peux juste fermer l'écran pour ne pas l'arreter")
            while btc_wallet == False :
                try :
                    btc_newprice = float(binance_client.futures_symbol_ticker(symbol='BTCUSDT')['price'])
                    
                    if btc_newprice > btc_prevprice*1.0005 and btc_wallet == False:
                        wallet = getwallet("USDT")
                        binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
                        btc_prevprice = btc_newprice
                        print("sell btc, btc_price =",btc_newprice,"wallet =",getwallet("USDT"),'\n')    
                        btc_wallet = True
                        with open('performances.csv', 'a', newline='') as P:  
                            Perf = writer(P)
                            Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice])  
                            P.close()
                    
                except Exception as e:
                    print("Error:", e,'\n')
                    time.sleep(5)
                    pass
                
                except KeyboardInterrupt :
                    if btc_wallet==False:
                        wallet = getwallet("USDT")
                        binance_client.futures_create_order(symbol='BTCUSDT',type='MARKET',side='SELL',quantity=btc_buysell)
                        btc_prevprice = btc_newprice
                        print("sell btc, btc_price =",btc_newprice,"wallet =",getwallet("USDT"),'\n')    
                        btc_wallet = True
                        with open('performances.csv', 'a', newline='') as P:  
                            Perf = writer(P)
                            Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice])  
                            P.close()
                            
        
        tf = time.time()
        print("it took",tf-t0,"to raise",getwallet("USDT")-78,"%")
        with open('performances.csv', 'a', newline='') as P:  
            Perf = writer(P)
            Perf.writerow([(time.time()-t_init)+t0,wallet,btc_newprice])  
            P.close()
        break
