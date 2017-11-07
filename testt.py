#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:04:21 2017

@author: Marco
"""

from okexSpotAPI import OkexSpot
from person import apikey, secretkey, mailPass
import misc

#现货API
okexSpot = OkexSpot(apikey,secretkey)
symbol = 'btc_usdt'
typeStr = '1hour'
size = 10

kLine = okexSpot.kLine(symbol,typeStr,size)
print(kLine)

def getMA5Line(kLine):
    if len(kLine) < 5:
        return
    ma5Line = []
    for i in range(len(kLine)-4):
        closePriceSum = 0
        for j in range(i, i + 5):
            closePriceSum += float(kLine[j][4])
        ma5Line.append(round(closePriceSum / 5, 4))
    return ma5Line

print(getMA5Line(kLine))
print(getMA5Line(kLine)[-1])

ma5Value = misc.getMA5Line(kLine)[-1]
if float(kLine[-1][4]) > ma5Value:
    print('<p>当前价格%s > 五日均线（%s周期)%s</p>' % (111, 222, 333))
if float(kLine[-1][4]) < ma5Value:
    print('收盘价 < 五日均线（1小时周期)')
if float(kLine[-1][4]) == ma5Value:
    print('收盘价 = 五日均线（1小时周期)')