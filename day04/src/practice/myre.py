#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:myre.py
@time(UTC+8):16/8/22-20:57
'''


# re == REGULAR EXPRESS 正则表达式,一门专门处理字符串的语言
# 常用符号 ^ $ . * () [] {} | \ ? +
# ^   一行开头
# $   一行结尾
# .   匹配任意一个字符串(除了换行符\n)
# *   匹配多个前面的字符  {0,}
# ()  括号里面的要么没有,要么全有
# []  括号中的字符任意娶一个,所有符号在中括号里面不在又特殊意义 3个除外 - ^
# {}  前面字符重复次数 {start, end}
# ?   {0, 1}
# ?   {1, }
# |   or
# \   转移字符,街上特殊意义的字符,变成普通字符    跟上一些普通字符,变成特殊意义的字符

# \d  [0-9]
# \D  [^0-9]
# \s  [\t\n\r\f\v] 空白字符
# \S  [^\t\n\r\f\v] 非空白字符
# \w  [a-zA-Z0-9]
# \W  [^a-zA-Z0-9]
# \b  匹配一个单词边界

# 重用组合
# [a-z]   a-z
# [^a-z]  不是字母
# [\d]    数字, \ 在[ ]里面还有自己的功能
# .*      任意多个任意字符
# .*?     非贪婪模式的任意多个字符

# 建议: 以后使用re的时候,尽量使用r

import re


s = "yanglidkfjkfj_yangli_kdfjkjyang li_kdfjkyanglkdkdkddkliyangli"
ret_findall = re.findall("yang.{0,}?li", s)
print(ret_findall)  # ['yangli', 'yangli', 'yang li', 'yanglkdkdkddkli', 'yangli']

# findall() 在字符串中找所有符合规则的字符串 --> list
# findall() 支持在在patterm里面使用（),返回的将是括号里面匹配的内容
# findall() 是最常用的
s2 = " i am handsomei"
ret_findall_2 = re.findall(r"\bi\b", s2)
print(ret_findall_2)


# match   仅匹配一个, 从字符串的 开始位置 匹配,如果开始的位置匹配失败,后面就算有,也不匹配了
# search  仅匹配一个, 在整个字符串中匹配
ret_match = re.match("yang.*?li", s)
print(ret_match.group())  # yangli
print(re.search("yang.*?li", s).group())  # yangli


# sub subn 替换 --> tuple
s3 = "i love you, ldde, ldfe"
ret_sub = re.sub("l.{2}e", "hate", s3)
print(ret_sub)  # i hate you, hate, hate
ret_subn = re.subn("l..e", "hate", s3)
print(ret_subn)  # ('i hate you, hate, hate', 3)

# split 分割 --> list
s4 = "1one2two3tree4four5"
ret_split = re.split("\d+", s4)
print(ret_split)  # ['', 'one', 'two', 'tree', 'four', '']

# 要在re中匹配一个单纯的 \ ,需要 \\ 因为在RE中\有自己的功能
# 所以python要传4个\\进去
# 注意顺序: 先到python解释器,然后到RE模块解释
print(re.findall("\\\\com", "www.\com"))
print(re.findall(r"\\com", "www.\com"))



# re的分组 -- （ ）: 在原来的基础之上再次分开
s = "i have a dream, and i have a night"
print(re.findall("h(\w+)", s))  # ['ave', 'ave', 't']
s_match = re.search("h(?P<name>\w+)", s)  # re.search() 基本一致
print(s_match.group())  # have
print(s_match.groups())  # ('ave', )
print(s_match.groupdict())  # {'name': 'ave'}