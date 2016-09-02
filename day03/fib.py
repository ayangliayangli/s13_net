#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:fib.py
@time(UTC+8):16/8/21-11:25
'''


def fib(n):
    if n == 2:
        return 2+1
    return fib(n-1)+n

ret = fib(5)
print(ret)