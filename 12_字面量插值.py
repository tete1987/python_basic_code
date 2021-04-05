#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/13 14:20 
# @Author : TETE
# @File : 12_字面量插值.py
#1.字面量%的使用
# str = "my name is %s,age is %d"%("tete",20)
# print(str)
#
# print("pi= %.2f"%3.1415926)

#2.字面量插值format使用
# name = 'tom'
# name2 = 'jerry'
# print('two boy are {} and {}'.format(name,name2))
# print('two boy are {0} and {1},{0} is tomm,{1} is jerry'.format(name,name2))

#字典：
# dic1 = {"name":"tom","age":18}
# print("my name is {name},age is {age}".format(**dic1))

#列表
list1 = ['tom',20]
print("my name is {0},age is {1}".format(*list1))