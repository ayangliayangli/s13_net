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
@time(UTC+8):16/8/20-10:23
'''


#divmode
#常用在分页中
print(divmod(97,10))   #---》 (9,7)

# filter map
# filter    将迭代器里面的元素依次作为参数到func去执行,返回为真的留下
# map       将迭代器里面的元素依次作为参数到func去执行,饭胡结果
# map(function, iterable)
li = [1, 2, 10, 22, 55]
li_filter = filter(lambda a : a<22, li)
li_map = map(lambda a:a+1, li)
print("li_filter: {} , li_map: {}".format(list(li_filter), list(li_map)))


# globals() 当前能使用到的所有全局变量
# locals()  当前能使用到的所有的局部变量
NAME = "LI YANG"


def show():
    a = 123
    b = 456
    print(locals())
    print(globals())
show()


#hash
s = "kljdfklasdjflasdjfla;sdjfla;sdjflas;djfasdfjk"
s_hash = hash(s)
print("s_hash:{}".format(s_hash))


#id len type
print("-----id--len--type-------")
a = 1
b = a
print(id(a))
print(id(b))

print(len("杨力"))    # --> 2 len of s ,在python3 中按照char计算,所以返回2
print(len(bytes("杨力", encoding="utf-8")))  # 6 ,先转换成bytes ,然后在计算

for item in "杨力":
    print(item)

#max min sum pow
print("---max--min--sum--pow---")
print(max(1,2,3))
print(min(1,2,3))
print(sum([1,2,3]))
print(pow(2,10))
print(2**10)


#range
print("---range()---")
print(range(0,10,2))
for i in range(0, 10, 2):
    print(i)


#reversed
print("---reversed---")
li = [1,2,3,4,5,6,100]
for i in reversed(li):
    print(i)

#slice()   切片 ,一般使用中括号
s = "i love you"
s[0:3]


#vars()  当前模块所有的变量
print("---zip---")
l1 = ["i", 11, 22, 33]
l2 = ["love", 11, 22, 33]
l3 = ["you ", 11, 22, 33]
zip_result = zip(l1, l2, l3)
zip_result_list = list(zip_result)
print(zip_result_list)



# 装饰器
# 原理1: f 函数名代表函数本省, f() 代表执行函数
# 原理2: 如果有重名的变量,前面的会被覆盖
print("------装饰器------------------------")


def outer(func):
    def inner(*args, **kwargs):
        print("-----before-------")
        ret = func(*args, **kwargs)
        print("------after-------")
        return ret
    return inner

# 加上@outer 之后,myfunc函数就变成了inner函数
@outer
def myfunc(args):
    print("this is mycfunc main body")
    print("this is args: {}".format(args))

myfunc("fuck")


#双层装装饰器
def outer2(func):
    def inner(*args, **kwargs):
        print("outer2----before----")
        ret = func(*args, **kwargs)
        print("outer2----after----")
        return ret
    return inner  # attention: inner 没有括号

@outer2
@outer
def myfunc2(args):
    print("this is myfunc2")
    print(args)

print("------双层装饰器-------------------------")
myfunc2("args_func2")


# 生成器 yield
# 迭代器:  不用自己写的,迭代器就是可以从生成器中去取数据的能力
def my_range(start, end, step):
    print("start myrange in while")
    while start < end:
        yield start
        start += step

print("迭代器去娶数据了--------------------------")
for i in my_range(0, 10, 1):
    print(i)
# ret = my_range(0,10,1)
# print(ret.__next__())

# 反射