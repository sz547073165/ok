#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 23:56:25 2017

@author: Marco
"""

from okexSpotAPI import OkexSpot
from person import apikey, secretkey, mailPass
import misc
import time

mailHost = misc.getConfigKeyValueByKeyName('config.ini', 'mail', 'mailHost')
mailUser = misc.getConfigKeyValueByKeyName('config.ini', 'mail', 'mailUser')
receivers = misc.getConfigKeyValueByKeyName('config.ini', 'mail', 'receivers').split(',')
highValue = misc.getConfigKeyValueByKeyName('config.ini', 'global', 'high')
lowValue = misc.getConfigKeyValueByKeyName('config.ini', 'global', 'low')
#现货API
okexSpot = OkexSpot(apikey,secretkey)
symbol = 'btc_usdt'
typeStr = '1hour'
size = 2
changeValue = 0
thresholdValue = 0.01
isSend = False

while True:
    kLine = okexSpot.kLine(symbol,typeStr,size)
    print(kLine)
    kLineLast = kLine[1]
    kLineEarly = kLine[0]
    
    timestampLast = kLineLast[0]/1000
    high = kLineLast[2]
    low = kLineLast[3]
    priceLast = kLineLast[4]
    priceEarly = kLineEarly[4]
    change = (float(priceLast) / float(priceEarly)) - 1
    
    content = '<html>'
    
    if high > highValue:
        highValue = high
        misc.setConfigKeyValue('config.ini', 'global', 'high', high)
        content += '<p style="font-weight: bold; color: red;">最高价：%s</p>' % high
        isSend = True
    if low < lowValue:
        lowValue = low
        misc.setConfigKeyValue('config.ini', 'global', 'low', low)
        content += '<p style="font-weight: bold; color: green;">最低价：%s</p>' % low
        isSend = True
    print(change)
    print(changeValue)
    if abs(change) > thresholdValue:
        if not change == changeValue:
            changeValue = change
            content += '<p>一小时内涨跌幅度：%s</p>' % (str(round(change * 100, 4))+'%')
            isSend = True
    content += '</html>'
    if isSend:
        misc.sendEmail(mailHost, mailUser, mailPass, receivers, 'BTC_USDT最新报告', content)
        isSend = False
        time.sleep(60)
        continue
    time.sleep(30)