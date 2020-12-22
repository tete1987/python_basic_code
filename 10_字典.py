#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/12 14:59 
# @Author : TETE
# @File : 10_字典.py
#1.字典的定义
# dict1 = {"a":1,"b":2}
# dict2 = dict(a=1,b=2)
# print(type(dict1))
# print(dict1)
# print(type(dict2))
# print(dict2)

# 2.取出字典中的key值和value值
# a = {"a":1,"b":2}
# b = dict(a=1,b=2)
# print(a.keys())
# print(a.values())

# 3.删除字典中的某值
# a = {"a":1,"b":2,"c":4}
# print(a.pop("b"))
# print(a)

# 4.随机删除某个键值
# a = {"a":1,"b":3,"c":5}
# print(a.popitem())
# print(a)

# 5.将列表中的元素当做key值创建新的字典
# a = {}
# b = a.fromkeys([1,4,5,"f"])
# print(b)

# 6.字典推导式
# print({ i for i in range(1,5)})


# def test(a,b):
#     a:dict
#     b:dict
#     a1 = [i for i in a.keys()]
#     a2 = [k for k in a.values()]
#     b1 = [j for j in b.keys()]
#     b2 = [l for l in b.values()]
#     if a1 == b1 and a2 == b2:
#         print("a 和 b 相等")
#         print(a)
#         print(b)
#     else:
#         print("a 和 b 不相等")
#         print(a)
#         print(b)
#
#
# a = {'name': 'tete', 'age': 14,'location':'beijing'}
#
# b = {'name': 'huahua', 'age': 14}
#
# test(a,b)

# favorite_languages = {
#     'jen':['python','ruby'],
#     'sara':["C++"],
#     'edward':['C','java','.net']
# }
# for name,languages in favorite_languages.items():
#     print(f"\n{name.title()}'s favorite languages are:")
#     for language in languages:
#         print(f"\t{language.title()}")

users = {
    'aeinstein':{
        'first':'albert',
        'last':'einstain',
        'location':'princeton'
    },
    'mcurie':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
    }
}

for username,user_info in users.items():
    print(f"\nUsername:{username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"\tFull name:{full_name.title()}")
    print(f"\tLocation：{location.title()}")