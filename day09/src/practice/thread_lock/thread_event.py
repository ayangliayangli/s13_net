#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:thread_lock.py
@time(UTC+8):16/9/17-15:12
'''

import time, threading

g_num = 10


def f(my_event, i):

    print('pre---', i)
    my_event.wait()  # 让司机知道这里有红路灯了
    print('after---', i+100)


my_event = threading.Event()


for i in range(10):
    t = threading.Thread(target=f, args=(my_event,i, ))
    t.start()

my_event.clear()  # 红灯
time.sleep(5)
my_event.set()  # 绿灯

