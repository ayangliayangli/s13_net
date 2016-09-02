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


def double_operator_handler(s):
    s = str(s)
    s = s.replace("++", "+")
    s = s.replace("+-", "-")
    s = s.replace("-+", "-")
    s = s.replace("--", "+")
    return s


def mul_div_handler(s):
    s = str(s)
    tmp_list = re.split(r"([*/])", s)
    # 注意这里要考虑到多个*号连起来的情况  eg  2*3*4  len 5  1 3
    current_index = 1
    result = None
    while current_index < len(tmp_list):
        if current_index == 1:
            # 当处理第一个符号的时候
            if tmp_list[current_index] == "*":
                result = float(float(tmp_list[current_index-1]) *
                               float(tmp_list[current_index + 1]))
            elif tmp_list[current_index] == "/":
                result = float(float(tmp_list[current_index-1]) /
                               float(tmp_list[current_index + 1]))
        else:
            if tmp_list[current_index] == "*":
                result *= float(tmp_list[current_index + 1])
            elif tmp_list[current_index] == "/":
                result /= float(tmp_list[current_index + 1])
        current_index += 2  # 处理完一个符号之后步长加1
    return str(result)


def add_sub_handler(s):
    s = str(s)  # 显示的转换为字符串
    tmp_list = re.split(r"([+-])", s)  # 以符号分割 1+2-3 ['1', '+', '2', '-', '3']  len:5  符号位置: 1 3
    result = None
    current_index = 1

    while current_index < len(tmp_list):
        if current_index == 1:
            # 处理第一个符号 + 或者 -
            if tmp_list[current_index] == "+":
                result = float(tmp_list[current_index - 1]) + float(tmp_list[current_index + 1])
            elif tmp_list[current_index] == "-":
                result = float(tmp_list[current_index - 1]) - float(tmp_list[current_index + 1])
        else:
            # 处理第二个或者第三个符号
            if tmp_list[current_index] == "+":
                result += float(tmp_list[current_index+1])
            elif tmp_list[current_index] == "-":
                result -= float(tmp_list[current_index+1])
        current_index += 2

    result_final = str(result)
    return result_final


def except_mul_divide(s):
    # 这里处理 + - ,以 + - 分割开,剩下的 * / 就在一个元素当中
    s = str(s)
    tmp_list = re.split(r"([+\-])", s)
    tmp_list_except_multiple_and_divide = []
    result = None
    for i in tmp_list:
        # 这里处理 * /
        i = str(i)  # 显示转换成为字符串
        is_contain_mul_div_flag = re.findall(r"[*/]", i)
        if is_contain_mul_div_flag:
            # 处理 * /
            tmp_list_except_multiple_and_divide.append(mul_div_handler(str(i)))
        else:
            # 把结果放入 tmp_list_except_multiple_and_divide
            tmp_list_except_multiple_and_divide.append(str(i))
    result = "".join(tmp_list_except_multiple_and_divide)
    result_final = double_operator_handler(result)
    return result_final


def handle_nomal_calculate(s):
    # 这里处理只有+ - * / 的字符串
    # ret = eval(s)
    # return ret
    s = str(s)  # 这里显示的转换,免得等会儿报错
    ret_except_mul_and_div = except_mul_divide(s)  # 这里处理掉 * /  返回类似于  1+2-3
    ret_one_char = add_sub_handler(ret_except_mul_and_div)  # 这里处理掉 + - 返回的就是一个数字
    ret_final_str = str(ret_one_char)
    print(ret_final_str)  # 这里开始没有返回,那么函数调用者会收到一个none,程序会报错
    return ret_final_str


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
        # 如果这里返回的是0 那么str(0) == none 会出错
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
    while not re.search(r"^.?\d[^+-]*$",s):
        # s 还是一个表达式的时候,继续执行去除括号的内容
        s = handle_brackets(s)
        # 这里要处理一下多余的符号 关于+- -+ ++ -- 之类的
        print("double_operator_pre",s)
        s = double_operator_handler(s)
        print("double_operator_after",s)
        print("-----------------------")
    return s


def main(s):
    '''主函数'''
    ret = calculate(s)
    print("{}={}".format(s, ret))


if __name__ == '__main__':
    # s = "1*(2+3)+7*(2+3)"
    # s2 = "1*5+7*-1"
    s3 = "1*(2+3)+7*(2+3)+(45+45/6-45/66+(5-9))"
    #
    # main(s3)
    s = "2+3*5*(2-2)"
    # ret = except_mul_divide(s)
    # print(ret)

    # s = "2+3+4-9"
    # ret = add_sub_handler(s)
    # print(ret, type(ret))
    main(s3)