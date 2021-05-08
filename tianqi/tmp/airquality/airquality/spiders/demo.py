# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
import pymysql

class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['127.0.0.1']
    start_urls = [r'file:///C:\Users\Administrator\Desktop\教学资料\大数据\爬虫\airquality.html']

    def parse(self, response):
        items = response.xpath("//tbody//tr").getall()
        with open(r"C:\Users\11326\Desktop\airquality.txt", "w" ) as f:

            field = Selector(text=items[0]).xpath("//th//text()").getall()
            f.write(",".join(field))
            for item in items:
                data = ""
                values = Selector(text=item).xpath("//td//text()").getall()
                for value in values:
                    data = data + value + ","
                f.write(data[:-1])
        pass










