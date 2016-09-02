#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:gen_static_confi.py
@time(UTC+8):16/8/22-22:03
'''


import sys, os, re

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)
current_app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(current_app_dir)

# from . import network
from bw_work_project.etc_static_nodes.lib import network
# from lib import network

import json
import time
import pprint


APP_DIR = ""
peers_info = []
old_peers_info = []


def init():
    current_app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(current_app_dir)
    # sys.path.append(current_dir)
    global APP_DIR
    APP_DIR = current_app_dir
    # from lib import network
    for i in sys.path:
        print(i)


def load_src_config_file():
    src_config_full_path = os.path.join(APP_DIR, "db/srcinfo.txt")
    print(src_config_full_path)
    with open(src_config_full_path, "r", encoding="utf-8") as old:
        current_id_final = ""
        for line in old.readlines():
            line_strip = line.strip()
            if line_strip.startswith("id: "):
                current_id = re.search("\".*\"", line_strip).group()
                current_id_final = re.sub("\"", "", current_id)
                # print(current_id_final)
            if line_strip.startswith("remoteAddress: "):
                remote_ip = re.search("\".*\"", line_strip).group()
                remote_ip_final = re.sub("\"", "", remote_ip)
                remote_ip_final2 = re.sub(":.*?$", ":30303", remote_ip_final)
                print("----------------{}".format(remote_ip_final2))

                one_node_info = "\"enode://" \
                                + current_id_final \
                                + "@" \
                                + remote_ip_final2 \
                                + "\","
                peers_info.append(one_node_info)
                print(one_node_info)


def print_list(my_list):
    for index,i in enumerate(my_list, 1):
        print(index,i)


def load_static_nodes():
    static_nodes_full_path = os.path.join(APP_DIR, "db/static-nodes.json.etc.default")
    with open(static_nodes_full_path, "r", encoding="utf-8") as new:
        for line in new:
            if line.strip().startswith("\"enode://"):
                old_peers_info.append(line.strip())
    print_list(old_peers_info)


def test_peers_port(peers_info_list, timeout=5):
    peers_info_connected_success = []
    for i in peers_info_list:
        host = re.findall("@(.*?):", i)[0]
        port = 30303
        ret = network.test_connection(host=host, port=port, timeout=timeout)
        if ret == 0:
            # test host port is success
            print("+++++++++++++++++success: {}:{}".format(host, port))
            peers_info_connected_success.append(i)

        else:
            # test host port is failure
            print("-----------------failure: {}:{}".format(host, port))
    return peers_info_connected_success


def gen_new_static_config():
    peers_info_set = set(peers_info)
    old_peers_info_set = set(old_peers_info)
    peers_union = peers_info_set | old_peers_info_set
    print_list(peers_union)

    # test port
    while True:
        # select whether need test connect port
        inp = input("do you want to test node connection(y/n):")
        if inp == "y":
            # 获取超时时间
            while True:
                # select timeout seconds default 5s
                timeout = input("connection timeout(default:5s):")
                if timeout.isnumeric():
                    peers_info_connected_success = test_peers_port(peers_union, int(timeout))
                    break
                elif timeout == "":
                    peers_info_connected_success = test_peers_port(peers_union)
                    break
                else:
                    print("just numeric is validate")
                    continue
            break
        elif inp == "n":
            peers_info_connected_success = peers_union
            break
        elif inp == "":
            continue
        else:
            print("just y and n is validate")
            continue

    # wirte to new config file
    static_nodes_new_full_path = os.path.join(APP_DIR, "db/static-nodes.json.etc.new")
    len_of_peers_info_connected_success = len(peers_info_connected_success)
    with open(static_nodes_new_full_path, "w", encoding="utf-8") as new:
        new.write("[\n")
        for index, item in enumerate(peers_info_connected_success, 1):
            if index == len_of_peers_info_connected_success:
                # 如果是最后一行,去掉逗号
                item_new = re.findall("(.*),", item)[0]
                new.write("\t" + item_new + "\n")
                continue
            else:
                new.write("\t" + item + "\n")

        new.write("]")
        print("config file is generated ... bli")


if __name__ == '__main__':
    init()
    # time.sleep(5)
    load_src_config_file()
    print("{:-^60}".format("load_static_nodes"))
    load_static_nodes()
    print("{:-^60}".format("new_peers_info_tuple"))
    gen_new_static_config()

