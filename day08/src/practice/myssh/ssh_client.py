#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:ssh_client.py
@time(UTC+8):16/9/10-15:58
'''

import subprocess, socket

ip_port = ('127.0.0.1', 9999)

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(ip_port)

while True:
    inp_strip = input(">>:").strip()
    if len(inp_strip) == 0:continue  # 如果输入为空,那么continue, 否则server 的 recv会阻塞
    send_data = inp_strip
    my_sock.send(bytes(send_data, encoding='utf-8'))
    if inp_strip == "exit" or inp_strip == "e":break  # 退出要在发送数据之后在break,否则服务器端会死循环,因为服务器端的conn没有了


    # 解决粘包问题
    # 思路--服务器传数据过来的时候,先传一个长度过来,客户端每次收1024个,直到收完为止
    recv_data = my_sock.recv(1024)
    recv_data_str = str(recv_data, encoding='utf-8')
    if recv_data_str.startswith("start"):
        # 获取到要接受数据的长度
        msg_size = int(recv_data_str.strip().split(":")[-1])
        my_sock.send(bytes("ready", encoding='utf-8'))  # 告诉服务器端客户端已经获取到长度,可以开始了

    receved_data_bytes = b''  # 已经获取到的数据
    receved_size = 0  # 已经获取到的数据的长度

    while receved_size < msg_size:  # 根据长度来判断是否跳出循环
        current_recv_data = my_sock.recv(1024)
        receved_data_bytes += current_recv_data
        receved_size = len(receved_data_bytes)
        print("-----receved_size:{} msg_size: {}".format(receved_size, msg_size))

    print(str(receved_data_bytes, encoding='utf-8'))
