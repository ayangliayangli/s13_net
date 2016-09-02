#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:handle_haproxy.py
@time(UTC+8):16/8/20-13:57
'''

import datetime
import time
import sys, os
import shutil

APP_DIR = os.path.dirname(os.path.abspath(__file__))  # app 的路径
OLD_FILE_PATH=os.path.join(APP_DIR, "haproxy.conf")  # 配置文件,老配置文件的路径
NEW_FILE_PATH=os.path.join(APP_DIR, "new_haproxy.conf")  # 新配置文件的路径,当输入write的时候,会使用新的文件替换老的文件
current_backend_info_dic = {}  # {"backend":[record1, record2, ... ]}


def init():
    pass


def backup_file(file):
    # backup file to db/backup  dir
    local_time_tuple = time.localtime()
    backup_file_name = os.path.join(APP_DIR,
                                    "db/backup/",
                                    time.strftime("%Y-%m-%d-%H-%M-%S", local_time_tuple))
    print(file)
    print(backup_file_name)
    print("backup success ... ")
    shutil.copy(file, backup_file_name)


def fetch(backend,file=OLD_FILE_PATH):  # 默认是打开老的配置文件
    result = []  # 清空现本函数要返回的变量,主要是给显示使用的
    current_backend_info_dic.clear()  # 清空全局变量
    with open(file, "r", encoding="utf8") as f:
        flag_is_in_backend_block = False
        for line in f:
            line_strip = line.strip()
            if line_strip.startswith("backend") and line_strip == "backend " + backend:
                flag_is_in_backend_block = True
                continue
            if flag_is_in_backend_block and line_strip.startswith("backend"):
                flag_is_in_backend_block = False
                break
            if flag_is_in_backend_block and line_strip :
                # print(line_strip)
                result.append(line_strip)
                current_backend_info_dic[backend] = result
    return result


def add(backend, record):
    backup_file(OLD_FILE_PATH)
    result_list = fetch(backend)
    if not result_list:
        # backend is not exist
        with open(OLD_FILE_PATH, "r", encoding="utf-8") as old, open(NEW_FILE_PATH, "w+", encoding="utf-8") as new:
            for line in old:
                new.write(line)
            new.write(" "*4 + "backend " + backend + "\n")
            new.write(" "*8 + record + "\n")
    else:
        # backend is exist
        if record in result_list:
            # record is exist
            print("backend is exist and record is exist , do not to modified")
            import shutil
            shutil.copy("haproxy.conf", "new_haproxy.conf")
        else:
            # backend is exist    record is not exist
            with open(OLD_FILE_PATH, "r", encoding="utf-8") as old, open(NEW_FILE_PATH, "w+",encoding="utf-8") as new:
                flag_in_backend = False
                for line in old:
                    if line.strip() == "backend " + backend and flag_in_backend == False:
                        # 进入 要操作的backend 里面了
                        result_list.append(record)
                        flag_in_backend = True  # change flage to True
                        new.write(line)
                        for new_line in result_list:
                            new.write(" "*8 + new_line + "\n")  # write all record in new file
                    if flag_in_backend == True and line.strip().startswith("backend"):
                        # 从backend 里面出来了
                        flag_in_backend = False
                        new.write(line)
                        continue
                    if flag_in_backend == False and line.strip():
                        # 其他情况
                        new.write(line)


def delete(backend, record_list):
    # backup file before delete
    backup_file("haproxy.conf")

    if backend in current_backend_info_dic.keys():
        for i in record_list:
            # remove record from current_backend_info_dic according to record_list
            current_backend_info_dic[backend].remove(i)
        if current_backend_info_dic[backend]:
            # 如果还有record
            with open(OLD_FILE_PATH, "r", encoding="utf-8") as old, open(NEW_FILE_PATH, "w", encoding="utf-8") as new:
                flag_in_backend = False
                flag_is_writed = False
                for line in old:
                    if line.strip() == "backend " + backend and flag_in_backend == False:
                        # in specified backend
                        new.write(line)
                        flag_in_backend = True
                        continue
                    elif line.strip().startswith("backend") and flag_in_backend == True:
                        # out of specified backend
                        new.write(line)
                        flag_in_backend == False
                        continue
                    elif flag_in_backend == True and flag_is_writed == False:
                        # 在backend 里面,并且修改之后的信息还没有写进去
                        for i in current_backend_info_dic[backend]:
                            new.write(" "*8 + i)
                            flag_is_writed = True
                    elif line.strip():
                        new.write(line)
        else:
            # record 已经删除完了,需要把backend 也一起删除
            with open(OLD_FILE_PATH, "r", encoding="utf-8") as old, open(NEW_FILE_PATH, "w", encoding="utf-8") as new:
                flag_in_backend = False
                for line in old:
                    if line.strip() == "backend " + backend and flag_in_backend == False:
                        # in
                        flag_in_backend = True
                        continue
                    elif line.strip().startswith("backend ") and flag_in_backend == True:
                        # out
                        new.write(line)
                        flag_in_backend = False
                        continue
                    elif flag_in_backend:
                        pass
                    elif line.strip() and not flag_in_backend:
                        new.write(line)
        print("del is success")
    else:
        print("you should fetch first")


def modified(backend, record_list):
    flag_is_in_backend = False
    flag_is_writed = False
    with open(OLD_FILE_PATH, "r", encoding="utf-8") as old, open(NEW_FILE_PATH, "w", encoding="utf-8") as new:
        for line in old:
            if line.strip() == "backend " + backend and not flag_is_in_backend:
                # start in backend
                new.write(line)
                flag_is_in_backend = True
                continue
            elif line.strip().startswith("backend") and flag_is_in_backend:
                # start out backend
                new.write(line)
                flag_is_in_backend = False
                continue
            elif flag_is_in_backend and not flag_is_writed:
                # in backend
                for i in record_list:
                    new.write(" "*8 + i + "\n")
                flag_is_writed = True
            elif not flag_is_in_backend and line.strip():
                # out backend
                new.write(line)
    print("modified success")


# test function fetch
def test_fetch():
    ret = fetch("www.yanglix.xyz")
    for i in ret:
        print(i)


def gen_record():
    server = input("server:")
    weight = input("weight:")
    maxcon = input("maxcon:")
    record_new = "server " + server + " weight " + weight + " maxcon " + maxcon
    return record_new


def print_list(mylist):
    for index, item in enumerate(mylist, 1):
        print(index, item)


def cmd_modified():
    backend = list(current_backend_info_dic.keys())[0]
    record_list = list(current_backend_info_dic[backend])
    for index,item in enumerate(record_list, 1):
        print(index, item)
    while True:
        inp = input("which one you want to modfied(type save to save)?")
        if inp == "save":
            print("program will save infomation to new_haproxy.conf")
            print("you can type write after to modified ")
            break
        elif inp == "":
            continue
        elif int(inp) in [1, 2]:
            record_new = gen_record()
        else :
            continue

        record_list.pop(int(inp) -1)
        record_list.insert(int(inp) - 1, record_new)
        print_list(record_list)
    modified(backend, record_list)


def cmd_del():
    want_to_delete_record_list = []
    for index, item in enumerate(list(current_backend_info_dic.values())[0], 1):
        print(index, item)
        while True:
            # 获取用户想要删除的数据
            inp = input("do you want to delete this record?(y/n):")
            if inp in ["y", "n"]:
                if inp == "y":
                    want_to_delete_record_list.append(item)
                elif inp == "n":
                    pass
                break
            else:
                print("just can input y or n")
                continue
    backend = list(current_backend_info_dic.keys())[0]
    delete(backend, want_to_delete_record_list)


def cmd_fetch():
    inp_backend = input("input backend:")
    ret_new = fetch(inp_backend, file=NEW_FILE_PATH)  # 这里设计的不好,每次fetch会影响全局变量,所以这里一定要先fetch new
    ret = fetch(inp_backend)
    if ret :
        print("old config ----------")
        for index, item in enumerate(ret, 1):
            print(index, item)
    else:
        print("there is no record under backend: {} in old config".format(inp_backend))

    if ret_new:
        print("new config ----------")
        for index, item in enumerate(ret_new, 1):
            print(index, item)
    else:
        print("there is no record under backend: {} in new config".format(inp_backend))

def cmd_add():
    # backend = "www.yanglix.xyz"
    # record = "server 10.0.0.250 10.0.0.251 10.0.0.252 weight 30 maxcon 1000"
    # record2 = "server 10.0.0.250 10.0.0.251 10.0.0.252 weight 20 maxcon 3000"
    print("type some necessary infomation:")
    backend = input("backend:")
    server = input("server:")
    weight = input("weight:")
    maxcon = input("maxcon:")
    record = "server " + server + " weight " + weight + " maxcon " + maxcon
    add(backend, record)


def cmd_write():
    shutil.copyfile(NEW_FILE_PATH, OLD_FILE_PATH)


def cmd_help():
    s = '''
        fetch --- fetch a record with specified backend
        del   --- del record or record list , you should fetch first
        mod   --- modified a record , you should fetch first
        add   --- add backend and record
        help  --- help information will print
        ?     --- the same as help
        write --- 永久的修改现在的配置文件,把新的零时文件直接替换程现在的文件
        q     --- quit
    '''
    print(s)
    print("current time: {:-^50} \n".format(time.ctime()))

if __name__ == '__main__':
    cmd_help()
    flag_exit = False
    while True:
        inp = input("cmd:")
        if inp == "":
            pass
        elif inp == "help" or inp == "?":
            cmd_help()
        elif inp == "q" or inp == "exit" or inp == "quit":
            print("thans use haproxy.conf modified system")
            exit(0)
        elif inp == "fetch":
            cmd_fetch()
        elif inp == "add":
            cmd_add()
        elif inp == "bk":
            backup_file("haproxy.conf")
        elif inp == "del":
            cmd_del()
        elif inp == "mod":
            cmd_modified()
        elif inp == "write":
            cmd_write()
        else:
            print("maybe you are wrong input, help information as follow")
            cmd_help()
