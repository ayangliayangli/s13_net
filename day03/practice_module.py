#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:practice_module.py
@time(UTC+8):16/8/21-12:51
'''


# 模块分类
# 内置模块    sys os time datetime
# 三方模块    func ansible
# 自己编写的模块 yangli yangli2 yangli3

# 作用:   代码归类   代码重用
# attention: 自己的模块名字,千万不能和系统的冲突,import的时候会优先在当前目录找!!!

# 模块导入方式
# import module_name
# from package import *
# from package import module_name as alias_name

print("-------module--import------------")
import s1
from lib import s1 as lib_s1
s1.f1()
s1.f2()
lib_s1.f1()






# 序列化
# json    跨平台,  仅仅支持基本数据类型
# pickle  支持丰富的自定义类  但是只能python使用
print("{var:-^50}".format(var="json"))
import json
dic = {"k1": "v1", "k2": "v2"}
dic_str = json.dumps(dic)
print("type: {}".format(type(dic_str)))    #str
print(dic_str)
dic_str_dic = json.loads(dic_str)
print("type: {}".format(type(dic_str_dic)))    #dict
print(dic_str_dic)


# json.dump()  json.load()
print("{:-^50}".format("dump-load"))
myli = [1, 2, 3, 4, 5]
json.dump(myli, open("info.json", "w", encoding="utf-8"))
ret = json.load(open("info.json", "r", encoding="utf-8"))
print(ret, type(ret))


# mystr = '{"k1": "v1", "k2": "v2"}'  # 注意,这里外面就要是单引号,里面是双引号
# print(type(json.loads(mystr)))
# print(json.loads(mystr))



# time datetime
print("{:-^50}".format("time"))
import time
import datetime
print(time.time())
print(time.ctime())
print(time.ctime(time.time() - 3600))
print(time.gmtime())
print(time.localtime())
print(time.mktime(time.localtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))   # structme  -- > str_time
print(time.strptime("16-08-21 15:05:45", "%y-%m-%d %H:%M:%S"))  # str_time --> structime

print("{:-^50}".format("datetime"))
print(datetime.datetime.now())
print(datetime.datetime.now() + datetime.timedelta(days=-1))  # timedelta,根据当前时间推算
print(datetime.datetime.now().replace(2010, 9, 1))  # timereplace 直接替换时间

# 时间可以比较大小
is_small_flag = datetime.datetime.now() > datetime.datetime.now() + datetime.timedelta(days=10)
print(is_small_flag)







# module :     logging
print("{:-^50}".format("logging"))
import logging
# 讲日志写在文件中,这里写入的方式是追加 a
# 日志前面加上时间
logging.basicConfig(filename="example_logging.log", level=logging.INFO,
                    format="%(asctime)s %(message)s",
                    datefmt="%d/%m/%Y %H:%M:%S")
logging.debug("this is debug log")
logging.info("this is info log")
logging.warning("this is warning log")
logging.error("this is error log")
logging.critical("this is critical log")


#常用方法 loggin
# get loger first
print("{:-^50}".format("logging to file and stream(console)"))

my_loger = logging.getLogger("TEST-LOG")
my_loger.setLevel(logging.DEBUG)

# get handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("file_handler.log")
file_handler.setLevel(logging.INFO)

# get formater
stream_formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(message)s")
file_formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")

# related logger handler formatter
stream_handler.setFormatter(stream_formatter)
file_handler.setFormatter(file_formatter)
my_loger.addHandler(stream_handler)
my_loger.addHandler(file_handler)

# start use my_loger
my_loger.debug("this is debug log")
my_loger.info("this is info log")
my_loger.warning("this is warning log")
my_loger.error("this is error log")
my_loger.critical("this is critical log")
