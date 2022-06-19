#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 19:56:18 2021

@author: yannick
"""

# This is my btc.py script.
import requests
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()
print(data["bpi"]["EUR"]["rate"])
#bitcoin_new = data["bpi"]["USD"]["rate"]
#print(bitcoin_new)