#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:my_config_parser.py
@time(UTC+8):16/8/29-21:18
'''


import configparser
from day04.config import setting

# 处理配置文件,--需要是制定格式的配置文件
# [session1]
# k1 = v1
# k2:v2
config = configparser.ConfigParser()
config.read(setting.CONFIG_PARSER_FILE_PATH, encoding="utf-8")

sections = config.sections()
section1_keys = config.options("section1")
section1_k1 = config.get("section1", "k1")

print(sections)
print(section1_keys)
print(section1_k1)

# section add / remove / check
config.has_section("section1")  # True
config.has_option("section1", "k1") # True
config.add_section("section3")
config.remove_section("section3")
config.write(open(setting.CONFIG_PARSER_FILE_PATH, "w"))  # 对于增删节点后需要重新写入文件
# option add / remove / check
config.has_option("section1", "k1")
config.set("section1", "k3", "v3")
config.remove_option("section1", "k1")
config.write(open(setting.CONFIG_PARSER_FILE_PATH, "w"))

