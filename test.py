#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 23:56:25 2017

@author: Marco
"""

import misc

print(misc.getConfigKeyValueByKeyName('config.ini', 'mail', 'mailHost'))
print(misc.getConfigKeyValueByKeyName('config.ini', 'mail', 'mailUser'))
print(misc.getConfigKeyValueByKeyName('config.ini', 'mail', 'receivers').split(','))