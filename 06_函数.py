#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/11 15:25 
# @Author : TETE
# @File : 06_函数.py

#1.函数形式：
# def method(a):
#     '''
#
#     :param a:
#     :return:
#     '''
#     print(a)
#
# method(2)

#2.增加return
# def method(a):
#     print(a)
#     return a+3
#
# print(method(2))

#3.函数默认值
# def method(a,b=[]):
#     b.append(a)
#     return b
#
# print(method(1))
# print(method(2))

#4.关键字传参
# def method(a,b):
#     print(a)
#     print(b)
#     return b
# print(method(a=1,b=2))


#5.传入字典
# def method(**a):
#     print(a.keys())
#
# method(a=1,b=2,c=3)

#6.传入元组
# def method(*a):
#     print(a[0])
#     print(a[1])
#     print(a[2])
#     print(a[3])
#
# method(1,2,3,4)

#7.仅限关键字参数
# def method(*, a):
#     print(a)
#
# method(a=1)

#8.字典解包：
# def method(a,b,c):
#     print(a)
#     print(b)
#     print(c)
#     return a,b,c
#
# dict1 = {"a":1,"b":2,"c":3}
# print(method(**dict1))

#9.lambda表达式
#1)单个参数
# y = lambda x:x+2
#
# print(y(2))

#2）多参数
y = lambda x,y,z : x+y+z

print(y(2,3,4))