#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:my_subprocess.py
@time(UTC+8):16/8/29-23:28
'''
import subprocess


# call
ret_call = subprocess.call("pwd", shell=True)
print(ret_call)

# check_call
# ret_check_call = subprocess.check_call("pwdd", shell=True)  # 这里会报错
# print(ret_check_call)

# check_out
ret_check_out = subprocess.check_output("pwd", shell=True)
print(ret_check_out, type(ret_check_out))  # b'/Users/lee/PycharmProjects/python_learn/s13_net/day04/src/practice\n' <class 'bytes'>
print(str(ret_check_out), type(str(ret_check_out)))  # b'/Users/lee/PycharmProjects/python_learn/s13_net/day04/src/practice\n' <class 'str'>


# Popen
## cwd first
# subprocess.Popen("mkdir test.d", shell=True, cwd="/Users/lee/")


## 交互式的命令
obj = subprocess.Popen("python", shell=True, universal_newlines=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,)
obj.stdin.write("ls\n")  # 应该会报错
print(obj.stdout.read())
print("start---")
print(obj.stderr.read())
print("end ----")

# print(obj.communicate("prinnt(\"1\")",5))  # 这个货报错
# print(obj.communicate("print(\"1\")",5))  # 这个直接执行输出