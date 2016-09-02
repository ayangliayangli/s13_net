#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:atm.py
@time(UTC+8):16/8/26-22:48
'''

import re, sys, os, json, pprint
from day04.config import setting
from day04.lib import common


user_info_dict = {
                 "name": "", "password": "", "phone_no": "",
                 "balance": "",
                 "current_credit": "", "max_credit": "",
                 "status": "",  # 0--normal  1--frozen
                 }


def fetch_all_user():
    # 这里有个坑,对于文件,当使用了read()后,如果再次读文件,那么读出来的将是空
    # 所以建议以后如果需要去文件内容,就直接把所有的内容读出来放到一个变量中,然后在使用
    # 比如本例中的file_content
    user_info_file_path = os.path.join(setting.APP_DIR, "db", "user_info.json")
    with open(user_info_file_path, "r", encoding="utf-8") as user_info_file:
        file_content = user_info_file.read().strip()
        print(file_content)
        if file_content == "":
            user_info_dict = {}
            print("user is null")
        else:
            user_info_dict = json.loads(file_content)
    return user_info_dict


def input_user_info():
    current_user_info_dic = {}

    print("start to add user, you must input some userful infomation ")
    name = input("name:")
    password = input("password:")
    phone_no = input("phone_no:")
    max_credit = input("maxcredit:")
    current_credit = input("current_credit:")
    balance = input("current_balance:")
    status = input("status:")

    current_user_info_dic["name"] = name
    current_user_info_dic["password"] = password
    current_user_info_dic["phone_no"] = phone_no
    current_user_info_dic["max_credit"] = int(max_credit)
    current_user_info_dic["current_credit"] = int(current_credit)
    current_user_info_dic["balance"] = int(balance)
    current_user_info_dic["status"] = status

    return current_user_info_dic


def add_user():
    # 设计思路, 把所有的用户读出来,修改,然后再覆盖
    all_user_info = fetch_all_user()
    current_user_info = input_user_info()

    # 密码使用md5算法加密,在存储
    password_md5_after = common.hashlib_md5(current_user_info["password"])
    current_user_info["password"] = password_md5_after
    # update all_user_info
    all_user_info[current_user_info["name"]] = current_user_info
    # override db
    # user_info_file_path = os.path.join(setting.APP_DIR, "db", "user_info.json")
    # with open(user_info_file_path, "w", encoding="utf-8") as user_info_file:
    #     json.dump(all_user_info, user_info_file)
    # 利用自己在common module 写的函数,把当前用户信息直接写到文件
    # 目录只是使用在setting中设置的
    common.write_to_file_with_json(all_user_info, setting.ALL_USER_INFO_FILE_PATH)
    print(current_user_info)  # 打印当前用户信息
    print("add user success")



if __name__ == '__main__':
    # fetch_all_user()  # pass
    add_user()  # pass
