#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:my_pymysql.py
@time(UTC+8):16/9/28-16:13
'''

import pymysql

host = 'office.yanglix.xyz'
port = 33306
username = "yangli"
password = "yanglipass"
db = "s13_net"

conn = pymysql.Connect(host=host, port=port, user=username, password=password, db=db)
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

cursor.execute('select * from _t_assets')
ret = cursor.fetchall()
print(ret)
cursor.close()
conn.close()