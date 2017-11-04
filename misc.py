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

def buildSign(params, secretKey):
    sign = ''
    for key in sorted(params.keys()):
        sign += key + '=' + str(params[key]) + '&'
    data = sign + 'secret_key=' + secretKey
    return hashlib.md5(data.encode('utf-8')).hexdigest().upper()

def httpGet(url, resource, params=''):
    conn = http.client.HTTPSConnection(url, timeout=10)
    conn.request('GET', resource + '?' + params)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    return json.loads(data)

def httpPost(url, resource, params):
    headers = {
            'Content-type': 'application/x-www-form-urlencoded'
    }
    conn = http.client.HTTPSConnection(url, timeout=10)
    temp_params = urllib.parse.urlencode(params)
    conn.request('POST', resource, temp_params, headers)
    response = conn.getresponse()
    data = response.read().decode('utf-8')
    params.clear()
    conn.close()
    return data
