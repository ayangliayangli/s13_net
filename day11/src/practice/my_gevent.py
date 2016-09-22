#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:my_gevent.py
@time(UTC+8):16/9/18-18:38
'''

import requests, gevent


def func(arg):
    print("start request {}".format(arg))
    resp = requests.get(arg)
    data = resp.text
    print('site: {} len: {}'.format(arg, len(data)))


gevent.joinall([
    gevent.spawn(func, 'http://www.bw.com'),
    gevent.spawn(func, 'http://www.baidu.com'),
    gevent.spawn(func, 'http://www.sina.com'),
    gevent.spawn(func, 'http://www.qq.com'),
])


