#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/1/8 14:18 
# @Author : TETE
# @File : 21.login_demo.py
import sys

'''需求：要求注册账号，然后注册的账号登录到系统后，显示出登录的昵称
1.注册的函数
2.登录的函数
3.获取昵称的函数
'''
def type_username():
    username = input("请输入账号：\n")
    return username

def type_password():
    password = input("请输入账号名称:\n")
    return password

def register(username,password):
    '''
    实现账户的注册功能
    :return:
    '''
    temp = username+"|"+password
    f=open('login.md','w')
    f.write(temp)
    f.close()


def login(username,password):
    '''
    登录的函数
    :return:
    '''
    f = open("login.md","r")
    for line in f:
        list_user = line.split("|")
        if list_user[0] == username and list_user[1] == password:
            return True
        else:
            return False

def info(username,password):
    '''
    获取昵称
    :return:
    '''
    f = open("login.md", "r")
    for line in f:
        list_user = line.split("|")
    r = login(username,password)
    if r:
        print("{0}您好，欢迎您登录".format(info[0]))
    else:
        print("请重新登录")

def main():
    '''主函数'''
    while True:
        t=int(input('1.注册  2.登录  3.退出系统\n'))
        if t==1:
            username = type_username()
            password = type_password()
            register(username,password)
        elif t==2:
            username = type_username()
            password = type_password()
            login(username, password)
            info(username, password)
        elif t==3:
            print("恭喜您成功退出系统")
            sys.exit()
        else:
            print("输入错误，请重新输入")
            continue

if __name__ == '__main__':
    main()

