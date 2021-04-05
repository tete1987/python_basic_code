#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/3/22 9:32 
# @Author : TETE
# @File : 30.匿名函数lambda.py 

# def add(a,b):
#     s = a + b
#     return s
#
# s = lambda a,b:a+b  #s就是函数function
#
# result = s(1,3)
#
# print(result)

# def func(x,y,func):
#     print(x,y)
#     print(func)
#     s = func(x,y)
#     print(s)
#
#
# #调用
# func(1,4,lambda a,b:a+b)

# list1 = [{'a':10,'b':6},{'a':30,'b':8},{'a':1,'b':9}]
#
# m = max(list1,key=lambda x:x['a'])
#
# print(m) #返回的是字典

# list1 = [1,4,5,6,98]
#
# result = map(lambda x:x+2,list1)
#
# print(list(result))
#
# list1 = [4,23,6,8,3,1,2]

# func = lambda x:x if x%2 ==0 else x+1
#
# result = map(func,list1)
#
# print(list(result))
# for index,i in enumerate(list1):
#     if i % 2 !=0:
#         list1[index] = i +1
#
# print(list1)
# from functools import reduce
# tuple1 = (3,)
#
# result = reduce(lambda x,y:x+y,tuple1,3)
#
# print(result)

# list1 = [12,4,6,8]
#
# result = filter(lambda x:x>5,list1)
#
# print(list(result))


student  = [
    {'name':'tom','age':20},
    {'name':'lily','age':23},
    {'name':'lucy','age':18},
    {'name':'jerry','age':30},
]

#找出年龄大于21的学生：
result = filter(lambda x:x['age']>20,student)

student = sorted(student,key=lambda x:x['age'])

print(student)