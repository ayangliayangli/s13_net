#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:my_process.py
@time(UTC+8):16/9/18-14:28
'''

import time
from multiprocessing import Process
from multiprocessing import queues
import multiprocessing


def func(i, q):
    time.sleep(1)
    q.put(i)
    # print(q.qsize())  # 这里报错,不能使用qsize() 这个方法,搞笑


q = queues.Queue(20, ctx=multiprocessing)  # use queues.Queue() share data with sub process


for i in range(10):
    p = Process(target=func, args=(i, q, ))
    # p.daemon = True
    p.start()


p.join()  # wait all sub process end
for i in range(10):
    print(q.get())
print('end of main process ---------')
