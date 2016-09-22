#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:thread_condition.py
@time(UTC+8):16/9/17-16:26
'''

import threading, time


def func_con():
    inp = input(">>:")
    if inp == "true":
        return True
    else:
        return False


def func(i, my_con):
    print(i)
    my_con.acquire()  # 开始加锁
    my_con.wait_for(func_con)  # 等待条件为真
    print(i+100)
    my_con.release()  # 结束锁

my_con = threading.Condition()

for i in range(10):  # 在新的线程里面执行func() 方法
    t = threading.Thread(target=func, args=(i, my_con))
    t.start()

