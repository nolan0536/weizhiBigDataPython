# -*- coding: utf-8 -*-
import scrapy
from airquality.items import AirqualityItem
import pymysql
from scrapy.selector import Selector

class DemoSpider(scrapy.Spider):
    name = 'demo02'
    allowed_domains = ['10.67.42.125']
    start_urls = [r'file:///D:\pachong\爬虫天气\airquality.html']

    def parse(self, response):                                           #port=3306的意思是mysql

        db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='tianqi',charset='utf8')
        cursor = db.cursor() #获取操作游标
        items = response.xpath("//tbody//tr").getall()
        for it in items:
            item = AirqualityItem()
            item_value= Selector(text=it).xpath("//td//text()").getall()
            if len(item_value)==9:
                print(item_value)          #在pipelines中存储
                item["yuefen"]=item_value[0]
                item["AQL"]=item_value[1]
                item["zldj"]=item_value[2]
                item["pm25"]=item_value[3]
                item["pm10"]=item_value[4]
                item["so2"]=item_value[5]
                item["co"]=item_value[6]
                item["no2"]=item_value[7]
                item["o3"]=item_value[8]
                yield item
        # for item in items:   #selecor的意思类似与beautifulsoup
        #     values = Selector(text=item).xpath("//td//text()").getall() #获取全部的值
        #     if len(values)==9:   #insert into 是导入
        #         print(values[2])
        #         sql = "insert into wether value(str_to_date('{0}','%Y-%m-%D'),{1}+0,'{2}',{3}+0,{4}+0,{5}+0,{6}+0,{7}+0,{8}+0)".format(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8][:-2])
        #         #执行sql语句
        #         cursor.execute(sql)            #str_to_date函数是将时间格式的字符串（str），按照所提供的显示格式转化为DATETIME类型
        #         db.commit()

        # cursor.close()
        # db.close()












