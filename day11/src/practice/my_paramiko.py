#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:my_paramiko.py
@time(UTC+8):16/10/1-11:31
'''

import paramiko

# 使用trans 来封装
# 密码方式连接 key方式连接
# 执行命令     文件传输


# 使用对象封装,顺便回忆一下OOP

class MyParamiko():

    def __init__(self, host, port, name, password,):
        self.host = host
        self.port = port
        self.name = name
        self.password = password

    def connect(self):
        trans = paramiko.Transport((self.host, self.port))
        trans.connect(username=self.name, password=self.password)
        self.__transport = trans

    def close(self):
        self.__transport.close()

    def cmd_execute(self):
        cmd = input("cmd:")
        print("cmd:{}".format(cmd))
        ssh_client = paramiko.SSHClient()
        ssh_client._transport = self.__transport
        stdin, stdout, stderr = ssh_client.exec_command(cmd)
        print(stdout.read())

    def trans_file(self,local_path, remote_path):
        sftp = paramiko.SFTPClient.from_transport(self.__transport)
        sftp.put(local_path, remote_path)


def main():
    myParamiko = MyParamiko(host='192.168.126.250', port=6322, name="bwweb", password="123456")
    myParamiko.connect()  # connect server , gen transport
    myParamiko.cmd_execute()  # execute cmd
    # 传输一个文件到服务器端,并且修改了一下名字
    myParamiko.trans_file("my_mysqlalchemy.py", "/home/www/sqlalchemy.py")
    myParamiko.close()  # close transport



if __name__ == '__main__':
    main()