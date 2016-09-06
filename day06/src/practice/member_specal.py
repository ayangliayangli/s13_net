#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:member_specal.py
@time(UTC+8):16/9/5-21:59
'''

class A():
    '''
    我是类, A
    '''
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __call__(self, *args, **kwargs):
        print("execute call()")

    def __str__(self):
        s = self.name + "---" + self.password
        return s

    def __repr__(self):
        pass

    def __iter__(self):
        yield 1
        yield 2
        yield 3
        yield "a"
        yield "b"
        yield "c"

    def __getitem__(self, item):
        if type(item) == str:
            # 使用的是字典的方式  obj["k1"]
            print("dict way--getitem")
            print(type(item), item)
        elif type(item) == slice:
            # use list way :   obj[start:end:step]
            print("list way --- getitem")
            print(type(item), item)

    def __setitem__(self, key, value):
        if type(key) == str:
            # 使用的是字典的方式  obj["k1"]
            print("dict way -- setitem")
            print(type(key), key)
            print(type(value), value)
        elif type(key) == slice:
            # use list way :   obj[start:end:step]
            print("list way --- setitem")
            print(type(key), key)
            print(type(value), value)

    def __delitem__(self, key):
        if type(key) == str:
            # 使用的是字典的方式  obj["k1"]
            print("dict way -- delitem")
            print(type(key), key)
        elif type(key) == slice:
            # use list way :   obj[start:end:step]
            print("list way --- delitem")
            print(type(key), key)

class B(A):
    pass

class C():
    pass


a_obj = A("yangli", "123456")  # __init__
print(a_obj.__doc__)
print(a_obj.__class__)
a_obj()  # 对象后面加上括号,   execute   __call__
print(a_obj)  # __str__
ret = str(a_obj)  # __str__
print(ret)

print("-------__iter__ show---------")
for item in a_obj:
    print(item)

print("---------getitem  setitem delitem dic-like----------")
a_obj["k1"]  # __getitem__  tpye(item) == str
a_obj["k1"] = "v1"  # __setitem__  tpye(item) == str
del a_obj["k1"]  # __delitem__  tpye(item) == str

print("---------getitem  setitem delitem  list-like----------")
a_obj[1:5:2]  # __getitem__ type(key) == slice
a_obj[1:5:2] = [1, 2, 3]  # __setitem__ type(key) == slice
del a_obj[1:5:2]  # __delitem__ type(key) == slice


print("{key:-^50}".format(key="isinstance_issubclass"))
print(isinstance(a_obj, A))  # True
print(issubclass(B, A))  # True
print(issubclass(C, A))  # False