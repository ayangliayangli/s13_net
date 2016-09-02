#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:index.py
@time(UTC+8):16/8/21-22:14
'''

# from reflect import commons
# commons = __import__("commons")

# this is interface of this reflect
# 反射: 以字符串的方式导入模块,以字符串的方式操作（查,增,删,判断存在）模块成员


def run():
    inp = input("input url(eg: commons/home):")
    m, f = inp.split("/") # eg manage/home  会自动导入 manage模块,然后执行 home()
    obj = __import__(m, fromlist=True)  # fromlist=True 允许构造m,使用符号【.】
    if hasattr(obj, f):  # 先判断模块是否有这个成员
        func = getattr(obj, f)  # 如果成员存在,那就执行该方法
        func()
    else:
        print("404")  # 如果成员不存在,那就直接报错


def append_project_path():
    import os
    import sys
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(project_path)


if __name__ == '__main__':
    run()



