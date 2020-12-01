#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/12 14:37 
# @Author : TETE
# @File : 09_集合.py
#1.集合的定义
# a = {1}
# b = set()
# print(type(a))
# print(type(b))
# #查看集合是否为空
# print(len(a))
# print(len(b))

#2.两个集合取并集
# a ={1,4,5,6}
# b = {7,4}
# print(a.union(b))
# #取交集：
# print(a.intersection(b))
# #取a中有，b中没有的值
# print(a.difference(b))

#3.对集合进行操作
#1）添加值
# a = {1,3,45}
# b = {3,6,78,8}
# a.add("f")
# print(a)

#2)求出去重之后的集合
print({i for i in "safdafafaekklldlldld"})
#或第二种写法：
c = "safdafafaekklldlldld"
print(set(c))