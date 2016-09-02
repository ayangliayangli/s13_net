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
@time(UTC+8):16/8/30-22:44
'''

import paramiko

host = "192.168.3.200"
port = 22
username = "root"
password = "123456"

# execute cmd via username and password
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port=port, username=username, password=password)
stdin, stdout, stderr = ssh.exec_command("df -hT")
print(stdout.read())
ssh.close()

# 传输文件 via sftp
t = paramiko.Transport((host, port))
t.connect(username=username, password=password)
sftp = paramiko.SFTPClient.from_transport(t)

# sftp.get("/tmp/haha.txt", "/tmp/haha.txt")
sftp.put("myre.py", "/tmp/myre.py")

sftp.close()
print("transfer file success")
