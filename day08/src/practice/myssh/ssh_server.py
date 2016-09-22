#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:ssh_server.py
@time(UTC+8):16/9/10-15:58
'''

import subprocess, socket

ip_port = ('0.0.0.0', 9999)

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.bind(ip_port)
my_sock.listen(5)

while True:
    conn, addr = my_sock.accept()

    while True:
        recv_data = conn.recv(1024)  # 如果发过来的是空,这里会阻塞
        resv_data_str = str(recv_data, encoding='utf-8')
        print("request execute cmd:" +str(recv_data, encoding='utf-8'))
        if resv_data_str == "e" or resv_data_str == "exit":
            s = "{ip}:{port} is disconnect".format(ip=addr[0], port=addr[1])
            print(s)
            break  # 退出本次连接,整个程序不会退出,外死循环会再次接收下一个连接

        p = subprocess.Popen(str(recv_data, encoding='utf-8'), shell=True, stdout=subprocess.PIPE)
        res = p.stdout.read()
        if len(res) == 0:
            # cmd error
            send_data = "cmd error"
        else:
            # subprocess
            send_data = str(res, encoding='utf-8')


        # 解决粘包问题,先发送一个长度过去
        send_data_bytes = bytes(send_data, encoding='utf-8')
        msg_size = len(send_data_bytes)
        conn.send(bytes("start:" + str(msg_size), encoding='utf-8'))
        recv_data = conn.recv(1024)
        if str(recv_data, encoding='utf-8').startswith("ready"):
            # start return result
            conn.send(send_data_bytes)

