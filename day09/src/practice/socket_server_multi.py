#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:socket_server_multi.py
@time(UTC+8):16/9/16-12:51
'''

import socket, os
import select

# IO多路复用 --- 检测socket是否发生了变化,如果发生了变化就通知
# rlist, wlist, elist = select.select(inputs, outputs, error, 1)  解释: \n
# ---  检测inputs里面的socket是否发生了变化,如果变化了,就返回,且超时时间是1s（第四个参数
# --- outputs 和 wlist 里面的数据是一样的
# ---  检测error里面的socket, 有错误的就放在elist里面

# 该程序实现的其实是一个伪多路复用,因为其实还是只有一个程序在处理客户端的请求,for循环,依次处理的
# 要实现真正的多路复用,需要结合多线程的概念,让每个请求都使用不通的线程来处理



ip_port = ('0.0.0.0', 9999)
my_socket = socket.socket()
my_socket.bind(ip_port)
my_socket.listen(5)
print("server is listening in ", ip_port)

inputs = [my_socket, ]
outputs = []
messages = {}
while True:
    # 循环的处理客户过来的连接
    rlist, wlist, elist = select.select(inputs, outputs, [], 2)
    print('inputs len: {}, rlist len: {}, wlist len: {}'.format(len(inputs), len(rlist), len(wlist)))

    for r in rlist:
        if r == my_socket:
            # 有新的连接过来
            conn, address = r.accept()
            print("new connection: ", address)
            conn.sendall(bytes('welcome access li server', encoding='utf-8'))
            inputs.append(conn)  # 同时把该conn也加入监听的列表中
            print("---socket_cli:", conn)
            # 这里注意,虽然添加到inputs 里面的都是conn, 但是每个conn是不同的socket
            # 一个socket可以由4个元素确定 local addr, local port, remote addr, remote port
            messages[conn] = []
        else:
            # 有新的数据连接过来
            try:  # 考虑到客户端异常断开连接的情况
                recv_bytes = r.recv(1024)
                if not recv_bytes:
                    raise Exception("客户端发送了空的内容过来, 可能是断开连接了")
                print("recv_bytes", recv_bytes)
                # r.sendall(recv_bytes)
                outputs.append(r)
                messages[r].append(recv_bytes)  # 把数据放入消息字典里面
            except Exception as e:
                inputs.remove(r)
                if r in outputs: outputs.remove(r)
                if r in messages: del messages[r]
                print(e)

    for w in wlist:
        # 处理有消息的队列, 返回信息给客户端  -- 实现读写分离
        send_data_bytes = messages[w].pop() + bytes("request", encoding='utf-8')
        w.sendall(send_data_bytes)
        outputs.remove(w)


