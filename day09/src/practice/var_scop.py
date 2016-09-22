#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:var_scop.py
@time(UTC+8):16/9/12-22:13
'''

## 小知识点-作用域
# 全局变量全局可读, 局部变量优先级更高
# 如果要写，加上globals 关键字， list dict set 等等除外
#
# python js 没有块级作用域(选择，循环等是一个块级作用域)， 所以块里面的变量在块外面也是可以运行的
# python 中是以函数为作用域的
# **在函数执行前，作用域已经完全确定，与函数在什么地方执行没有影响**

if 1 == 1:name = "yangli"
print(name)  # 这里可以输出： yangli


# def func():
#     name_local = "yangli"
# func()
# print(name_local) # 这里不会输出 IDE也直接报错


name2 = "yangli2"

def f1():
    print(name2)

def f2():
    name2="yangli2_f2"
    f1()

f2()  # 执行f2 , print的是 yangli2 , 变量的作用域在函数执行之前就已经确定



#############################
# list  特殊构造方法
print("# list  特殊构造方法 -- sina 面试题")
li1 = [ x+100 for x in range(10)]
li2 = [lambda :x for x in range(10)]
# li2 是一个列表,列表钟的元素是函数
# li2 --->  [<function <listcomp>.<lambda> at 0x1005f1ea0>, <function <listcomp>.<lambda> at 0x1005f1f28>, <function <listcomp>.<lambda> at 0x1005fe048>,...
# 如果把list第一个元素（func）取出来执行,因为最终x的值为9,所以,会输出 9

print(li2)
print(li2[0]())  # 输出9