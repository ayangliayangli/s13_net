#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:setting.py
@time(UTC+8):16/9/4-21:10
'''
import os

APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEACHERS_FILE_PATH = os.path.join(APP_DIR, "db", "teachers")
STUDENTS_FILE_PATH = os.path.join(APP_DIR, "db", "students")
COURSES_FILE_PATH = os.path.join(APP_DIR, "db", "courses")