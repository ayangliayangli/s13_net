#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:productor_consumer.py
@time(UTC+8):16/9/17-12:36
'''

import queue, threading
import time

consumers = ["li1", "li2", "li3", "li4", "li5", "li6", "li7", "li8", "li9", "li10", ]
q = queue.Queue(200)


def product(args):
    while True:  # 厨师会一直生产
        time.sleep(1)
        current_product = 'chef:' + str(args) + '做的包子'
        print("[product]:", current_product)
        q.put(current_product, block=True, timeout=None)


def consumer(*args, **kwargs):
    while True:  # 模拟消费者会一直消费
        time.sleep(3)
        product = q.get()
        print('[consumer]', consumers[args[0]], "eat", product)


def start_product():
        for i in range(3):
            t = threading.Thread(target=product, args=(i, ))
            t.start()


def start_consumer():
        for i in range(5):
            t = threading.Thread(target=consumer, args=(i, ))
            t.start()


def get_queue_size():
    while True:
        s = 'maxsize: {}, current_size: {}'.format(q.maxsize, q.qsize())
        print('currentstatus---------', s)
        time.sleep(1)


def start_get_queue_size():
    t = threading.Thread(target=get_queue_size, )
    t.start()

if __name__ == '__main__':
    start_product()
    start_consumer()
    start_get_queue_size()

