#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/2/22 15:04 
# @Author : TETE
# @File : 23_配置文件读取.py
import configparser
import os


def base_dir(filename=None):
    return os.path.join(os.path.dirname(__file__), filename)


def get_linux(linux='linux'):
    list1 = []
    config = configparser.ConfigParser(allow_no_value=True)
    config.read(base_dir('config.ini'),encoding='utf-8')
    ip = config.get(linux, 'IP')
    port = config.get(linux, 'PORT')
    username = config.get(linux, 'USERNAME')
    password = config.get(linux, 'PASSWORD')

    list1 = [ip, port, username, password]
    print(list1)

get_linux()
