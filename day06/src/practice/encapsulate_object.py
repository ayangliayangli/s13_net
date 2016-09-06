#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:encapsulate_object.py
@time(UTC+8):16/9/4-14:42
'''

class c1():
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def show(self):
        print("name:{name}  password: {password}".format(name=self.name, password=self.password))


class c2():
    def __init__(self, name, obj):
        self.name = name
        self.obj = obj


class c3():
    def __init__(self, obj):
        self.obj = obj


def main():
    c1_obj = c1("yangli", "123456")
    c2_obj = c2("yangli_c2", c1_obj)
    c3_obj = c3(c2_obj)

    c1_obj.show()  # name:yangli  password: 123456
    c2_obj.obj.show()  # name:yangli  password: 123456
    c3_obj.obj.obj.show()  # name:yangli  password: 123456


if __name__ == '__main__':
    main()