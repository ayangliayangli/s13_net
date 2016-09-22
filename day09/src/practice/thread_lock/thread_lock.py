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


def f(lock):
    global g_num

    lock.acquire()  # lock
    g_num -= 1
    time.sleep(1)  # 模拟需要很长的时间
    print(g_num)
    lock.release()  # unlock

lock = threading.Lock()
rlock = threading.RLock()  # 这个和lock是一样的,只是可以循环嵌套的给变量加锁


for i in range(10):
    t = threading.Thread(target=f, args=(lock, ))
    t.start()
