#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 10:14:01 2022

@author: yannick
"""

from csv import writer
  
list_data=[0,0,27,39000]
  

with open('performances.csv', 'a', newline='') as P:  
    Perf = writer(P)
    Perf.writerow(list_data)  
    P.close()