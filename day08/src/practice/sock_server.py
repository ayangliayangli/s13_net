#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:sock_server.py
@time(UTC+8):16/9/9-17:46
'''

import socket

ip_addr = ("127.0.0.1", 9999)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.settimeout(10)
mysock.bind(ip_addr)
mysock.listen(5)
print("server is running:")
conn, addr = mysock.accept()

while True:
    # try:
    # print(addr, type(addr))
    cli_info_str = addr[0] + ":" + str(addr[1])
    recv_data = conn.recv(1024)
    if str(recv_data) == "quit" or str(recv_data) == "q":
        break
    print(cli_info_str + ">>" + str(recv_data, encoding='utf-8'))
    inp = input(">>")
    # send_data = str(recv_data, encoding='utf8').upper()
    send_data = inp.strip()
    # print(addr)
    conn.send(bytes(send_data, encoding='utf-8'))
    # except Exception :
    #     print("connection resret by peer")
    #     break

conn.close()