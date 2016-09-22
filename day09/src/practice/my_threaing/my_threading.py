#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:my_threading.py
@time(UTC+8):16/9/16-21:31
'''


import threading
import time


def f(i):
    time.sleep(5)
    print(i)


def test_normal():
    print('{:-^50}'.format("normal"))
    for i in range(10):
        f(i)


def test_threading():
    print('{:-^50}'.format("threading"))
    for i in range(10):
        t = threading.Thread(target=f, args=(i,))
        t.start()


def test_threading_setDaemon():

    print("---main---start")
    t = threading.Thread(target=f, args=(5,))
    t.setDaemon(True)  # 主进程结束后,不等子线程就结束
    t.start()
    print("---main---end")


def test_threading_join():
    print("---main---start")
    t = threading.Thread(target=f, args=(5,))
    t.start()
    t.join(3)  # 主线程在这个位置,等待子线程3秒
    print("---main---end")

if __name__ == '__main__':
    # test_normal()
    # test_threading()
    # test_threading_setDaemon()
    test_threading_join()