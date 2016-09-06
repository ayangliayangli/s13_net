#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:member_qualifier.py
@time(UTC+8):16/9/5-21:15
'''


class A():
    __private_static_name = "private_static_name"

    def __init__(self, name, password):
        self.__private_normal_field_name = name
        self.__private_normal_field_password = password

    def __privare_normal_method_show(self):
        print(A.__private_static_name)

    def public_normal_method(self):
        print(A.__private_static_name)


a_obj = A("yangli", "123456")
# a_obj.__private_normal_field_name  # error
# a_obj.__private_static_name  # error
# a_obj.__privare_normal_method_show()
a_obj.public_normal_method()  # good ,you can get private member via public method

# 如果一定有必要,那可以强制在外面通过obj去拿到private member, 但是不推荐 --》 因为不规范