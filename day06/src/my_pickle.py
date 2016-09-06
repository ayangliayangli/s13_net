#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:my_pickle.py
@time(UTC+8):16/9/4-21:29
'''

import pickle

my_list = [1, 2, 3]
my_dict = {"k1": 1, "k2": 2, "k3": 3}

# with open("db.txt", "w", encoding="utf-8") as fp:
#     pickle.dump(my_list, fp)

output_fp = open("db.txt", "wb",)  # 注意使用pickle 的时候,要使用二进制的方式打开文件,且不要指定编码
pickle.dump(my_list, output_fp)  # 这里dump 第一个数据 --> [ ]
pickle.dump(my_dict, output_fp)  # 这里dump 第二个数据 --> { }
output_fp.close()

input_fp = open("db.txt", "rb",)

pickle_load_data = pickle.load(input_fp)  # 这里load 第一个数据 , 从文件取出 --> [ ]
print(pickle_load_data, type(pickle_load_data))  # 这里load第二个数据, 从文件取出 -- { }

pickle_load_data = pickle.load(input_fp)
print(pickle_load_data, type(pickle_load_data))

# 建议,把要持久化的数据防盗dict中,pickle.load() 之后,通过dict的key来拿到指定的对象