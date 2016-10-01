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
from multiprocessing import Manager


def func(i, dic):
    time.sleep(1)
    dic[i] = i + 100
    print(dic.values())
    # print(q.qsize())  # 这里报错,不能使用qsize() 这个方法,搞笑


dic = Manager().dict()

for i in range(10):
    p = Process(target=func, args=(i, dic, ))
    # p.daemon = True
    p.start()

p.join()  # main wait for sub peocess end , because var dic
print('end of main process ----- ')



