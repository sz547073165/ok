#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 11:09:11 2017

@author: Marco
"""
#客户端调用，用于查看API返回结果

from okexSpotAPI import OkexSpot
from person import apikey, secretkey

#初始化url
okexRESTURL = 'www.okcoin.com'   #请求注意：国内账号需要 修改为 www.okcoin.cn  

#现货API
okexSpot = OkexSpot(okexRESTURL,apikey,secretkey)

print (u' 现货行情 ')
print (okexSpot.ticker('btc_usd'))

print (u' 现货深度 ')
print (okexSpot.depth('btc_usd'))

#print (u' 现货历史交易信息 ')
#print (okexSpot.trades())

#print (u' 用户现货账户信息 ')
#print (okexSpot.userinfo())

#print (u' 现货下单 ')
#print (okexSpot.trade('ltc_usd','buy','0.1','0.2'))

#print (u' 现货批量下单 ')
#print (okexSpot.batchTrade('ltc_usd','buy','[{price:0.1,amount:0.2},{price:0.1,amount:0.2}]'))

#print (u' 现货取消订单 ')
#print (okexSpot.cancelOrder('ltc_usd','18243073'))

#print (u' 现货订单信息查询 ')
#print (okexSpot.orderinfo('ltc_usd','18243644'))

#print (u' 现货批量订单信息查询 ')
#print (okexSpot.ordersinfo('ltc_usd','18243800,18243801,18243644','0'))

#print (u' 现货历史订单信息查询 ')
#print (okexSpot.orderHistory('ltc_usd','0','1','2'))
