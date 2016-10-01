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
from multiprocessing import Array


def func(i, li):
    time.sleep(1)
    li[i] = i + 100
    for item in li:
        print(item)
    print('subprocess: {} end ------'.format(i))


li = Array('i', 10)  # specified type and length

for i in range(10):
    p = Process(target=func, args=(i, li, ))
    # p.daemon = True
    p.start()

print('end of main process ----- ')



