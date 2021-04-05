#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/3/22 14:21 
# @Author : TETE
# @File : 31.递归函数.py 
def sum(n):
    if n == 0:
        return 0
    else:
        return n+sum(n-1)


#调用
result = sum(10)

print(result)

def f1(n):
    if n>0:
        print('--->',n)
        f1(n-1)
    else:
        print('已结束')

#调用
f1(6)