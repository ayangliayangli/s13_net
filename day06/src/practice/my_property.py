#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:my_property.py
@time(UTC+8):16/9/4-23:15
'''


class A():
    static_field = "i am static field"  # 静态字段
    count = 5

    def __init__(self, name, password):  # 一般方法
        self.name = name  # 一般字段
        self.password = password  # 一般字段
        self.__private_name = "i am private_name"  # 这个是私有变量,在外面无法访问到,只能在class内部调用, 继承的class中也是不行的

    @staticmethod
    def show_static_method():
        print("我是静态方法,我可以通过cls name 调用")

    @classmethod
    def show_cls_method(cls):
        obj = cls()  # 可以在类方法中,实例化一个对象出来

    @property
    def show_property(self):
        print("i am a property getter")
        return self.count + 5

    @show_property.setter
    def show_property(self, value):
        print("i am a property setter")

    @show_property.deleter
    def show_property(self):
        print("i am a proterty deleter")


    # property 的第二种方式, 在一些开源项目中常用
    def f1(self):
        print("proterty 2 -- getter")

    def f2(self, value):
        print("proterty 2 -- getter")

    def f3(self):
        print("proterty 2 -- getter")

    foo = property(fget=f1, fset=f2, fdel=f3) # 注意参数是一个函数,而不是去执行函数



a_obj = A("yangli", "123456")
print(a_obj.show_property)  # --> getter
a_obj.show_property = 5  # --> setter
del a_obj.show_property  # --> deleter


# 测试第二种property
a_obj.foo
a_obj.foo = 5
del a_obj.foo