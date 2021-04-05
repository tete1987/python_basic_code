#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/3/17 16:08 
# @Author : TETE
# @File : 28_闭包.py 
# def func(a,b):
#     c =10
#
#     def inner_func():
#         s = a+b+c
#
#         print("相加之和：%s"%s)
#
#
#     return inner_func
#
# ifunc = func(4,5)  #ifunc就是inner_func  ifunc = inner_func
#
# ifunc()
#
def func():
    a = 100

    def inner_func1():
        b = 90
        s = a+b
        print(s)

    def inner_func2():
        inner_func1()
        print("-----inner_func2")

    return inner_func2

x = func()

x()
