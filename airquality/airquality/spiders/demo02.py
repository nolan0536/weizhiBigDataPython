# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import pymysql
from airquality.items import AirqualityItem
class DemoSpider(scrapy.Spider):
    name = 'demo02'
    allowed_domains = ['192.168.43.191']
    start_urls = [r'file:///C:\Users\张铭轩\Desktop\爬虫\爬虫天气\airquality.html']


    def parse(self, response):
        # db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='tianqi',charset='utf8')
        # cursor = db.cursor()
        items = response.xpath("//tbody//tr").getall()
        for it in items:
            item = AirqualityItem()
            item_value= Selector(text=it).xpath("//td//text()").getall()
            # if len(values)==9:
            #     print(values[2])
            #     sql = "insert into wether value(str_to_date('{0}','%Y-%m-%D')," \
            #           "{1}+0,'{2}',{3}+0,{4}+0,{5}+0,{6}+0,{7}+0,{8}+0)".format(
            #         values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8][:-2])
            #
            if len(item_value) == 9:
                print(item_value)
                item["day"]=item_value[0]
                item["AQI"] = item_value[1]
                item["lever"] = item_value[2]
                item["PM2"] = item_value[3]
                item["PM10"] = item_value[4]
                item["SO2"] = item_value[5]
                item["CO"] = item_value[6]
                item["NO2"] = item_value[7]
                item["O3"] = item_value[8]
                yield item










