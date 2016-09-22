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


def func(i, my_con):
    print(i)
    my_con.acquire()  # 开始加锁
    my_con.wait()  # 等待条件为真
    print(i+100)
    my_con.release()  # 结束锁

my_con = threading.Condition()

for i in range(10):  # 在  新的线程  里面执行func() 方法
    t = threading.Thread(target=func, args=(i, my_con))
    t.start()

while True:
    inp = input(">>:")
    if inp.isnumeric():
        if inp == "q":
            break
        else:
            my_con.acquire()
            my_con.notify(int(inp))  # 条件满足,放通inp个线程
            my_con.release()
    else:
        continue