#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:default.conf.py
@time(UTC+8):16/8/26-23:11
'''
import sys, os

APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(APP_DIR)

ALL_USER_INFO_FILE_PATH = os.path.join(APP_DIR, "db", "user_info.json")
ALL_USER_BILL_RECORD_FILE_PATH = os.path.join(APP_DIR, "db", "bill_record.json")

CONFIG_PARSER_FILE_PATH = os.path.join(APP_DIR, "db", "config_parser.txt")