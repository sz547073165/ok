#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 10:38:01 2017

@author: Marco
"""
#用于进行http请求，以及md5加密，生成签名的工具

import hashlib
import http.client
import json
import urllib
import configparser
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time

'''签名'''
def buildSign(params, secretKey):
    sign = ''
    for key in sorted(params.keys()):
        sign += key + '=' + str(params[key]) + '&'
    data = sign + 'secret_key=' + secretKey
    return hashlib.md5(data.encode('utf-8')).hexdigest().upper()

'''get请求'''
def httpGet(url, resource, params=''):
    conn = http.client.HTTPSConnection(url, timeout=10)
    try:
        conn.request('GET', resource + '?' + params)
    except:
        return
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    return json.loads(data)

'''post请求'''
def httpPost(url, resource, params):
    headers = {
            'Content-type': 'application/x-www-form-urlencoded'
    }
    conn = http.client.HTTPSConnection(url, timeout=10)
    temp_params = urllib.parse.urlencode(params)
    try:
        conn.request('POST', resource, temp_params, headers)
    except:
        return
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    params.clear()
    conn.close()
    return data

'''读取配置文件的key所对应的value'''
def getConfigKeyValueByKeyName(fileName, section, keyName):
    conf = configparser.ConfigParser()
    conf.read(fileName, 'utf-8')
    keyValue = conf.get(section, keyName)
    if keyValue:
        return keyValue
    else:
        return

'''设置keyName和keyValue到配置文件，比较粗糙，暂时用try、catch检查'''
def setConfigKeyValue(fileName, section, keyName, keyValue):
    conf = configparser.ConfigParser()
    conf.read(fileName, 'utf-8')
    try:
        conf.add_section(section)
    except:
        pass
    conf.set(section, keyName, keyValue)
    conf.write(open(fileName,'w'))

'''发送邮件'''
def sendEmail(mailHost, mailUser, mailPass, receivers, subject, content):
    try:
        email_client = smtplib.SMTP(mailHost, 25)
        email_client.login(mailUser, mailPass)
        # create msg
        msg = MIMEText(content, 'HTML', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')  # subject
        msg['From'] = mailUser
        msg['To'] = ','.join(receivers)
        email_client.sendmail(mailUser, receivers, msg.as_string())
        print('邮件发送成功，目标：%s' % receivers)
    except Exception as e:
        print('邮件发送失败，原因：%s' % e)
    finally:
        email_client.quit()

'''获取当前时间'''
def getTimeStr():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

'''获取当前时间'''
def getTimeStrWithUnixTimestamp(unixTimestamp):
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(unixTimestamp))

'''获取均线，默认获取五日均线'''
def getMALine(kLine, typeStr=5):
    if len(kLine) < typeStr:
        return
    ma5Line = []
    for i in range(len(kLine)-typeStr+1):
        closePriceSum = 0
        for j in range(i, i + typeStr):
            closePriceSum += float(kLine[j][typeStr-1])
        ma5Line.append(round(closePriceSum / typeStr, 4))
    return ma5Line

'''获取斜率'''
def getSlope(kLine):
    if len(kLine) < 2:
        return
    slope = []
    for i in range(len(kLine)-1):
        slope.append(kLine[i+1]-kLine[i])
    return slope