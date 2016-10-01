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


def func(i):
    time.sleep(1)
    print(i)

for i in range(10):
    p = Process(target=func, args=(i, ))
    # p.daemon = True
    p.start()
    # p.join()
print('end of main process ---------')
