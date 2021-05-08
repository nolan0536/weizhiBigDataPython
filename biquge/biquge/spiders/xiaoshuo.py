import scrapy
import re
from biquge.items import BiqugeItem

class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['xbiquge.la']
    start_urls = ['http://www.xbiquge.la/']

    def parse(self, response):
        print(1111111111111111111111111111111111)
        url='http://www.xbiquge.la/13/13959/'
        print(url)
        headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 Safari/537.36'
        }
        yield scrapy.Request(url=url,headers=headers,callback=self.parse_in,dont_filter=True)
    def parse_in(self, response):
        print(22222222222222222222222222222222222)
        item = BiqugeItem()
        item['title']=response.xpath('//div[@id="maininfo"]/div/h1/text()').extract()
        item['zuozhe']=response.xpath('//div[@id="maininfo"]/div/p[1]/text()').extract()
        jobs=response.xpath('//div[@id="list"]/dl/dd')
        for job in jobs:
            item['zhangjieming']=job.xpath('./a/text()').extract()[0]
            url=job.xpath('./a/@href').extract()[0]
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 Safari/537.36'
            }
            yield item
            yield scrapy.Request(url='http://www.xbiquge.la'+url,headers=headers,callback=self.parse_on,dont_filter=True)

    def parse_on(self,response):
        print(response)
        print(33333333333333333333333333333333333333333)
        result=response.text
        item=BiqugeItem()
        item['neirong']=re.findall(r'<div id="content">(.*?)<p>',result,re.S)[0]
        yield item

