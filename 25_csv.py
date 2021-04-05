#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/2/23 8:57 
# @Author : TETE
# @File : 25_csv.py
import csv

def read_csv_list():
    with open('url.csv','r',encoding='utf-8') as f:
        #reader 是迭代器
        reader = csv.reader(f)
        next(reader)
        for item in reader:
            print(item)
            # print(item[0])

read_csv_list()


def read_csv_dict():
    with open('url.csv','r',encoding='utf-8') as f:
        #reader 是迭代器
        reader = csv.DictReader(f)

        for item in reader:
            print(dict(item))

read_csv_dict()