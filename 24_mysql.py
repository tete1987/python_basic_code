#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2021/2/22 15:59 
# @Author : TETE
# @File : 24_mysql.py 
import  pymysql

class MySql:
    def conn(self):
        try:
            con = pymysql.connect(
                host='127.0.0.1',
                user='root',
                passwd='123456',
                db='django_test'
            )

        except Exception as e:
            return e.args

        return con

    def get_one(self,sql,params):
        cur = self.conn().cursor()
        data = cur.execute(sql,params)
        result = cur.fetchone()

        return result


def chek_valid(username,password):
    opera = MySql()
    sql = 'select * from login where username = %s and password=%s'
    params = (username,password)
    return opera.get_one(sql=sql,params=params)

def info():
    uesername = input('请输入用户名：\n')
    password = input('请输入密码：\n')
    result = chek_valid(uesername,password)
    if result:
        print('登录成功')
    else:
        print('登录失败')

if __name__ == '__main__':
    info()


