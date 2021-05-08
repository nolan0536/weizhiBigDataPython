import scrapy
from tianqi.items import TianqiItem

class TianqispiderSpider(scrapy.Spider):
    name = 'tianqispider'
    allowed_domains = ['weatther.com']
    start_urls = ['http://www.weather.com.cn/weather/101120601.shtml']

    def parse(self, response):
        print(111111111111111111111111111)
        tianqis=response.xpath('//*[@id="7d"]/ul')
        for tianqi in tianqis:
            item=TianqiItem()
            item['day']=tianqi.xpath('./li/h1/text()').extract()
            item['tianqi']=tianqi.xpath('./li/p/@title').extract()
            item['max']=tianqi.xpath('./li/p[2]/span/text()').extract()
            item['min']=tianqi.xpath('./li/p[2]/i/text()').extract()
            item['fengli']=tianqi.xpath('./li/p[3]/i/text()').extract()
            yield item

