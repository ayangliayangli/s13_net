#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:mysys.py
@time(UTC+8):16/8/24-21:42
'''

import sys, time


# sys.argv  把参数放在一个list里面
# sys.path

def view_bar(rate,total):
    rate_num = int(rate/total*100)
    r = "\r%s>%d%%" % ("="*rate_num, rate_num)   # \r 是回到当前行的最前面
    sys.stdout.write(r)
    sys.stdout.flush()


if __name__ == '__main__':
    for i in range(101):
        time.sleep(1)
        view_bar(i,100)