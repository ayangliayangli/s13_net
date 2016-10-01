#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:my_context.py
@time(UTC+8):16/9/24-00:02
'''

from contextlib import contextmanager
import socket
import time

# 使用上下文知识点  with   模拟内置函数  open( ) 的效果
# 每次调用完之后,函数自动再执行一个操作, e.g. close file-like object


@contextmanager
def my_sock_with_context(*args, **kwargs):
    ip_port = ('0.0.0.0', 9999)
    my_sock = socket.socket()
    my_sock.bind(ip_port)
    my_sock.listen(5)

    try:
        print("start return to main function")
        time.sleep(1)
        yield my_sock
        time.sleep(1)
        print("return to my_sock_with_context")
    except:
        pass
    finally:
        time.sleep(2)
        my_sock.close()



with my_sock_with_context() as my_sock:
    print("main function")



