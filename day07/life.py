#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:life.py
@time(UTC+8):16/9/7-15:39
'''
import random


class People(object):
    def __init__(self, name, gender, age, work="",
                 species="yellow", country="china", balance=0, speciality="", house="", car="",
                 bf="", gf="", husband="", wife="", ex=""):
        self.name = name
        self.gender = gender
        self.age = age
        self.work = work
        self.species = species
        self.country = country
        self.balance = balance
        self.speciality = speciality
        self.house = house
        self.car = car
        self.bf = bf
        self.gf = gf
        self.husband = husband
        self.wife = wife
        self.ex = ex

    def __str__(self):
        s = '''
            user center infomation as following:
            name---{name}
            gender---{gender}
            age---{age}
            work---{work}
            species---{species}
            country---{country}
            balance---{balance}
            speciality---{speciality}
            house---{house}
            car---{car}
            bf---{bf}
            gf---{gf}
            husband---{husband}
            wife---{wife}
            ex---{ex}
        '''.format(name=self.name, gender=self.gender, age=self.age,
                   work=self.work, species=self.species, country=self.country,
                   balance=self.balance, speciality=self.speciality, house=self.house, car=self.car,
                   bf=self.bf, gf=self.gf, husband=self.husband, wife=self.wife, ex=self.ex)
        return s

    def fall_in_love(self, other_people):
        if self.gender == other_people.gender:
            if self.country == "china" or other_people.country == "china" :
                # 性别相同
                print("性别相同")
                return
        if self.gender == "male":
            other_people.bf = self.name
            self.gf = other_people.name
        elif self.gender == "female":
            other_people.gf == self.name
            self.bf = other_people.name

    def break_love(self, other_people):
        if self.gender == "male":
            self.gf = ""
            other_people.bf = ""
        elif self.gender == "female":
            self.bf = ""
            other_people.bf = ""
        else:
            print("it is impossible")

    def work_hard(self):
        # 每次工作,资产 * 1.1
        self.balance = float(self.balance) * 1.1

    def work_lazy(self):
        # 每次不工作,资产 * 0.9
        self.balance = float(self.balance) * 0.9

    def shop_car(self):
        # 为了简单,直接购买jeep , 合计50万RMB
        jeep_price = 500000
        if self.balance >= jeep_price:
            self.balance -= jeep_price
            self.car = "jeep"
            print("购买成功")
        else:
            print("you do not have enough money")

    def sale_car(self):
        # 为了简单, 假设世界上只有一辆车,jeep,价格500000
        # 二手的价格是 30万
        jeep_price_second = 300000
        if self.car:
            # have a car
            self.car = ""
            self.balance += 300000
        else:
            # do not have car
            print("you do not have a car for sale")


def people_list_print(*args, **kwargs):
    for i in args:
        print(i)


# 测试住函数
def main():
    # yangli = People("yangli", "male", 25, "linux os",balance=9999999)
    # print(yangli)
    John = People("John", "male", 25, "IT",balance=11000)
    Liz = People("Liz", "female", 25, "",balance=10000)
    Peter = People("Peter", "male", 30, "doctor",balance=800000, car="jeep")

    people_list_print(John, Liz, Peter)

    print("{:+^50}".format("John fall in love with Liz"))
    John.fall_in_love(Liz)
    people_list_print(John, Liz, Peter)

    print("{:+^50}".format("John break love with Liz"))
    Liz.break_love(John)
    people_list_print(John, Liz, Peter)

    # print("{:+^50}".format("John work hard 10"))
    # for i in range(10):
    #     if random.randrange(0,10) < 1:
    #         # John 开始努力工作,90%的时间都在努力工作,剩下的10%的时间会头休息一下
    #         John.work_lazy()
    #     else:
    #         John.work_hard()
    # print(John)



    print("{:+^50}".format("John work hard 101"))
    work_hard_count_john = 0
    work_lazy_count_john = 0
    for i in range(101):
        if random.randrange(0, 10) < 2:
            # John 开始努力工作,80%的时间都在努力工作,剩下的10%的时间会休息一下
            print("John work lazy ... balance * 1.1")
            work_lazy_count_john += 1
            John.work_lazy()
        else:
            print("John work hard ... banlance * 0.9")
            work_hard_count_john += 1
            John.work_hard()
    print("static infomation ------work_hard:{}  work_lazy:{} ".format(work_hard_count_john, work_lazy_count_john))
    print(John)



    print("{:+^50}".format("Peter work 101"))
    for i in range(101):
        if random.randrange(0,10) < 2:
            # Peter 开始工作,20%的时间都在努力工作,剩下的80%的时间在休息
            Peter.work_hard()
        else:
            Peter.work_lazy()
    print(Peter)

    print("{:+^50}".format("John shop a car"))
    John.shop_car()
    print(John)



    # 如果John 现在的资产 和 Peter 差不多,或者更高
    if John.balance >= Peter.balance * 0.8:
        s = '''
            Liz:
            你在时,你是全世界
            你不在时,全世界都是你
            而我,路过了你的全世界
            希望你一切都好, 能遇到你已是我今生荣幸, 你一定要每天都快乐, 就算没有我 ...
        '''
    else:
        s = '''
            逆袭失败,再次重来
        '''
    print(s)


if __name__ == '__main__':
    main()