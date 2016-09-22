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


def f(lock, i):
    global g_num

    lock.acquire()  # lock
    g_num -= 1
    time.sleep(1)  # 模拟需要很长的时间
    print(g_num, i)
    lock.release()  # unlock

my_semaphore = threading.BoundedSemaphore(3)  # 同时允许3个线程访问代码块


for i in range(20):
    t = threading.Thread(target=f, args=(my_semaphore,i, ))
    t.start()
