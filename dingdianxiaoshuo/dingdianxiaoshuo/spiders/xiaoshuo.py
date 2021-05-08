import scrapy
from dingdianxiaoshuo.items import DingdianxiaoshuoItem
import re
class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['23us.com']
    start_urls = ['https://www.23us.com/']

    def parse(self, response):
        print(1111111111111111111111111111)
        jobs=response.xpath('//bdo[@id="s_dd"]/dd')
        for job in jobs:
            item=DingdianxiaoshuoItem()
            item['title']=job.xpath('./a[2]/text()').extract()

            url=job.xpath('./a[2]/@href').extract()[0]
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 Safari/537.36'
            }
            print(url)
            yield scrapy.Request(url=url,headers=headers,callback=self.parse_in,dont_filter=True,meta={'url':url})

    def parse_in(self,response):
        print(222222222222222222222222)
        resulr=response.meta['url']
        print(resulr)
        item=DingdianxiaoshuoItem()
        jobs=response.xpath('//*[@id="at"]/tr/td')
        for job in jobs:
            item['zhangjieming']=job.xpath('./a/text()').extract()
            url=job.xpath('./a/@href').extract()[0]
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 Safari/537.36'
            }
            yield item
            yield scrapy.Request(url=resulr+url,headers=headers,callback=self.parse_on,
                                 dont_filter=True)
    def parse_on(self,response):
        print(33333333333333333333333333)
        item=DingdianxiaoshuoItem()
        item['neirong']=response.xpath('//*[@id="contents"]/text()').extract()
        yield item

