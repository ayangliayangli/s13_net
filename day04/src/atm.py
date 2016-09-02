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
@time(UTC+8):16/8/27-22:13
'''

import sys, os, json, re, datetime, time
from day04.lib import common
from day04.src import atm_admin  # 使用此模块可以轻松获取到所有用户的信息,用来做对比
from day04.config import setting


all_user_info_dic = {}  # 所有用户的信息, 读出来,方便写入的时候直接覆盖写
current_user_info_dic = {}  # 当前用户信息,同时是用户已经登录了的依据


# 装饰器,判断是否是admin用户
def is_admin(func):
    def inner(*args, **kwargs):
        if current_user_info_dic["name"] == "admin":
            ret = func(*args, **kwargs)
            return ret
        else:
            print("just admin is validate")
            print("使用装饰器实现")
    return inner


# 装饰器,判断该用户是否被冻结
def is_frozen(func):
    def inner(*args, **kwargs):
        frozen_stats = int(current_user_info_dic["status"])
        if frozen_stats == 0:
            # normal
            ret = func(*args, **kwargs)
            return ret
        else:
            # frozen
            print("your account is frozen now, contact admin please")
    return inner


# 当又用户添加在另一个模块去完成的时候,就需要从文件里面去更新全局变量的内容
def update_user_info_from_file():
    # 增加用户会改变文件中的内容,所以此模块的全局变量要从文件去更新
    global all_user_info_dic
    global current_user_info_dic
    all_user_info_dic = atm_admin.fetch_all_user()
    current_user_info_dic = all_user_info_dic[current_user_info_dic["name"]]


def show_current_user():
    s = '''
        current user info as follow-------------------------
        name: {name}
        phone_no: {phone_no}
        balance: {balance}
        max_credit: {max_credit}
        current_credit: {current_credit}
        status: {status}
    '''.format(
                name=current_user_info_dic["name"],
                phone_no=current_user_info_dic["phone_no"],
                balance=current_user_info_dic["balance"],
                max_credit=current_user_info_dic["max_credit"],
                current_credit=current_user_info_dic["current_credit"],
                status=current_user_info_dic["status"],
               )
    print(s)


@is_admin
def show_all_user():
    index = 1
    for i in all_user_info_dic:
        local_current_user_info_dic = all_user_info_dic[i]
        s = '''
            index:{index}-------------------------
            name: {name}
            phone_no: {phone_no}
            balance: {balance}
            max_credit: {max_credit}
            current_credit: {current_credit}
            status: {status}
        '''.format(
                    index=index,
                    name=local_current_user_info_dic["name"],
                    phone_no=local_current_user_info_dic["phone_no"],
                    balance=local_current_user_info_dic.get("balance"),
                    max_credit=local_current_user_info_dic["max_credit"],
                    current_credit=local_current_user_info_dic["current_credit"],
                    status=local_current_user_info_dic["status"],
                   )
        print(s)
        index += 1  # 该次循环完成后,index自加1


def login():
    global all_user_info_dic
    global current_user_info_dic
    while True:
        name = input("name:")
        password = input("password:")
        password_md5_after = common.hashlib_md5(password)
        # 验证逻辑
        all_user_info_dic = atm_admin.fetch_all_user()
        if name in all_user_info_dic.keys():
            # user is exist
            if password_md5_after == all_user_info_dic[name]["password"]:
                current_user_info_dic = all_user_info_dic[name]
                # print("login success")
                show_current_user()  # 显示当前用户信息
                cmd_help()  # 显示帮助信息
                common.show_my_log("{name} authen success".format(name=name))
                break
            else:
                common.show_my_log("{name} authen failure".format(name=name))
                continue
        else:
            # user is not exist
            common.show_my_log("{name} is not exist".format(name=name))
            continue


@is_frozen
def make_bill_record(count):
    current_user_name = current_user_info_dic["name"]
    # 所有用户的账单记录
    bill_record_with_user_dic = common.read_from_file_with_json(setting.ALL_USER_BILL_RECORD_FILE_PATH)
    # 当前用户的账单记录
    bill_record_dic = bill_record_with_user_dic.setdefault(current_user_name, {})

    # 构造本次的交易时间记录
    time_stamp = time.time()
    count = int(count)
    project = input("购买了什么东西:")
    bill_record_dic[time_stamp] = {"project": project, "count": count}
    bill_record_with_user_dic[current_user_info_dic["name"]] = bill_record_dic
    common.write_to_file_with_json(bill_record_with_user_dic, setting.ALL_USER_BILL_RECORD_FILE_PATH)
    print("make bill record is success")
    return count


def show_bill_record():
    bill_record_with_user_dic = common.read_from_file_with_json(setting.ALL_USER_BILL_RECORD_FILE_PATH)
    bill_record_dict = dict(bill_record_with_user_dic.setdefault(current_user_info_dic["name"], {}))
    for i in bill_record_dict:
        # 这个i 是得到的dic的key, 也就是这笔记录发生的时间
        record = dict(bill_record_dict.get(i))
        record_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(i)))
        s = '''
            time:{time}
            project:{project}
            count:{count}
        '''.format(time=record_time,
                   project=record.get("project"),
                   count=record.get("count"))
        print(s)


@is_frozen
def store_or_draw_money(action):
    while True:
        count = str(input("how much:")).strip()
        if count.isnumeric():
            # 输入的是数字, 开始执行存钱或者取钱 逻辑
            if action == "store" or action == 1:
                # 存钱
                current_user_info_dic["balance"] += int(count)
                print("存钱成功")
            elif action == "draw" or action == 2:
                # 取钱
                if current_user_info_dic["balance"] > int(count):
                    current_user_info_dic["balance"] -= int(count)
                    print("取钱成功")
                else:
                    print("you do not have enough money")
                    break
            elif action == "yxyk" or action == 3:
                # 使用信用卡
                current_credit = int(current_user_info_dic["current_credit"])
                if int(count) <= current_credit:
                    # 信用卡的额度足够
                    make_bill_record(int(count))  # 该函数构造其他记录信息, update本次消费记录的数据到文件
                    current_user_info_dic["current_credit"] = current_credit - int(count)
                    print("刷卡成功")
                else:
                    # 信用卡的额度不够
                    print("you credit is not enough")
                    return

            # 把当前用户信息写入到文件,如果前面操作成功,如果操作失败,会直接 return
            all_user_info_dic[current_user_info_dic["name"]] = current_user_info_dic
            common.write_to_file_with_json(all_user_info_dic, setting.ALL_USER_INFO_FILE_PATH)
            common.show_my_log("action is success")
            # print(current_user_info_dic)
            show_current_user()
            break
        else:
            print("numeric is valid")
            continue


@is_frozen
def transfer_accounts():
    all_user_names = all_user_info_dic.keys()
    while True:
        dist_name = str(input("to:"))
        if dist_name not in all_user_names:
            # user is not exist
            print("user is not in system, please contact admin")
            continue
        else:
            # user is exist
            break
    while True:
        money = str(input("money:"))
        if not money.isnumeric():
            print("just numeric is valid")
            continue
        else:
            money = int(money)
            break

    # 修改相应账户的数据
    current_user_balance = current_user_info_dic["balance"]
    dist_user_info_dic = all_user_info_dic[dist_name]
    if current_user_balance < money:
        # 没有足够的钱转出
        s = '''
            you do not have enough money in you balance
            current balance: {balance}
            want to transfer: {money}
        '''.format(balance=current_user_balance, money=money)
        print(s)
    else:
        # 有足够的钱转出
        current_user_info_dic["balance"] = current_user_balance - money
        dist_user_info_dic["balance"] += money
        all_user_info_dic[dist_name] = dist_user_info_dic
        common.write_to_file_with_json(all_user_info_dic, setting.ALL_USER_INFO_FILE_PATH)
        print("transfer account is success")


@is_frozen
def credit_huankuan():
    show_current_user()
    current_credit = int(current_user_info_dic["current_credit"])
    max_credit = int(current_user_info_dic["max_credit"])
    balance = int(current_user_info_dic["balance"])
    need_to_pay = max_credit - current_credit

    # 用储蓄账户换信用账户的逻辑
    if need_to_pay == 0:
        # 不需要还款的情况
        print("you do not need to 还款")
    elif need_to_pay <= balance and need_to_pay > 0:
        # 储蓄卡余额是足够的

        # 额度恢复
        current_user_info_dic["current_credit"] = current_credit + need_to_pay
        # 储蓄卡现金减少
        current_user_info_dic["balance"] = balance - need_to_pay
        # 写进文件
        all_user_info_dic[current_user_info_dic["name"]] = current_user_info_dic
        common.write_to_file_with_json(all_user_info_dic, setting.ALL_USER_INFO_FILE_PATH)
        common.show_my_log("还款成功")
        # 显示当前用户信息
        show_current_user()
    else:
        # 储蓄卡的余额不够
        s = "you not have enough money, balance: {}, need_to_pay: {}".format(balance, need_to_pay)
        print(s)


def cmd_help():
    s = '''
    help infomation as follow --------------------------------------

    -------general operation -------
    store  == earn money
    draw   == draw money
    usecredit == use credit account money
    repayment == 自动重储蓄卡里面还款
    showbill == 显示信用卡的刷卡记录
    show == 显示当前用户状态
    trans == 向系统中的其他用户转账
    su   == 切换用户

    --------admin operation --------
    fetchuser ==  获取系统里面的所有用户
    adduser ==  添加一个用户,同时改方法可以用于修改用户的信息
    '''
    print(s)


@is_admin
def cmd_adduser():
    atm_admin.add_user()
    update_user_info_from_file()


# 程序的主函数
def main():
    print("{message:-^60}".format(message="welcome to use my ATM system"))
    print("{time:-^50}".format(time=str(datetime.datetime.now())))
    if not current_user_info_dic:
        # 未登录的情况
        login()
    while True:
        current_user_name = current_user_info_dic["name"]
        inp = input("{name}(?/help):".format(name=current_user_name))
        if inp == "":
            pass
        elif inp == "help" or inp == "?":
            cmd_help()
        elif inp == "exit" or inp == "q":
            print("thanks")
            break
        elif inp == "show":
            show_current_user()
        elif inp == "store":
            store_or_draw_money(1)
        elif inp == "draw":
            store_or_draw_money(2)
        elif inp == "usecredit":
            store_or_draw_money(3)
        elif inp == "repayment":
            credit_huankuan()  # 使用函数手动还款,自动还款怎么做??
        elif inp == "showbill":
            show_bill_record()
        elif inp == "adduser":  # admin
            cmd_adduser()
        elif inp == "fetchuser":
            show_all_user()
        elif inp == "trans":
            transfer_accounts()
        elif inp == "su":
            # 切换用户
            login()
        else:
            cmd_help()

if __name__ == '__main__':
    main()