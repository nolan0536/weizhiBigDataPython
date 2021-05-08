# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import pymysql

class DemoSpider(scrapy.Spider):
    name = 'demo02'
    allowed_domains = ['127.0.0.1']
    start_urls = [r'file:///F:\work\大数据资源开发\书稿\项目一\airquality.html']

    def parse(self, response):
        db = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='test',charset='utf8')
        cursor = db.cursor()
        items = response.xpath("//tbody//tr").getall()
        for item in items:
            values = Selector(text=item).xpath("//td//text()").getall()
            if len(values)==9:
                sql = "insert into test value(str_to_date('{0}','%Y-%m-%D'),{1}+0,'{2}',{3}+0,{4}+0,{5}+0,{6}+0,{7}+0,{8}+0)".format(values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7],values[8][:-2])
                cursor.execute(sql)
                db.commit()

        cursor.close()
        db.close()
        pass










