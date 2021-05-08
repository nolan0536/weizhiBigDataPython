#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis
import pymysql
import json

def process_item():
    #创建redis数据库连接
    rediscli = redis.Redis(host="127.0.0.1",port=6379,db = 0)
    mysqlcli = pymysql.connect(host='localhost',user='root',password='root',db='tianqi',port=3306,charset='utf8')
    #将数据从redis里pop出来
    source,data=rediscli.blpop("new:items")
    #创建MySQL数据库游标对象
    cursor=mysqlcli.cursor()
    sql="insert into youyuan value()"
    cursor.execute(sql)



if __name__=="__main__":
    process_item()
