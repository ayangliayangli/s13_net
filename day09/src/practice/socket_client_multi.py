#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:socket_client_multi.py
@time(UTC+8):16/9/16-12:51
'''

import socket

ip_port = ('127.0.0.1', 9999, )
conn = socket.socket()
conn.connect(ip_port)
server_welcome_msg_str = str(conn.recv(1024), encoding='utf-8')
print(server_welcome_msg_str)

while True:
    inp = input(">>:")
    conn.sendall(bytes(inp, encoding='utf-8'))
    recv_data_str = str(conn.recv(1024), encoding='utf-8')
    print(recv_data_str)