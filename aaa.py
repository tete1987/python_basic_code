#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/3/1 8:50 
# @Author : TETE
# @File : aaa.py 
for i in range(1,10):
    for j in range(1,i+1):
        print("%d * %d = %2d "%(j,i,j*i),end= ' ')
    print("")