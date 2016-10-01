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

#########productor######

server_ip = "192.168.126.250"
connnection = pika.BlockingConnection(pika.ConnectionParameters(host=server_ip))
chan = connnection.channel()

chan.queue_declare(queue='first_queue')

chan.basic_publish(exchange="",
                   routing_key="first_queue",  # 这里很重要,制定是哪一个queue
                   body="this is first mq from yangli"
                   )
print("send msg")
connnection.close()