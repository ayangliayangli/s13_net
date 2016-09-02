#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:test.py
@time(UTC+8):16/8/20-14:20
'''


flag = True

if True:
    flag = False
    print("in_if: {}".format(flag))   # false
print("in_if: {}".format(flag))       # fale
# 在流程控制中使用的 使用的变量就是全局变量


def f():
    flag = False
    print("in_if: {}".format(flag))     # False
flag = True
f()
print("in_if: {}".format(flag))          # True
# 在函数中定义的变量是本地变量,和全局的没有关系,   shadow var
