#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/16 11:52 
# @Author : TETE
# @File : 15_面向对象编程.py
# class Person():
#     #类的属性
#     name = "noname"
#     #方法：
#     def get_name(self):
#         return self.name
#
# print(Person.name)
#
# #实例化的过程：
# p = Person()
# print(p.name)
# #调用方法
# print(p.get_name())
#
# #重新赋值：
# p.name = "lili"
# print(p.get_name())
#
# #重新定义Person类的属性值：
# Person.name = "huahua"
# f = Person()
# print(f.get_name())

class Person:
    def __init__(self,name,age,gender):
        #实例属性
        self.name = name
        self.gender = gender
        self.age = age

    def eat(self):
        print(f"name : {self.name},age : {self.age},gender : {self.gender} 我在吃")

    def drink(self):
        print(f"name : {self.name},age : {self.age},gender : {self.gender} 我在喝")

    def run(self):
        print(f"name : {self.name},age : {self.age},gender : {self.gender} 我在跑")

    def set_att(self,value):
        self.value = value


#实例化的过程
xiaoming = Person("xiaoming",10,"male")
xiaohong = Person("xiaohong",28,"female")

print(xiaoming.name)
#调用方法
xiaoming.drink()
xiaoming.eat()

xiaoming.set_att("hallo")
print(xiaoming.value)

xiaohong.drink()
xiaohong.run()

