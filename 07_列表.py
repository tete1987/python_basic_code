#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/12 14:21 
# @Author : TETE
# @File : 07_列表.py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/11 16:49
# @Author : TETE
# @File : 07_常用数据结构.py

#1.列表：
#1)append
# list1=[1,3,6,23]
# list1.append(5)
# print(list1)

#2)sort用法
# list1 = [1,5,3,8]
# list1.sort()
# print(list1)
# list1.sort(reverse=True)
# print(list1)

#3)pop用法
# list1 = [1,4,5,23,2]
# y = list1.pop()
# print(y)
# print(list1)
# f = list1.pop(2)
# print(f)
# print(list1)

#4)remove 用法
# list1 = [2,3,3,7]
# list1.remove(2)
# print(list1)

#5)insert 用法
# list1 = [3,6,4.2,8]
# list1.insert(0,3)
# print(list1)

#6)index 用法
# list1 = [4,7,3,2]
# print(list1.index(7))

#7）count用法
# list1 = [1,4,6,6,3,3,6,2]
# print(list1.count(6))

'''练习：
如果我们想生成一个平方列表，比如[1,4,9]，使用for循环应该怎么写，使用列表生成式又应该怎么写呢？'''
#8）正常写法
# list1 = []
# for i in range(1,4):
#     list1.append(i**2)
# print(list1)

#9）列表推导式写法
# list_square = [i**2 for i in range(1,4)]
# print(list_square)

#如果for语句后面还有嵌套if语句，使用列表推导式可如下：
# list_square = [i**2 for i in range(4) if i != 1 ]
#
# print(list_square)
#此种模式写法等于：
#list_square = []
# for i in range(4):
#     if i != 1:
#         list_square = [i**2]

#循环嵌套：
# list_square = []
# for i in range(1,4):
#     for j in range(1,4):
#         list_square.append(i*j)
#
# print(list_square)
#注：循环嵌套首先要将里面的嵌套跑完，之后才开始循环外面的循环，第二次循环外面的循环时，里面的嵌套又重新执行一遍。

#循环嵌套的推导式写法：
# list_square = [i*j for i in range(1,4) for j in range(1,4)]
# print(list_square)

# 10）切片
# my_foods =['pizza','falafei','carrot cake']
# friend_food = my_foods[:]
#
# my_foods.append('icecream')
# friend_food.append('apple')
#
# print(my_foods)
# print(friend_food)

current_users = ['tete','xiaole','xiaoniu','hexu','shaokai']
current_users_lower = [i.lower() for i in current_users]


new_users = ['tete','huahua','Xiaoniu','HUAWEI','SHAOKAI']
new_users_lower = [w.lower() for w in new_users]

for new_user in new_users_lower:
    if new_user in current_users_lower:
        print(f" {new_user} 该名称已被注册")
    else:
        print(f" {new_user} 该账户可使用")