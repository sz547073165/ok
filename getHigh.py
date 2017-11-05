#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 10:38:01 2017

@author: Marco
"""

from person import apikey ,secretkey, mailPass
import misc
from okexSpotAPI import OkexSpot
import time

mailHost = misc.getConfigKeyValueByKeyName('config.ini', 'mail', 'mailHost')
mailUser = misc.getConfigKeyValueByKeyName('config.ini', 'mail', 'mailUser')
receivers = misc.getConfigKeyValueByKeyName('config.ini', 'mail', 'receivers').split(',')

okexSpot = OkexSpot(apikey, secretkey)
symbol = 'btc_usdt'

highValue = misc.getConfigKeyValueByKeyName('config.ini', 'ticker', 'high')

while True:
    ticker = okexSpot.ticker(symbol)
    high = ticker['ticker']['high']
    print(ticker)
    if high > highValue:
        content = '<html>'
        content += '<p>返回数据时服务器时间：%s</p>' % misc.getTimeStrWithUnixTimestamp(int(ticker['date']))
        content += '<p>买一价：%s</p>' % ticker['ticker']['buy']
        content += '<p style="font-weight: bold; color: red;">最高价：%s</p>' % ticker['ticker']['high']
        content += '<p>最新成交价：%s</p>' % ticker['ticker']['last']
        content += '<p>最低价：%s</p>' % ticker['ticker']['low']
        content += '<p>卖一价：%s</p>' % ticker['ticker']['sell']
        content += '<p>成交量(最近的24小时)：%s</p>' % ticker['ticker']['vol']
        content += '</html>'
        highValue = high
        misc.setConfigKeyValue('config.ini', 'ticker', 'high', high)
        misc.sendEmail(mailHost, mailUser, mailPass, receivers, 'BTC_USDT最新最高价', content)
    time.sleep(15)