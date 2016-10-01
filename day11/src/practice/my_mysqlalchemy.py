#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:my_mysqlalchemy.py
@time(UTC+8):16/9/29-15:40
'''


import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship

# engine_str = "mysql+pymysql://yangli:yanglipass@office.yanglix.xyz:33306/s13_net"
engine_str = "mysql+pymysql://yangli:yanglipass@192.168.126.250:3306/s13_net"
engine = create_engine(engine_str, max_overflow=5)
Base = declarative_base()


# class  -- table
# global_var -- column
# object -- row

# create sigle talbe
class User(Base):
    __tablename__ = '_t_users'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    extra = Column(String(32))

    __table_args__ = (
        UniqueConstraint('id', 'name', name='uix_id_name'),
        Index('ix_id_name', 'name', 'extra'),
    )

    def __str__(self):
        s = '''
        -----------------------------------------
        id:{}  name:{}   extra:{}
        '''.format(self.id, self.name, self.extra)
        return s


# 一对一的关系 ForeignKey()

class Favor(Base):

    __tablename__ = '_t_favor'
    id = Column(Integer, primary_key=True, autoincrement=True)
    caption = Column(String(50), default='red', unique=True)


class Person(Base):

    __tablename__ = '_t_person'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=True, index=True)
    favor_id = Column(Integer, ForeignKey("_t_favor.id"))
    # 这个不影响表结构, 只是方便这个正想查询和反响查询,不用自己join
    favor = relationship(Favor, backref="person")


# many-to-many

class Group(Base):
    __tablename__ = '_t_group'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(32), unique=False, nullable=True)

    def __str__(self):
        s = 'Group object: id:{} name:{}'.format(self.id,self.name)
        return s


class Server(Base):
    __tablename__ = '_t_server'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(32), unique=True, nullable=False)
    ip = Column(String(32), nullable=False, unique=False)
    port = Column(Integer, default=22)


class ServerToGroup(Base):
    __tablename__ = '_t_servertogroup'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    server_id = Column(Integer, ForeignKey('_t_server.id'))
    group_id = Column(Integer, ForeignKey('_t_group.id'))

    servers = relationship(Server, backref="middle")
    groups = relationship(Group, backref="middle")




def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


def get_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def add_obj():
    session = get_session()
    yangli = User(name='yangli', extra='gen')
    session.add(yangli)
    session.add_all([
        User(name='yangli1', extra='gen1'),
        User(name='yangli2', extra='gen2'),
        User(name='yangli2', extra='gen2'),
        User(name='yangli3', extra='gen3'),
    ])
    session.commit()
    print("add_obj end ---")


def add_favor():
    session = get_session()
    session.add_all([
        Favor(caption="red"),
        Favor(caption="blue"),
        Favor(caption="yellow"),
    ])
    session.commit()


def add_person():
    session = get_session()
    session.add_all([
        Person(name="yangli1", favor_id=1),
        Person(name="yangli2", favor_id=1),
        Person(name="yangli3", favor_id=1),
        Person(name="dujuan1", favor_id=2),
        Person(name="dujuan2", favor_id=2),
    ])
    session.commit()


# 正向查找
def select_person_with_favor():
    session = get_session()
    ret = session.query(Person).all()
    for obj in ret:
        print(obj, obj.favor.caption)  # this is attention


# 反向查找
def select_favor_with_person():
    session = get_session()
    obj = session.query(Favor).filter(Favor.id==1)[0]
    persons = obj.person  # this is attention
    print(persons)

def del_obj():
    session = get_session()
    session.query(User).filter(User.id > 2).delete()
    session.commit()

def update_obj():
    session = get_session()
    # session.query(User).filter(User.id >2).update({'name':'dujuan'})
    session.query(User).filter(User.id >2).update({User.name:User.name + '99'}, synchronize_session=False)
    # session.query(User).filter(User.id >2).update({User.name:User.name + '99'}, synchronize_session="evaluate")
    session.commit()

def select_obj():
    session = get_session()
    ret = session.query(User).all()
    ret1 = session.query(User).filter(User.id > 2).all()
    # filter  relationship --- and
    ret2 = session.query(User).filter(User.id > 2, User.name == 'yangli1').all()



    for i in ret2:
        print(i)


def add_group():
    session = get_session()
    session.add_all([
        Group(name="g1"),
        Group(name="g2"),
        Group(name="g3"),
    ])
    session.commit()


def add_server():
    session = get_session()
    session.add_all([
        Server(name="host1", ip="192.168.1.251", port="22"),
        Server(name="host2", ip="192.168.1.252", port="22"),
        Server(name="host3", ip="192.168.1.253", port="6322"),
    ])
    session.commit()


def add_server_to_group():
    session = get_session()
    session.add_all([
        ServerToGroup(server_id=1, group_id=1),
        ServerToGroup(server_id=2, group_id=1),
        ServerToGroup(server_id=3, group_id=1),
        ServerToGroup(server_id=1, group_id=2),
        ServerToGroup(server_id=2, group_id=2),
    ])
    session.commit()


def select_servers_specified_group_via_traditional():
    # 查看一个主机属于哪些组
    session = get_session()
    server_obj = session.query(Server).filter(Server.name=="host1").first()
    server_to_group_obj = session.query(ServerToGroup.server_id, ServerToGroup.group_id).filter(ServerToGroup.server_id==server_obj.id).all()
    # server_to_group_obj [(1, 1), (1, 2), (1, 1), (1, 2)]
    group_ids = list(zip(*server_to_group_obj))[1]  # 在python3里面zip返回的是一个刻迭代的对象,所以要转换一下才能使用
    print(group_ids)
    groups = session.query(Group.name).filter(Group.id.in_(group_ids)).all()
    print(groups)


def select_servers_specified_group_via_new():
    # 查看一个主机属于哪些组
    session = get_session()
    middles = session.query(Server).filter(Server.name=="host1").first().middle
    for item in middles:
        print(item.groups)

if __name__ == '__main__':
    # init_db()  # 创建表格
    # drop_db()  # 删除所有表格
    # add_obj()
    # del_obj()
    # for i in range(10):
    #     print('{}th'.format(i))
    #     update_obj()

    # select_obj()
    # add_favor()
    # add_person()
    # select_person_with_favor()
    # select_favor_with_person()
    # add_group()
    # add_server()
    # add_server_to_group()
    # select_servers_specified_group_via_traditional()
    select_servers_specified_group_via_new()