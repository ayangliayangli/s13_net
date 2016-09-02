#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:myos.py
@time(UTC+8):16/8/24-21:59
'''

import os

# os.path.abspath()  # 获取绝对路径
# os.path.dirname()  # 获取当前文件的文件夹路径

APP_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# print(os.name)
# print(os.stat(os.path.join(APP_DIR, "src", "practice", "myre.py")))


# os.makedirs("dir1/dir2")  # 新建多级目录
# os.removedirs("dir1")  # 删除多级目录,需要目录为空
# os.mkdir("dir1")  # 新建单个目录
# os.rmdir("dir1/dir2")  # 删除单个目录
# os.remove("dir1/haha.py")  # 删除一个文件

# os_stat_myos = os.stat("myos.py")
# mtime = os_stat_myos.st_mtime
# import time
# print(time.localtime(mtime))
# print(os_stat_myos)

print(os.sep)
print(os.linesep)
print(os.pathsep)
print(os.name)
print(os.path.split(os.path.abspath(__file__)))   # ('/Users/lee/PycharmProjects/python_learn/s13_net/day04/src/practice', 'myos.py')

print(os.path.exists("myos.py"))
print(os.path.isabs(os.path.abspath(__file__)))
print(os.path.isdir("dir1"))

