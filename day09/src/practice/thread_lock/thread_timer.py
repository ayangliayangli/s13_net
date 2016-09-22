#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:thread_timer.py
@time(UTC+8):16/9/17-16:45
'''

from threading import Timer


def func():
    print("hello world in sub process")

t = Timer(2, func)
print("start in main process .. ")
t.start()