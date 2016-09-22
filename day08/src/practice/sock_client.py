#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:sock_client.py
@time(UTC+8):16/9/9-17:46
'''

import socket

ip_addr = ("10.0.0.191", 9999)
mysock = socket.socket()
mysock.settimeout(100)

mysock.connect(ip_addr)

while True:

    send_data = input(">>:")
    mysock.send(bytes(send_data, encoding='utf8'))
    recv_data = mysock.recv(1024)
    # print(peer_info)
    peer_info = mysock.getpeername()
    print(peer_info[0] + ":" + str(peer_info[1]) + ">>" + str(recv_data, encoding='utf8'))

    if send_data == "quit" or send_data == "q":
        break

mysock.close()
