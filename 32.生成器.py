#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/3/22 15:53 
# @Author : TETE
# @File : 32.生成器.py 

# g = (x*3 for x in range(20))

# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# while True:
#     try:
#         e = next(g)
#         print(e)
#     except:
#         print('没有更多元素了')
#         break

# def func():
#     n = 0
#     while True:
#         n += 1
#         yield n  #得到这个元素且不再往下产生，类似return，但多了一个特点：暂停
#
# g = func()
#
#
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

#斐波那契数列
# def fib(length):
#     a,b = 0,1
#     n = 0
#     while n<length:
#         yield b
#         a,b = b,a+b
#         n += 1
#
#     return  '没有更多元素了'  #return就是在得到StopIteration后面的提示信息
#
# #调用
# g = fib(8)
#
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# def gen():
#     i = 0
#     while i < 5:
#         temp = yield i
#         print('temp:',temp)
#         i += 1
#     return '没有更多数据了'
#
# g = gen()
# print(g.send(None))
#
# n1 =g.send('呵呵')
# print('n1:%s'%n1)
#
# n2 =g.send('哈哈')
# print('n2:%s'%n2)

# def gen():
#     i = 0
#     while i < 5:
#         temp = yield i
#         print('temp:',temp)
#         for j in range(temp):
#             print('----->',j)
#         print('**********')
#         i += 1
#     return '没有更多数据了'
#
# g = gen()
# print(g.send(None))
#
# n1 =g.send(5)
# print('n1:%s'%n1)
#
# n2 =g.send(3)
# print('n2:%s'%n2)

# def task1(n):
#     for i in range(n):
#         print('正在搬第%s块砖'%i)
#         yield None
#
# def task2(n):
#     for i in range(n):
#         print('正在搬第%s首歌'%i)
#         yield None
#
# g1 = task1(5)
#
# g2 = task2(5)
#
# while True:
#     try:
#         g1.__next__()
#         g2.__next__()
#     except:
#         break


from collections.abc import Iterable
list1 = [5,3,7,9,4]
iter(list1)


f = isinstance(list1,Iterable)
print(f)

f = isinstance('s6788',Iterable)
print(f)