#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/12 14:19 
# @Author : TETE
# @File : 08_元组.py

#1.元组定义
# tuple1 = (1,2,3)
# tuple2 = 1,2,3
#
# print("tuple1元组：",tuple1)
# print("tupple元组的类型是：",type(tuple1))
#
# print("tuple2元组：",tuple2)
# print("tuple2元组的类型是：",type(tuple2))

#2.元组嵌套列表：
# a = [1,3,5]
# tuple_a = (2,5,a)
# print(id(tuple_a[2]))
# #修改元组中的列表的值：
# tuple_a[2][2]=6
# print(tuple_a)
# #可以查看到虽然值变了，但在元组中的id值并没有改变
# print(id(tuple_a[2]))

#3.元组中的元素个数计数
# a = (1,4,6,"a",35,"a")
# print(a.count("a"))

#4.返回元素的索引位置：
a = (1,5,3,6)
print(a.index(3))

