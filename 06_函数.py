#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/11 15:25 
# @Author : TETE
# @File : 06_函数.py

# 1.函数形式：
# def method(a):
#     '''
#
#     :param a:
#     :return:
#     '''
#     print(a)
#
# method(2)

# 2.增加return
# def method(a):
#     print(a)
#     return a+3
#
# print(method(2))

# 3.函数默认值
# def method(a,b=[]):
#     b.append(a)
#     return b
#
# print(method(1))
# print(method(2))

# 4.关键字传参
# def method(a,b):
#     print(a)
#     print(b)
#     return b
# print(method(a=1,b=2))


# 5.传入字典
# def method(**a):
#     print(a.keys())
#
# method(a=1,b=2,c=3)

# 6.传入元组
# def method(*a):
#     print(a[0])
#     print(a[1])
#     print(a[2])
#     print(a[3])
#
# method(1,2,3,4)

# 7.仅限关键字参数
# def method(*, a):
#     print(a)
#
# method(a=1)

# 8.字典解包：
# def method(a,b,c):
#     print(a)
#     print(b)
#     print(c)
#     return a,b,c
#
# dict1 = {"a":1,"b":2,"c":3}
# print(method(**dict1))

# 9.lambda表达式
# 1)单个参数
# y = lambda x:x+2
#
# print(y(2))

# 2）多参数
# y = lambda x,y,z : x+y+z
#
# print(y(2,3,4))

# 10.函数可以嵌套函数
# def login(username="tete",password="admin"):
#     if username == 'tete' and password == 'admin':
#         return "yes"
#     else:
#         return "登录账号错误"
#
# def profile(token):
#     if token == "yes":
#         return "欢迎登录"
#     else:
#         return "请重新登录"
#
# print(profile(login()))

# def f3():
#     def f4():
#         return "hello"
#     return f4()
#
# print(f3())

'''需求：在调用f1 或f2 函数的时候，先打印python课程，再打印后面的内容'''

# def getInfo(func):
#     def inner():
#         print("《python课程》")
#         func()
#     return inner
#
# @getInfo
# def f1():
#     print("网易云课堂")
#
#
# def f2():
#     print("好好学习，天天向上")
#
# f1()

# 11.装饰器案例讲解
# def login(func):
#     def inner(token):
#         if token == 'aaaa':
#             return func(token)
#         else:
#             return "请重新登录"
#     return inner
#
# @login
# def profile(token):
#     '''个人主页'''
#     return "已登录"
#
# print(profile("aaaa"))

# 2)案例2
import sys

'''需求：要求注册账号，然后注册的账号登录到系统后，显示出登录的昵称
1.注册的函数
2.登录的函数
3.获取昵称的函数
'''
def in_out():
    username = input("请输入账号：\n")
    password = input("请输入账号名称:\n")
    return username,password

def register():
    '''
    实现账户的注册功能
    :return:
    '''
    username,password = in_out()
    temp = username+"|"+password
    f=open('login.md','w')
    f.write(temp)
    f.close()


def login():
    '''
    登录的函数
    :return:
    '''
    username,password = in_out()
    with open("login.md","r") as f:
        info=f.read()
    info=info.split("|")
    if username == info[0] and password == info[1]:
        return True
    else:
        return False

def getNick(func):
    '''
    获取昵称
    :return:
    '''
    with open('login.md','r') as f:
        info=f.read()
    info = info.split("|")
    if func:
        print("{0}您好，欢迎您登录".format(info[0]))
    else:
        print("请重新登录")

if __name__ == '__main__':
    while True:
        t=int(input('1.注册  2.登录  3.退出系统\n'))
        if t==1:
            register()
        elif t==2:
            getNick(login())
        elif t==3:
            sys.exit(1)
        else:
            print("输入错误，请重新输入")
            continue

