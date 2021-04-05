#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/3/18 9:43 
# @Author : TETE
# @File : 29.装饰器.py 
# def decorate(func):
#     a =100
#     print("wrapper外层打印测试")
#
#     def wrapper():
#         func()
#         print("-----刷漆")
#         print("-----铺地板",a)
#         print("-----装门")
#
#     print("wrapper加载完成")
#     return wrapper
#
#
# @decorate
# def house():
#     print("我是毛坯房")

# def decorate(func):
#     def wrapper(*args,**kwargs):
#         print("正在校验----")
#         func(*args,**kwargs)
#         print("校验完毕----")
#
#     return wrapper
#
# @decorate
# def f1(n):
#     print('---f1---',n)
#
# @decorate
# def f2(name):
#     print('----f2---',name)
#
# @decorate
# def f3(students,clazz='1098'):
#     print("班级名称：%s"%clazz)
#     for stu in students:
#         print(stu)
#
# f1(1)
#
# f2('huahua')
#
# students = ['lily','a',1]
# f3(students,clazz='1092班级')

# def decorate1(func):
#     print('------1 start----')
#     def wrapper(*args,**kwargs):
#         func()
#         print('刷漆')
#
#     print('------1 end------')
#     return wrapper
#
#
# def decorate2(func):
#     print('------2 start----')
#
#     def wrapper(*args, **kwargs):
#         func()
#         print('铺地板，装门')
#
#     print('------2 end------')
#     return wrapper
#
#
# @decorate2
# @decorate1
# def house():
#     print('我是毛坯房')
#
# #调用
# house()



def outer(a):  #第一层：负责接收参数的
    def decorate(func):    #第二层：负责接收函数的
        def wrapper(*args,**kwargs):  #第三层：负责接收函数的参数
            func(*args)
            print("--->铺地砖%s块"%a)

        return wrapper    #返回的是第三层

    return decorate  #返回的是第二层

@outer(10)
def house(time):
    print('我入住的时间是：%s'%time)

@outer(1990)
def steert():
    print("这条街是望京街道")


house('2021-10-1')

steert()
