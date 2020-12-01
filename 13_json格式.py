#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/16 9:43 
# @Author : TETE
# @File : 13_json格式.py
import json
info = [{
    "name":"Tom",
    "gender":"male",
    "other":None
},{
    "name":"Jack",
    "gender":"male",
    "other":None
}]

#dumps：将pyhton中的字典，转换为字符串
data = json.dumps(info,sort_keys=True,indent=4)
print(data)
print(type(data))

