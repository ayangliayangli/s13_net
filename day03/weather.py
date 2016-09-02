#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:weather.py
@time(UTC+8):16/8/21-14:04
'''


import json, requests

s = 'http://wthrcdn.etouch.cn/weather_mini?city=' + "深圳"
response = requests.get(s)
response.encoding="utf-8"
print(response.text)