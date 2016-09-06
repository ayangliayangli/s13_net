#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:practice.py
@time(UTC+8):16/9/4-12:18
'''


class Foo():
    static_name = ""
    static_password = ""

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def fetch(self, sql):
        print(sql)




# 测试函数
def main():
    obj = Foo("mazhongxiao", "123456")
    obj.fetch("select * from user")

    print("name", obj.name)
    print("password", obj.password)
    print("static_password", Foo.static_password)  # 这里还没有赋值,所以输出的内容为空字符串

    Foo.static_password = "i am static_password"
    print("static_password", obj.static_password)  # 通过对象类调用 静态字段
    print("static_password", Foo.static_password)  # 通过类来调用  静态字段


if __name__ == '__main__':
    main()