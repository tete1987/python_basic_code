#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/11 9:49 
# @Author : TETE
# @File : 05 _while循环.py
#示例1：
# a = 1
# while a ==1:
#     print("a=1")
#     a = a+1
# else:
#     print("a != 1")
#     print(a)

# # 2.break语句
# for i in range(1,10):
#     if i == 5:
#         break
#     print(i)

# 3.continue语句
# for i in range(1,10):
#     if i == 5:
#         continue
#     print(i)

'''练习题：
1.猜数字游戏
计算机出一个1-100之间的随机数由人来猜
计算机根据人猜的数字分别给出“大一点、小一点、猜对了”等提示

解题思路：
1.先定义一个变量与计算机的随机数进行比对大小
2.将该变量变成人为可输入模式。
'''
#导入一个随机数函数random
import random

comuter_number = random.randint(1,100)

while True:
    person_number = int(input("请输入一个随机数"))
    if person_number > comuter_number:
        print("小一点")
    elif person_number < comuter_number:
        print("大一点")
    else:
        print("猜对啦")
        break