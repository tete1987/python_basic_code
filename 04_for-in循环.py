#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/11 9:23 
# @Author : TETE
# @File : 04_for-in循环.py
'''练习题：
1.计算1-100求和
2.加入分支结构实现1-100之间的偶数求和
3.使用python实现1-100之间的偶数求和'''

#1.计算1-100求和：
# result = 0
# for i in range(1,101):
#     print(i)
#     result = result + i
# print(result)


#2.加入分支结构实现1-100之间的偶数求和
# result = 0
# for i in range(1,101):
#     if i % 2 == 0:
#         print(i)
#         result = result + i
#
# print(result)

#3.使用python实现1-100之间的偶数求和
result = 0
for i in range(1,100,2):
    print(i)
    result = result +i
print(result)