#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:04:21 2017

@author: Marco
"""

from okexSpotAPI import OkexSpot
from person import apikey, secretkey, mailPass
import misc

okexSpot = OkexSpot(apikey,secretkey)
symbol = 'btc_usdt'
typeStr = '1hour'
size = 24

kLine = okexSpot.kLine(symbol,typeStr,size)
ma5 = misc.getMALine(kLine)
ma5Slope = misc.getSlope(ma5)

print('MA5：',ma5)
print('MA5 slope：',ma5Slope)
print(len(ma5))
print(len(ma5Slope))