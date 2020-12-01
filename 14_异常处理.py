#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2020/11/16 10:30 
# @Author : TETE
# @File : 14_异常处理.py

#自定义异常
class MyException(Exception):
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
try:
    num1 = input("请输入一个除数")
    num2 = int(input("请输入一个被除数"))
#如果输入的第一个值不是整型数据，则捕获异常
    if not num1.isdigit():
        raise MyException("num1","num2")
    print(num1 / num2)

except MyException:
    print("输入有误")
except:
    print("这是一个异常")
#若知道异常的名称字时捕获异常：
# except ZeroDivisionError:
#     print("被除数不可为0")

#当不知道异常的名称时，直接捕获所有异常
# except:
#     print("这是一个异常")

# #正常执行时执行的代码
else:
    print("执行成功")
#
# #不论是否有异常都可以执行的代码：
# finally:
#     print("无论是否有异常均执行")

