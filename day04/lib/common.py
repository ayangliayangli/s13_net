#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:common.py
@time(UTC+8):16/8/24-23:03
'''

import hashlib, time, os, sys
import logging
import json
from day04.config import setting


def hashlib_md5(origin_str):
    key = "dsfjasdj.$@fkas&dfdf"
    obj = hashlib.md5(bytes(key, encoding="utf-8"))
    obj.update(bytes(origin_str, encoding="utf-8"))
    ret = obj.hexdigest()
    return ret


def show_my_log(message, type=3, level=2):
    # message is infomation want to log
    # type 1:console  2:file  3:both console and file
    # default both file and console  default info level
    log_file_path = os.path.join(setting.APP_DIR, "log", "atm.txt")
    my_logger = logging.getLogger("ATM-LOG")
    my_logger.setLevel(logging.DEBUG)

    sh = logging.StreamHandler()
    fh = logging.FileHandler(log_file_path)
    sh.setLevel(logging.DEBUG)
    fh.setLevel(logging.DEBUG)

    formater = logging.Formatter("%(asctime)s-%(levelname)s-%(name)s: %(message)s")
    sh.setFormatter(formater)
    fh.setFormatter(formater)

    if type == 1:
        my_logger.addHandler(sh)
    elif type == 2:
        my_logger.addHandler(fh)
    elif type == 3:
        my_logger.addHandler(sh)
        my_logger.addHandler(fh)
    else:
        print("show_my_log: type is wrong , 1 2 3 is valid")
        return 1

    if level == "debug" or level == 1:
        my_logger.debug(message)
    elif level == "info" or level == 2:
        my_logger.info(message)
    elif level == "error" or level == 3:
        my_logger.error(message)
    elif level == "critical " or level == 4:
        my_logger.critical(message)
    return 0


def write_to_file_with_json(my_dict, file_path):
    with open(file_path, "w", encoding="utf-8") as fp:
        json.dump(my_dict, fp)
        return 0
    return 1


def read_from_file_with_json(file_path):
    # 确定返回的是一个字典
    ret = {}
    with open(file_path, "r", encoding="utf-8") as fp:
        file_content = fp.read()
        if file_content:
            # 文件中又内容
            ret = dict(json.loads(file_content))
        else:
            # 文件中没有内容
            pass
        return ret


if __name__ == '__main__':
    # for i in range(100):
    #     time.sleep(1)
    #     s = "dsfasdfasdfasdfasdf" + str(i)
    #     print(i, hashlib_md5(s))
    ret = show_my_log("this is test infomation just file", 3, 3)
    ret = show_my_log("this is test infomation just file", 3, 3)
    print(ret)
    # li = [1, 2, 3]
    # ret = write_to_file_with_json(li, "example.json")


