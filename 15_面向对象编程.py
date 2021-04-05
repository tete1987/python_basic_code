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

# class Person:
#     def __init__(self,name,age,gender):
#         #实例属性
#         self.name = name
#         self.gender = gender
#         self.age = age
#
#     def eat(self):
#         print(f"name : {self.name},age : {self.age},gender : {self.gender} 我在吃")
#
#     def drink(self):
#         print(f"name : {self.name},age : {self.age},gender : {self.gender} 我在喝")
#
#     def run(self):
#         print(f"name : {self.name},age : {self.age},gender : {self.gender} 我在跑")
#
#     def set_att(self,value):
#         self.value = value
#
#
# #实例化的过程
# xiaoming = Person("xiaoming",10,"male")
# xiaohong = Person("xiaohong",28,"female")
#
# print(xiaoming.name)
# #调用方法
# xiaoming.drink()
# xiaoming.eat()
#
# xiaoming.set_att("hallo")
# print(xiaoming.value)
#
# xiaohong.drink()
# xiaohong.run()

'''
动态参数案例
'''


# class Person:
#     def __init__(self,*args):
#         self.args = args
#
#     def info(self):
#        print("人员的姓名：",self.args)
#
# per1 = Person(1,4,56,45)
# per1.info()

# class Person:
#     def __init__(self):
#         print("我是构造函数")
#
#     def __del__(self):
#         print("我是析构函数")
#
#     def info(self):
#         print("我是方法")
#
# per1 = Person()
# per1.info()

# class Person(object):
#     def info(self):
#         print('普通方法')
#
#     @property
#     def show(self):
#         print('特性方法')
#
#     @staticmethod
#     def f1():
#         print('静态方法')
#
#     @classmethod
#     def add(cls):
#         print('类方法')
#
#
# if __name__ == '__main__':
#     obj = Person()
#     obj.info()
#     obj.show
#     obj.f1()
#     obj.add()

# class Person(object):
#     def eat(self):
#         print("人吃饭")
#
# class Mother(Person):
#     def eat(self):
#         print("妈妈喜欢吃水果")
#
#     def run(self):
#         print("妈妈跑得快")
#
# class Father(Person):
#     def eat(self):
#         print("爸爸喜欢吃肉")
#
# class Son(Father,Mother):
#
#     pass
#
# son = Son()
# son.eat()
# son.run()

# class A():
#     def show(self):
#         print("我是父类A")
#
#
# class B(A):
#     pass
#
#
# class C(A):
#     def show(self):
#         print("我是子类C")
#
#
# class D(B, C):
#     pass
#
#
# d = D()
# d.show()



# class Factory:
#     def createFruit(self,fruit):
#         if fruit == "apple":
#             return Apple()
#         elif fruit == "banana":
#             return Banana()

class Fruit:
    b = 100

    def aaa(self):
        # print(self)
        print(self.b)
        # return 'fruit'


class Apple(Fruit):
    b = 300
    print(b)



a = Apple()
a.aaa()
# class Banana(Fruit):
#     def __str__(self):
#         return 'banana'
#
# if __name__ == '__main__':
#     factory = Factory()
#     print(factory.createFruit('apple'))
#     print(factory.createFruit('banana'))
#
