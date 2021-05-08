#!/usr/bin/env Python
# coding=utf-8
import scrapy
from dongfangcaifu.items import DongfangcaifuItem
import json

class GupiaoSpider(scrapy.Spider):
    name = 'gupiao'
    allowed_domains = ['data.eastmoney.com']
    start_urls = ['http://data.eastmoney.com/rzrq/']

    def parse(self, response):
        trs=response.xpath('//table[@class="table-model"]/tbody')
        for tr in trs:
            item=DongfangcaifuItem()
            item['id']=tr.xpath('./tr/td[2]/a/text()').extract()
            item['jiancheng']=tr.xpath('./tr/td[3]/a/text()').extract()
            item['shoupanjia']=tr.xpath('./tr/td[4]/span/text()').extract()
            item['zhangdiefu']=tr.xpath('./tr/td[5]/span/text()').extract()
            item['zijin']=tr.xpath('./tr/td[7]/text()').extract()
            item['shizhibi']=tr.xpath('./tr/td[8]/text()').extract()
            yield item

