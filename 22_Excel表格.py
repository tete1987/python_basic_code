#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/2/22 14:22 
# @Author : TETE
# @File : 22_Excel表格.py
import xlrd
import os

from xlutils.copy import copy


def base_dir(filename=None):
    return os.path.join(os.path.dirname(__file__),filename)

work = xlrd.open_workbook(base_dir('云建积分管理-2021年2月.xls'))
#
# sheet = work.sheet_by_index(0)
# #查看多少行
# print(sheet.nrows)
#
# #获取单元给的内容
# print(sheet.cell_value(28,1))
old_content =copy(work)
ws = old_content.get_sheet(0)
ws.write(0,3,'2021.03')
old_content.save(base_dir('云建积分管理-2021年3月.xls'))

