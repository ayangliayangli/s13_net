#!/usr/bin/env python
# _*_ coding:utf-8 _*_


'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:car.py
@time(UTC+8):16/8/16-14:34
'''

#const block

import datetime
import json
import time

PRODUCT_INFO_DICT = {
    "家用电器": {
        "tv": [
            {"name": "konka", "price": 2000, "store": 20},
            {"name": "tcl", "price": 3000, "store": 20},
            {"name": "mi", "price": 1999, "store": 30},
        ],
        "air-conditions": [
            {"name": "media", "price": 2500, "store": 20},
            {"name": "green", "price": 5000, "store": 20},
            {"name": "hair", "price": 1999, "store": 30},
        ],
        "bingxiang":[
            {"name": "tcl", "price": 2500, "store": 20},
            {"name": "midea", "price": 1800, "store": 20},
            {"name": "hair", "price": 1999, "store": 30},
        ],
    },

    "pc":{
        "normal":[
            {"name": "联想", "price": 5499, "store": 20},
            {"name":  "apple", "price": 6988, "store": 20},
            {"name":"hp", "price": 6999, "store": 30},
        ],
        "game":[
            {"name": "lennovo", "price": 5499, "store": 20},
            {"name": "dall", "price": 5999, "store": 20},
            {"name": "mechrevo", "price": 6100, "store": 30},
        ],
        "inone":[
            {"name": "imac", "price": 12988, "store": 20},
            {"name": "dall", "price": 5499, "store": 20},
            {"name": "mac mini", "price": 4688, "store": 30},
        ],
    },
}

# variable block
user_logined = ""   # 当前登录的用户
current_user_info = {}
exit_flag = False   # 是否退出程序
break_outer_for_flag = False    # 是否退出外面的for循环,在login_auth（）中使用
current_dir = []  # 当前目录所在的地方
current_dir_content = []  # 当前目录下的内容
shop_history = []
shop_car = []
current_shop_product = []
login_first_flag = True


# function area


def login_auth():
    # with open("userinfo.txt", "r") as user_file:
    with open("userinfo.txt", "r", encoding="utf-8") as user_file:
        for count in range(3):
            if break_outer_for_flag:
                break
            username_inp = input("username:")
            password_inp = input("password:")
            for line in user_file.readlines():
                username, password, price = line.strip().split("|")
                if username == username_inp and password == password_inp:
                    #auth success
                    global user_logined
                    user_logined += username_inp
                    print("welcome {name:s}".format(name=username_inp))
                    global break_outer_for_flag
                    break_outer_for_flag = True   #同时跳出外面的for
                    current_user_info["username"] = username #把当前用户信息放在全局变量中
                    current_user_info["price"] = float(price)       #把当前用户信息放在全局变量中
                    break
            else:
                print("username or password is wrong")
        else:
            print("you get out , cause you are hacker i will bolck your ip")
            global exit_flag
            exit_flag = True


def cmd_ls():
    current_dir_content.clear()  # 显示的时候,先清空上次的目录内容
    len_of_current_dir = len(current_dir)
    if len_of_current_dir == 0:
        content = PRODUCT_INFO_DICT.keys()
        for index, element in enumerate(content, 1):
            print(index,element)
            current_dir_content.insert(index-1, element)
    elif len_of_current_dir == 1:
        content = PRODUCT_INFO_DICT[current_dir[0]].keys()
        for index, element in enumerate(content, 1):
            current_dir_content.insert(index-1, element)
            print(index, element)
    elif len_of_current_dir == 2:
        # show product infomation detail
        content = PRODUCT_INFO_DICT[current_dir[0]][current_dir[1]]
        for index, one_product in enumerate(content, 1):
            current_dir_content.insert(index-1, one_product["name"])
            template_print_product = '''
                                        -index:{index}--------------------
                                        name: {name}
                                        price: {price}
                                        store: {store}
                                    '''
            print(template_print_product.format(name=one_product["name"],
                                                index=index,
                                                price=one_product["price"],
                                                store=one_product["store"],))
    else:
        print("error: len_of_current_dir max is 2 min is 0")


# 判断输入的是数字还是名称,如果是数字,那就转换为目录的名字
def cmd_cd_final(dist):
    if str(dist).isnumeric():
        dist_name = current_dir_content[int(dist) - 1]
    else:
        dist_name = dist
    current_dir.append(dist_name)


def cmd_cd(dist):
    len_of_current_dir = len(current_dir)
    if dist == "..":
        # cd parrent directory
        if len_of_current_dir in [1, 2]:
            current_dir.pop()
        else:
            print("you can not cd ..")
    elif str(dist).isdigit():
        # use digital form to select production directory
        if len_of_current_dir in [0, 1] and int(dist) <= len(current_dir_content):
            cmd_cd_final(dist)
        else:
            print("there is no more directory to cd")
    else:
        # use string form to select production directory
        if len_of_current_dir == 0 and dist in PRODUCT_INFO_DICT.keys():
            cmd_cd_final(dist)
        elif len_of_current_dir == 1 and dist in PRODUCT_INFO_DICT[current_dir[0]].keys():
            cmd_cd_final(dist)
        else:
            print("cmd [cd] is wrong must be num")
    cmd_ls()


def cmd_help():
    help_info = '''
        ls  == list
        cd value == change current direction  eg: cd [dist]
        pwd == print current direction
        addtocart value ==  add product to car  eg:  addtocar [dist]
        showcart == show what's in shop car
        mycenter == show user information center
        earn  ==  earn money
        shop  == clear shop car and sub your money
        history  == history shoped

    '''
    print(help_info)


def cmd_add_to_mycar(product):
    product_full_name = ""

    if product == "":
        print("maybe you forget productname, useage: addtocart productname")
        return

    if str(product).isnumeric() and int(product) <= len(current_dir_content):
        # 产品用数字形式表达,并且数字 < 当前目录内容的总数, 把数字转换成产品
        product = current_dir_content[int(product) - 1]

    for item in PRODUCT_INFO_DICT[current_dir[0]][current_dir[1]]:

        if product == item["name"]:
            # 构造shop car 里面的数据, 判断想添加的产品,确实存在货架上
            for i in range(len(current_dir)):
                product_full_name += str(current_dir[i]).__add__("_")
            product_full_name += product
            shop_car.append(product_full_name)
            print("add to my car success")
            break
        else:
            pass
    else:
        # 轮训完了,没有找到这个商品,那么终止添加商品到shopcar的操作
        print("this product is not exist")


def cmd_mycenter():
    current_user_info_str_template = '''----------------------
                                        username:{0}
                                        price:{1}

    '''.format(current_user_info["username"], current_user_info["price"])
    print(current_user_info_str_template)


def cmd_pwd():
    print(current_dir)


def find_price(mycar):
    return_price = {}
    for product_str in shop_car:
        first_level,second_level,product_name = str(product_str).strip().split("_")
        for item in PRODUCT_INFO_DICT[first_level][second_level]:
            if product_name == item["name"] :
                return_price[product_str] = item["price"]
    return return_price


def cmd_shop():
    # check there is product in shop car
    if len(shop_car) == 0:
        print("shopcart is null, youcan use cmd [addtocart]")
        return 1

    total_price_current_time = 0
    return_price = find_price(shop_car)

    for price in return_price.values():
        total_price_current_time += float(price)
    if total_price_current_time <= float(current_user_info["price"]):
        #sub money
        current_user_info["price"] -= total_price_current_time

        #store to file
        with open("history_shop.txt", "a", encoding="utf8") as fp:
            shop_car_json = json.dumps(shop_car)
            print("shop_car_json: %s " % shop_car_json)
            print("shop_car",shop_car)
            fp.write(shop_car_json + "\n")

        # current shop infomation store to current_shop_product
        current_shop_product.extend(shop_car)

        # clear shop car
        shop_car.clear()
        print("shop success")
    else:
        print("money is not enough")
        print("total_price_current_time %f" % total_price_current_time)
        print("mymoney %f" % float(current_user_info["price"]))


def cmd_showmycar():
    # print(shop_car)
    if shop_car:
        for i in shop_car:
            print(i)
    else:
        print("你的购物车空空的,快去添加商品到购物车吧!")


def cmd_show_this_login_shoped():
    for index, item in enumerate(current_shop_product):
        print(index, item)


def cmd_show_history():
    with open("history_shop.txt", "r", encoding="utf8") as fp:
        for line in fp:
            print(line)


def cmd_earn_money():
    while True:
        earn_money = input("how much earn this time:")
        if earn_money.isnumeric():
            current_user_info["price"] += float(earn_money)
            break
        else:
            print("must be numeric")


if __name__ == '__main__':
    while True:
        debug_str = '''
        ---{time}-----------debug info-------start--------
        --------------debug info-------end--------
        '''.format(time=datetime.datetime.now(),)
        # print(debug_str)

        # print("exit_flag:{flag}".format(flag=exit_flag))
        if exit_flag:
            #exit program
            break

        if not len(user_logined):
            # must login if not login
            login_auth()
        else:
            # you can use any command if login

            #output help infomation when first login
            if login_first_flag :
                cmd_help()
                login_first_flag = False

            input_data = input("cmd(type ? for help):").strip().split(" ")
            first_argv = ""    # 要先注销,要不然上次的参数可能会对本次的有影响
            second_argv = ""   # 比如说上次的命令又两个参y数,而本次的只有一个,那么就算本次只输入一个,那么其实本次循环的时候还是又两个参数,第二个就是上次的第二个参数
            if len(input_data) == 1:
                first_argv = input_data[0]
            elif len(input_data) == 2:
                first_argv, second_argv = input_data

            # handle cmd now
            if first_argv == "exit":
                cmd_show_this_login_shoped()
                # change varable , program will stop in next iterable
                global user_logined
                global exit_flag
                user_logined = ""
                exit_flag = True
            elif first_argv == "cd" :
                print("cmd is %s" % first_argv)
                cmd_cd(second_argv)
            elif first_argv == "ls" :
                cmd_ls()
            elif first_argv == "pwd":
                cmd_pwd()
            elif first_argv == "?" or first_argv == "help":
                cmd_help()
            elif first_argv == "addtocart" :
                if second_argv:
                    print("second_args %s" % second_argv)
                    cmd_add_to_mycar(second_argv)
                else:
                    print("choose which product you want to add to shop car")
            elif first_argv == "showcart" :
                cmd_showmycar()
            elif first_argv == "earn":
                cmd_earn_money()
            elif first_argv == "mycenter" :
                cmd_mycenter()
            elif first_argv == "shop":
                cmd_shop()
            elif first_argv == "history" :
                cmd_show_history()
            elif first_argv == "":
                pass
            else:
                print("try help body ")
