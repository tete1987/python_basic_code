#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/13 11:04 
# @Author : TETE
# @File : 11_pyhton模块.py

#1.模块
#1)变量
# name = "tom"
#
# #2）方法：
# def add(a,b):
#     return a+b
#
# #3）类
# class index():
#     def sub(self,a,b):
#         return a-b
#
# print(name)
# #调用方法
# print(add(1,5))
#
# #调用类
# i = index()
# print(i.sub(3,4))

# f = __import__('login')
# f.index()
import login

obj = login.Person()

if hasattr(obj,'person_info'):
    f = getattr(obj,'person_info')
    f()
else:
    print("没找到")

obj = login.Person()
f = setattr(obj,"exit","this is a exit method")
f2 = hasattr(obj,"exit")
print(f2)


f0 = hasattr(login,"str1")
print("未删除之前：",f0)
f1 = delattr(login,"str1")
f2 = hasattr(login,"str1")
print("删除之后：",f2)

