#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:myhashlib.py
@time(UTC+8):16/8/24-22:08
'''

import hashlib

# 支持各种hash算法, SHA256 512 MD5
key="kdjfkdjsfaklsdjf"
src_password="123"
obj = hashlib.md5(bytes(key, encoding="utf-8"))  # 创建MD5对象,添加自己自定义的key
obj.update(bytes(src_password, encoding="utf-8"))
result = obj.hexdigest()
print(result)