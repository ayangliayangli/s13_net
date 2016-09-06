#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
@version:
@author: leo Yang
@license: none
@contact: yangliw3@foxmail.com
@site:
@software:PyCharm
@file:course.py
@time(UTC+8):16/9/4-15:50
'''

import sys, os, pickle
from day06.config import setting
import datetime, time

# 下面两个方法是工具方法,本来想写在一个单独的lib里面的,方便王指导看,就在这里了吧


def write_object_to_file_with_pickle(obj,file):
    # 把obj 写入 file, 使用pickle 模块
    with open(file, "wb",) as fp:
        pickle.dump(obj, fp)


def read_object_from_file_with_pickle(file):
    # read object from file with pickle module --> return obj
    # do not known which tpye
    with open(file, "rb",) as fp:
        obj = pickle.load(fp)
        return obj


class People():
    def __init__(self, name, password, gender, age, assets=0, ):
        self.name  = name
        self.password = password
        self.gender = gender
        self.age = age
        self.assets = assets

    def show(self):
        s = '''
            infomation as following--------
            name={name}
            gender={gender}
            age={age}
            assets={assets}
        '''.format(name=self.name,
                   gender=self.gender,
                   age=self.age,
                   assets=self.assets,
                   )
        print(s)


class Students(People):
    def __init__(self, name, password, gender, age, assets=0, course_list=[], course_record={}):
        self.course_list = course_list
        self.course_record = course_record
        super(Students, self).__init__(name, password, gender, age, assets)

    def show(self):
        super(Students, self).show()  # 先执行父类的show（） 显示基本信息
        print("class have choosed:")
        for index, item in enumerate(self.course_list, 1):  # 显示选课信息
            print("             ", index, item.name)

    @staticmethod
    def fetch_all_students():
        ret = read_object_from_file_with_pickle(setting.STUDENTS_FILE_PATH)
        return ret

    @staticmethod
    def set_all_students(students_list):
        write_object_to_file_with_pickle(students_list, setting.STUDENTS_FILE_PATH)

    @staticmethod
    def fetch_a_student(name):
        students = Students.fetch_all_students()
        for i in students:
            if i.name == name:
                return i
        else:
            return None

    @staticmethod
    def set_a_student(student):
        students_in_file = Students.fetch_all_students()
        for i in students_in_file:
            if i.name == student.name:
                students_in_file.remove(i)
                break
        else:
            pass

        students_in_file.append(student)
        Students.set_all_students(students_in_file)

    @staticmethod
    def new_student():
        print("input some necessary infomation")
        name = input("name:")
        password = input("password:")
        gender = input("gender:")
        age = input("age:")
        assets = input("assets:")

        obj_student = Students(name, password, gender, age, assets)
        Students.set_a_student(obj_student)

    def have_class(self, course_name):
        pass

    def choose_class(self):
        courses = Course.fetch_all_course()
        for index, item in enumerate(courses, 1):
            print(index, item.name)
        inp = input("which one class do you choose:")
        inp_int = int(inp)
        if inp_int <= len(courses):
            # 输入在允许的范围之内
            self.course_list.append(courses[inp_int - 1])
            Students.set_a_student(self)
        else:
            print("out of range")


class Teachers(People):
    def __init__(self, name, password, gender, age, assets=0, course_list=[]):
        super(Teachers, self).__init__(name, password, gender, age, assets)
        self.course_list = course_list

    @staticmethod
    def fetch_all_teacher():
        ret = read_object_from_file_with_pickle(setting.TEACHERS_FILE_PATH)
        return ret

    @staticmethod
    def set_all_teacher(teachers_list):
        write_object_to_file_with_pickle(teachers_list, setting.TEACHERS_FILE_PATH)

    @staticmethod
    def fetch_a_teacher(name):
        teachers = Teachers.fetch_all_teacher()
        for teacher in teachers:
            if teacher.name == name:
                # 有该老师
                return teacher
        else:
            # 没有该老师
            return None

    @staticmethod
    def set_a_teacher(teacher):
        teachers = Teachers.fetch_all_teacher()
        for i in teachers:
            if i.name == teacher.name:
                teachers.remove(i)
                break

        teachers.append(teacher)
        Teachers.set_all_teacher(teachers)

    @staticmethod
    def new_teacher():
        print("input some necessary infomation")
        name = input("name:")
        password = input("password:")
        gender = input("gender:")
        age = input("age:")
        assets = input("assets:")

        teacher_obj = Teachers(name, password, gender, age, assets)
        # 把该新建的老师添加进去
        Teachers.set_a_teacher(teacher_obj)

    def have_class(self, course_name):
        pass


class Course():
    def __init__(self, name, teacher, pay_per_class, class_time = time.time() ):
        # 经过考虑,把student_list students_comment 设计在学生中,course取消
        self.name = name
        self.teacher = teacher
        self.pay_per_class = pay_per_class
        self.class_time = class_time

    def __get_courses(self):
        ret = read_object_from_file_with_pickle(setting.COURSES_FILE_PATH)
        return ret

    def __set_courses(self, values):
        # 这里传进来的values 需要是一个 list
        write_object_to_file_with_pickle(values, setting.COURSES_FILE_PATH)

    all_courses = property(fget=__get_courses, fset=__set_courses)
    # 这里使用property,来从文件中获取所有的 courses 数据, 以及充文件中拿到所有的 courses 数据
    # 使用开源中常用的 foo = property(fget=func1, fget=func2, fdel=func3) 的方式
    # 在这里灵活活的使用了私有方法,保证数据的安全性

    def show(self):
        s = '''
            ----------------
            name:{name}
            teacher:{teacher}
            pay_per_class:{pay_per_class}
            class_time: {class_time}
        '''.format(name=self.name,
                   teacher=self.teacher,
                   pay_per_class=self.pay_per_class,
                   class_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(self.class_time)))
        print(s)


    @staticmethod
    def fetch_all_course():
        courses = read_object_from_file_with_pickle(setting.COURSES_FILE_PATH)
        return courses

    @staticmethod
    def fetch_a_course(course_name):
        courses = Course.fetch_all_course()
        for course in courses:
            if course.name == course_name:
                # 找到了指定的课程
                return course
        return None
        # 如果循环完了,没有找到,那说明不存在这个课程

    @staticmethod
    def set_all_courses(objs):
        write_object_to_file_with_pickle(objs, setting.COURSES_FILE_PATH)
        # Course.all_courses = objs  # 这个是错误的用法, property 只能使用 obj 调用

    def set_a_course(self):
        courses = self.fetch_all_course()
        for course in courses:
            if self.name == course.name:
                # 有相同的课程, 先删除
                courses.remove(course)
                break
        else:
            # 循环完,没有找到同名课程,直接插入
            pass

        courses.append(self)
        Course.save_courses_to_file(courses)  # 这里使用静态变量







# 下面是测试的方法 main()
def test():
    yangli = People("yangli","123456", "male", 25, 10000)
    yangli.show()

    student_yangli = Students("yanglistu", "123456", "male", 15, 1000)
    student_yangli.show()


def test_write_data_to_file():
    s1 = Students("yanglistu1", "123456", "male", 15, 1000)
    s2 = Students("yanglistu2", "123456", "male", 15, 1000)
    s3 = Students("yanglistu3", "123456", "male", 15, 1000)
    s_list = []
    s_list.append(s1)
    s_list.append(s2)
    s_list.append(s3)
    write_object_to_file_with_pickle(s_list, setting.STUDENTS_FILE_PATH)

    student_list = read_object_from_file_with_pickle(setting.STUDENTS_FILE_PATH)
    for i in student_list:
        # ??? 这里如何能够让i显示的转换成 studens对象
        i.show()


def test_course():
    obj_course1 = Course("math", "hefuqiang", 50)
    obj_course2 = Course("chinese", "hejun", 55)
    course_list = [obj_course1, obj_course2]
    # write_object_to_file_with_pickle(course_list, setting.COURSES_FILE_PATH)
    Course.set_all_courses(course_list)  # 使用静态方法, 该静态方法内部会使用property
    # obj_course1.all_courses = course_list  # 这里有坑, property obj 调用, class 不能调用

    ret = Course.fetch_a_course("math")
    print(ret)
    ret.show()


def test_property_all_courses():
    obj1 = Course("math1", "hefuqiang1", 60)
    obj2 = Course("math2", "hefuqiang2", 70)
    objs = [obj1, obj2]  # 设计的是 courses 放在一个list里面,然后再通过pickle放入文件中

    obj1.all_courses = objs

    for i in obj1.all_courses:
        i.show()


def test_teachers():
    obj1_teacher = Teachers("hefuqiang", "123456", "male", 35, 10000)
    obj2_teacher = Teachers("hefuqiang2", "1234567", "male", 35, 10000)
    objs = [obj1_teacher, obj2_teacher]
    Teachers.set_all_teacher(objs)  # 把所有老师直接写入文件
    Teachers.new_teacher()  # 交互式的新建一个老师, 名字如果与上面的相同,那么会覆盖掉
    ret = Teachers.fetch_all_teacher()
    for i in ret:
        i.show()


def test_students():
    obj1_students = Students("yangli1", "123456", "male", 25, 1000)
    obj2_students = Students("yangli2", "1234567", "male", 25, 1000)
    objs = [obj1_students, obj2_students]
    Students.set_all_students(objs)  # 把所有学生直接写入文件
    Students.new_student()  # 交互式的新建一个学生, 名字如果与上面的相同,那么会覆盖掉
    ret = Students.fetch_all_students()
    for i in ret:
        i.show()


def test_student_choose_class():
    obj1_students = Students("yangli_choose", "123456", "male", 25, 1000)
    obj1_students.choose_class()
    obj1_students.show()

    obj_student_yangli_choose = Students.fetch_a_student("yangli_choose")  # 去文件中拿这个学生,然后再选课
    obj_student_yangli_choose.choose_class()
    obj_student_yangli_choose.show()


if __name__ == '__main__':
    # test_write_data_to_file()
    # test_course()
    # test_property_all_courses()
    # test_teachers()
    # test_students()
    test_student_choose_class()