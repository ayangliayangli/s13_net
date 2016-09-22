#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:my_socket_server.py
@time(UTC+8):16/9/10-23:39
'''


import socketserver
import subprocess


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        client_info = self.client_address
        print("--------", client_info, "is connected")
        conn = self.request

        # send welcome info to client
        conn.send(bytes('welcome to my_socketserver_server', encoding='utf-8'))

        # dead while
        while True:
            recv_data = conn.recv(1024)
            # conn.send(recv_data.upper())
            recv_data_str = str(recv_data, encoding='utf-8')
            cmd_res = subprocess.Popen(recv_data_str, shell=True,
                                       stdin=subprocess.PIPE,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)

            # 注意: file-like 对象read()之后,指针会到最后,导致读出来的是空
            cmd_res_data = cmd_res.stdout.read()
            if not cmd_res_data:
                cmd_res_data = cmd_res.stderr.read()

            if len(cmd_res_data) == 0:
                # cmd execute right , but not out put , e.g. cd
                cmd_res_data = bytes("cmd output is none", encoding='utf-8')

            # 解决粘包问题
            msg_size = len(cmd_res_data)
            conn.send(bytes('start|' + str(msg_size), encoding='utf-8'))
            ready_flag = conn.recv(1024)
            if str(ready_flag, encoding='utf-8').startswith("ready"):
                conn.send(cmd_res_data)

    def finish(self):
        client_info = self.client_address
        print(client_info, "is disconnected")

if __name__ == '__main__':
    print("server is running ... ")
    ip_port = ('0.0.0.0', 9997)
    server = socketserver.ThreadingTCPServer(ip_port, MyServer)
    server.serve_forever()