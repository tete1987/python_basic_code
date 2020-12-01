#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/13 11:04 
# @Author : TETE
# @File : 11_pyhton模块.py
#1.模块
#1)变量
name = "tom"

#2）方法：
def add(a,b):
    return a+b

#3）类
class index():
    def sub(self,a,b):
        return a-b

print(name)
#调用方法
print(add(1,5))

#调用类
i = index()
print(i.sub(3,4))