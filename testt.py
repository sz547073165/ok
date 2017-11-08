#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 11:04:21 2017

@author: Marco
"""

from okexSpotAPI import OkexSpot
from person import apikey, secretkey, mailPass
import misc

aaa = misc.httpGet('localhost:8080','/api/v1/tickeeeer.do')
print(aaa)
    