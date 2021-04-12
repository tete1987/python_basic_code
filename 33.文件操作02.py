#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 9:20
# @Author  : TeTe
# @File    : 33.文件操作02.py

import os

# os.path.dirname(__file__)： #获取当前文件夹的绝对路径
src_path = r'D:\桌面文件\风景图片'
target_path = r'E:\上传的资料'

def copy(src_path,target_path):
    #获取文件夹里面的内容
    filelist = os.listdir(src_path)

    #遍历列表
    for file in filelist:
        #拼接路径
        path = os.path.join(src_path,file)

        #判断是文件夹还是文件
        if os.path.isdir(path):
            #如果是文件夹，则在原来的文件夹中拼接一个新的文件夹（名称）
            target_path1 = os.path.join(target_path,file)
            #创建文件夹
            os.mkdir(target_path1)
            # 递归调用copy
            copy(path,target_path1)

        else:
            #不是文件夹则直接进行复制
            with open(path,'rb') as rstream:
                container = rstream.read()

                path1 = os.path.join(target_path,file)
                with open(path1,'wb') as wstream:
                    wstream.write(container)
    else:
        print('复制完成！')

copy(src_path,target_path)
'''
os.path :常用函数
    os.path.dirname()：获取指定文件的目录
    os.path.join()：拼接获取新的路径
    os.path.split()：分割（文件目录，文件名）
    os.path.splitext()：分割（文件目录\文件名，文件的扩展名）
    os.path.getsize()：获取文件大小
    os.path.isabs()：判断是否为绝对路径
    os.path.isfile()：判断是否是文件
    os.path.isdir()：判断是否是文件夹
    
os模块下的方法：
    os.getcwd():获取当前目录
    os.listdir()：浏览文件夹
    os.mkdir()：创建文件夹
    os.rmdir()：删除空的文件夹
    os.remove()：删除文件
    os.chdir()：切换目录
'''
