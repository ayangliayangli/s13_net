#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:my_calculator.py
@time(UTC+8):16/8/26-13:28
'''

import re, sys, os


def handle_nomal_calculate(s):
    ret = eval(s)
    return ret


def handle_brackets(s):
    # 该函数用于处理括号的情况
    # 会自动调用 handle_nomal_calculate 处理非括号的部分
    # 返回的是处理第一个括号之后的字符串
    result = ""
    tmp = re.split(r"\(([^()]+)\)", s, 1)
    print(tmp)
    # 找到 第一个最里面的括号 , 括号里面不在有括号的内容,
    # tmp 返回一个三个元素的list, 第二个元素就是括号里面的内容
    if len(tmp) == 3:
        # 还有有括号的情况
        tmp[1] = str(handle_nomal_calculate(tmp[1]))

    elif len(tmp) == 1:
        # 没有括号的情况
        tmp[0] = str(handle_nomal_calculate(tmp[0]))
        print("没有括号了")
    else:
        print("can not split")

    result = "".join(tmp)
    return result


def calculate(s):
    # 循环调用处理括号的函数,知道得到的结果是一个符号加上一个数字
    while not re.search(r"^.?\d$",s):
        # s 还是一个表达式的时候,继续执行去除括号的内容
        s = handle_brackets(s)
    return s



if __name__ == '__main__':
    s = "1*(2+3)+7*(2+3)"
    s2 = "1*5+7*-1"

    ret = calculate(s)
    print("{}={}".format(s, ret))