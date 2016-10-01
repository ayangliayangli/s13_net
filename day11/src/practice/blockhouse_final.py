#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:blockhouse.py
@time(UTC+8):16/10/1-16:15
'''


import paramiko
from paramiko.py3compat import u
import select
import sys
import termios, tty
import sys,os,socket

'''
这是一个堡垒机的雏形,使用paramiko 去执行命令
暂时没有实现:tab 补全
'''

ip_port = ("192.168.126.250", 6322)
username = "bwweb"
password = "123456"
trans = paramiko.Transport(ip_port)
trans.start_client()
trans.auth_password(username=username, password=password)

chan = trans.open_session()  # open session or chanel
chan.get_pty()  # get a terminal
chan.invoke_shell()  # active terminal





# 获取原来的tty属性
# oldtty = termios.tcgetattr(sys.stdin)

# 设置新的tty
try:
    # tty.setraw(sys.stdin.fileno())
    # chan.settimeout(0.0)

    # 下面是核心逻辑
    # 在这里就是死循环不断接受用户的数据,提交给服务器端执行,然后服务器端返回结构
    # 利用select 来见他那个file-like 对象的变化
    # 监听的对象有:   sys.stdin    chan
    while True:
        rlist, wlist, elist = select.select([sys.stdin, chan], [], [], 1)
        if chan in rlist:
            # 收到了服务器的数据,那就显示
            try:
                text = u(chan.recv(1024))  # python3 才需要这样设置一下, text 是str
                sys.stdout.write(text)
                sys.stdout.flush()
            except Exception as e:
                print(e)
                break

        if sys.stdin in rlist:
            # 客户端输入了,那就提交给服务器端
            cmd = sys.stdin.readline()  # 从这里拿到的cmd 是str 类型, chan 内部应该会自动转
            # print('-----cmd: ', cmd, type(cmd))
            if cmd:
                chan.sendall(cmd)
            else:
                continue

except Exception as e:
    print(e)

finally:
    # termios.tcsetattr(sys.stdin, termios.TCSADRAIN, oldtty) # 如果程序退出,还原原来的tty属性,否则这个窗口就要重新打开才能用
    chan.close()
    trans.close()
