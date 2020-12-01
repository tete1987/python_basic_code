#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/12 14:59 
# @Author : TETE
# @File : 10_字典.py
#1.字典的定义
# dict1 = {"a":1,"b":2}
# dict2 = dict(a=1,b=2)
# print(type(dict1))
# print(dict1)
# print(type(dict2))
# print(dict2)

#2.取出字典中的key值和value值
# a = {"a":1,"b":2}
# b = dict(a=1,b=2)
# print(a.keys())
# print(a.values())

#3.删除字典中的某值
# a = {"a":1,"b":2,"c":4}
# print(a.pop("b"))
# print(a)

#4.随机删除某个键值
# a = {"a":1,"b":3,"c":5}
# print(a.popitem())
# print(a)

#5.将列表中的元素当做key值创建新的字典
# a = {}
# b = a.fromkeys([1,4,5,"f"])
# print(b)

#6.字典推导式
print({ i for i in range(1,5)})