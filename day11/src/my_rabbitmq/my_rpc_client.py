#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:my_rpc_client.py
@time(UTC+8):16/10/1-22:30
'''

import pika
#######consumer######
server_ip  = "192.168.126.250"
conn = pika.BlockingConnection(pika.ConnectionParameters(host=server_ip))
chan = conn.channel()

chan.queue_declare(queue="first_queue")


def callback(ch, method, properties, body):
    print("[x] received : {}".format(body))

chan.basic_consume(callback,
                   queue="first_queue",
                   no_ack=True,
                   )
# start waiting msg
print("waiting for msg from {}".format(server_ip))
chan.start_consuming()
conn.close()