#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:my_rpc_server.py
@time(UTC+8):16/10/1-22:30
'''

import pika


def callback(ch, method, properties, body):
    print("[x] received : \n{}".format(str(body, encoding='utf-8')))


def recv_data_via_client_queue(client_queue_name="client"):
    server_ip = "192.168.126.250"
    connnection = pika.BlockingConnection(pika.ConnectionParameters(host=server_ip))
    chan = connnection.channel()

    chan.queue_declare(queue=client_queue_name)

    chan.basic_consume(callback, queue=client_queue_name, no_ack=True)
    print("waiting for client return -------")
    chan.start_consuming()





server_list = [
                "192.168.126.250",
                "192.168.126.251",
                "192.168.126.252",
               ]
for index,item in enumerate(server_list, 1):
    print("index:{}, ip:{}".format(index, item))

sel_host_index = int(input("choose key:"))
sel_host_ip = server_list[sel_host_index - 1]
print("selected host: ", sel_host_ip)
cmd = input("cmd(要在客户端执行的命令):")


#########productor######

server_ip = "192.168.126.250"
connnection = pika.BlockingConnection(pika.ConnectionParameters(host=server_ip))
chan = connnection.channel()

# chan.queue_declare(queue='first_queue')
chan.exchange_declare(exchange=sel_host_ip, type="fanout")  # 让不同主机执行的命令存放在不同的exchange中

chan.basic_publish(exchange=sel_host_ip,
                   routing_key="",  # 这里很重要,制定是哪一个queue
                   body=cmd + "|" + "client"  # 发布的消息前面是命令,后面是结果返回的队列名字
                   )
print("send msg")
recv_data_via_client_queue(client_queue_name="client")
connnection.close()