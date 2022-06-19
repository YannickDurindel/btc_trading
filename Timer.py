#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 09:04:52 2022

@author: yannick
"""

import time

def HoldOn(t0,dt):
    t1 = time.time()
    print(t0)
    print(t1)
    while t0 + dt > t1 :
        t1 = time.time()

t0 = time.time()
time.sleep(2)
HoldOn(t0,1)
print("succed")