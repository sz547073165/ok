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
size = 5
changeValue = 0
thresholdValue = 0.01
isSend = False

while True:
    kLine = okexSpot.kLine(symbol,typeStr,size)
    if not kLine:
        continue
    print(kLine)
    kLineLast = kLine[-1]
    kLineEarly = kLine[-2]
    
    timestampLast = kLineLast[0]/1000
    high = kLineLast[2]
    low = kLineLast[3]
    priceLast = kLineLast[4]
    priceEarly = kLineEarly[4]
    change = (float(priceLast) / float(priceEarly)) - 1
    
    subject = 'BTC_USDT'
    content = '<html>'
    content += '<p>%s</p>' % misc.getTimeStr()
    
    if high > highValue:
        highValue = high
        misc.setConfigKeyValue('config.ini', 'global', 'high', high)
        content += '<p style="font-weight: bold; color: red;">最高价：%s</p>' % high
        subject += '“最高价”'
        isSend = True
    if low < lowValue:
        lowValue = low
        misc.setConfigKeyValue('config.ini', 'global', 'low', low)
        content += '<p style="font-weight: bold; color: green;">最低价：%s</p>' % low
        subject += '“最低价”'
        isSend = True
    if abs(change) > thresholdValue:
        if not change == changeValue:
            changeValue = change
            if change > 0:
                value = '+' + str(round(change * 100, 4)) + '%'
            else:
                value = str(round(change * 100, 4)) + '%'
            content += '<p>一小时内涨跌幅度：%s</p>' % value
            subject += '“涨跌幅”'
            isSend = True
            ma5Value = misc.getMALine(kLine, 5)[-1]
            if float(kLine[-1][4]) > ma5Value:
                content += '<p>当前价格%s > 五日均线（%s周期)%s</p>' % (priceLast, typeStr, ma5Value)
            if float(kLine[-1][4]) < ma5Value:
                content += '<p>当前价格%s < 五日均线（%s周期)%s</p>' % (priceLast, typeStr, ma5Value)
            if float(kLine[-1][4]) == ma5Value:
                content += '<p>当前价格%s = 五日均线（%s周期)%s</p>' % (priceLast, typeStr, ma5Value)
    content += '</html>'
    subject += '报告'
    
    if isSend:
        misc.sendEmail(mailHost, mailUser, mailPass, receivers, subject, content)
        isSend = False
        time.sleep(60)
        continue
    time.sleep(30)