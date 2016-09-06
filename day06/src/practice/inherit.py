#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:inherit.py
@time(UTC+8):16/9/4-14:52
'''


class S1():
    def f1(self):
        print("s1 f1")

    def f2(self):
        print("s1 f2")
        self.f3()

    def f3(self):
        print("s1 f3")


class S2(S1):
    def f1(self):
        print("s2 f1")
        self.f2()

    def f3(self):
        print("s2  f3")

s1_obj = S1()
s2_obj = S2()

s1_obj.f1()
s2_obj.f1()
s2_obj.f2()

print("{:-^50}".format("分割线"))

s2_obj.f1()  # result:  s2 f1  s1 f2  s2 f3
# 这里要注意,找方法的时候要从self这个对象那里开始往上找
# 所以,虽然看似是在s1里面执行f3,但是self这里指向的是 s2_obj ,所以执行self.f3() 的时候,要执行s2.f3()