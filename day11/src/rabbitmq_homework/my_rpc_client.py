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
import subprocess
#######consumer######

local_host_ip = "192.168.126.250"  # 本机的ip地址,去这个exchange取数据来执行

server_ip  = "192.168.126.250"
conn = pika.BlockingConnection(pika.ConnectionParameters(host=server_ip))
chan = conn.channel()

# chan.queue_declare(queue="first_queue")
chan.exchange_declare(exchange=local_host_ip, type="fanout")

result = chan.queue_declare(exclusive=True)
queue_name = result.method.queue

chan.queue_bind(exchange=local_host_ip, queue=queue_name)



def callback(ch, method, properties, body):
    print("[x] received : {}".format(body))
    recv_data_str = str(body, encoding='utf-8')
    cmd,client_queue_name = recv_data_str.split("|")

    cmd_ret = subprocess.Popen(cmd, shell=True,
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                     )
    cmd_ret_str = cmd_ret.stdout.read() + cmd_ret.stderr.read()
    print("cmd_ret_str", cmd_ret_str)

    # 把执行的结果【cmd_ret_str】发布到队列【client_queue_name】当中,服务器自己回去取结果
    conn = pika.BlockingConnection(pika.ConnectionParameters(host=server_ip))
    chan = conn.channel()
    chan.queue_declare(queue=client_queue_name)
    chan.basic_publish(exchange="",
                       routing_key=client_queue_name,
                       body=cmd_ret_str
                       )
    conn.close()



chan.basic_consume(callback,
                   queue=queue_name,
                   no_ack=True,
                   )
# start waiting msg
print("waiting for msg from {}".format(server_ip))
chan.start_consuming()
