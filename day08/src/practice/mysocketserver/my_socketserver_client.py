#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:my_socketserver_client.py
@time(UTC+8):16/9/10-23:39
'''

import socket

ip_port = ('127.0.0.1', 9997)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(ip_port)

recv_data_str = str(mysock.recv(1024), encoding='utf-8')
print(recv_data_str)

while True:
    send_data_str = input(">>:").strip()
    if not send_data_str:
        # 如果输入为空 , continue
        continue

    send_data_bytes = bytes(send_data_str, encoding='utf-8')
    mysock.send(send_data_bytes)

    if send_data_str == "exit" or send_data_str == "e":
        break

    # 收报的时候要注意解决粘包问题
    recv_data_str = str(mysock.recv(1024), encoding='utf-8')
    if recv_data_str.startswith("start"):
        msg_size = int(recv_data_str.split("|")[-1])
    mysock.send(bytes('ready', encoding='utf-8'))  # 发送接收到长度的信息

    recved_data_len = 0
    recved_data_bytes = b''

    while recved_data_len < msg_size:
        cur_recv_data_bytes = mysock.recv(1024)
        recved_data_bytes += cur_recv_data_bytes
        recved_data_len += len(recved_data_bytes)
        print('----recved_data_len:{}, msg_len:{}'.format(recved_data_len, msg_size))

    recved_data_str = str(recved_data_bytes, encoding='utf-8')
    print(recved_data_str)

mysock.close()
