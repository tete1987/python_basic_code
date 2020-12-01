#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/10 16:16 
# @Author : TETE
# @File : 03_if语句.py

#1.if 语句练习
#1）简单if练习
# a = 1
# if a == 0:
#     print("a=0")
# else:
#     print("a不等于0")

#2）多重分支
# a = 2
# if a == 0:
#     print("a=0")
# elif a == 1:
#     print("a=1")
# elif a == 2:
#     print("a=2")
# else:
#     print("a不等于0,1,2")

'''练习：
分别使用分支嵌套以及多重分支去实现分段函数求值。
分段函数求值：
3*x-5（x>1）
f(x)=x+2(-1<=x<=1)
5*x+3(x<-1)

解题思路：
x>1 时执行 3*x-5
-1<=x<=1  时执行 x+2
x<-1时执行 5*x+3'''
#多重分支：
# x=-8
# if x > 1:
#     y = 3*x-5
# elif -1 <= x <= 1:
#     y = x +2
# else:
#     y = 5*x +3
# print(y)

#分支嵌套：
x=0
if x > 1:
    y = 3*x -5
else:
    if x < -1:
        y = 5*x +3
    else:
        y = x +2
print(y)
