#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/19 9:00 
# @Author : TETE
# @File : 20_python外部数据源文件处理.py
import yaml
#1.Excel表格处理
# from openpyxl import Workbook
# from openpyxl import load_workbook
# from openpyxl import Workbook
# from openpyxl.utils import get_column_letter
#
# wb = Workbook()
#
# dest_filename = 'empty_book.xlsx'
#
# ws1 = wb.active
# #表的sheet页签名称
# ws1.title = "range names"
#
# for row in range(1, 40):
#     ws1.append(range(600))
# #创建第二个页签，名称是pi
# ws2 = wb.create_sheet(title="Pi")
#
# ws2['F5'] = 3.14
#
# ws3 = wb.create_sheet(title="Data")
# for row in range(10, 20):
#     for col in range(27, 54):
#        _ = ws3.cell(column=col, row=row, value="{0}".format(get_column_letter(col)))
# print(ws3['AA10'].value)
#
# wb.save(filename = dest_filename)
#
#
# wb = load_workbook(filename = 'empty_book.xlsx')
# sheet_ranges = wb['range names']
# print(sheet_ranges['D18'].value)
# for i in range(1,3):
#     print(sheet_ranges.cell(column=1,row=i).value)

#2.yaml，将pyhton格式转换为yaml
# #1)直接打印时会有红字提醒，如果想去掉红字，可以加一个Loader，返回列表格式
# print(yaml.load("""
# - Hesperiidea
# - Papilionidea
# """,Loader=yaml.FullLoader))

#2）如果想返回字典，则使用以下方式：
# print(yaml.load("""
# a: 1
# """,Loader=yaml.FullLoader))

#3)打印文件中的内容，首先新建一个demo.yaml文件
# print(yaml.load(open("demo.yaml"),Loader=yaml.FullLoader))

#4)yaml.dump方法
# print(yaml.dump({'a':[1,2]}))

#使用yaml.dump 写入一个文件
with open("demo1.yml","w") as f:
    yaml.dump(data={'a':[1,2],'b':3},stream=f)