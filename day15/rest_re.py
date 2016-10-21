#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:rest_re.py
@time(UTC+8):16/10/19-00:38
'''

import re
s = "javascript is more useful than java and javabeans"



re.sub('\s', '-', s)
print(s)