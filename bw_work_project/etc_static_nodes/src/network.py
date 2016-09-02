#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:network.py
@time(UTC+8):16/8/24-10:25
'''

import socket, os, sys


def test_connection(host, port, timeout=6):
    # return 0: success 1: error
    print("handling-{host}:{port}".format(host=host, port=port))
    try:
        cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cli_sock.settimeout(timeout)
        cli_sock.connect((host, int(port)))
        return 0
    except:

        return 1


if __name__ == '__main__':

    ret = test_connection("14.215.177.38", "80")
    print(ret)
    print(test_connection("14.215.177.38", 81))