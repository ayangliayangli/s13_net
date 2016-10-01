#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:process_pool.py
@time(UTC+8):16/9/18-15:26
'''

from multiprocessing import Pool
import time


def f(arg):
    time.sleep(1)
    print(arg)

pool = Pool(5)

for i in range(30):  # 模拟又30个任务
    pool.apply_async(func=f, args=(i, ))

pool.close()  # 结束所有的任务
# pool.terminate()  # 结束进程当前执行的任务
pool.join()
print('end of main process ------')
