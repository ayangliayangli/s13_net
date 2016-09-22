#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:thread_pool.py
@time(UTC+8):16/9/17-17:09
'''

import threading, time
import queue


class ThreadPool():
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self._q = queue.Queue(maxsize)
        for i in range(maxsize):
            self._q.put(threading.Thread)  # 放maxsize 个Thread的类名到 _q 中

    def get_thread(self):
        return self._q.get()

    def add_thread(self):
        self._q.put(threading.Thread)


def func(i, pool):
    print(i)
    time.sleep(3)
    pool.add_thread()

pool = ThreadPool(5)  # create a pool object , maxsize of pool is 5
for i in range(21):
    t = pool.get_thread()(target=func, args=(i, pool))
    t.start()

