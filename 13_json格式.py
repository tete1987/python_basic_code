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

# info = ("1",2,"aaaa")
#dumps：将pyhton中的字典，转换为字符串，序列化
dict_str = json.dumps(info,sort_keys=True,indent=4)

print(dict_str)
print(type(dict_str))

#loads反序列化
str_dict=json.loads(dict_str)
print(str_dict)
print(type(str_dict))

#3.文件的序列化与反序列化
from pip._vendor import requests

r =requests.get(url='https://adserver-us.adtech.advertising.com/pubapi/3.0/9538.1/4719824/0/-1/ADTECH;v=2;cmd=bid;cors=yes;misc=1610417437039')
json.dump(r.content.decode('utf-8'),open("weather.json","w"))
'''
1.文件反序列化后，类型是Unicode
2.把Unicode类型转为str类型
3.然后使用反序列化，把str转为字典类型
'''
dict1 = json.loads((json.load(open("weather.json","r")).encode('utf-8')))
print(dict1["id"])