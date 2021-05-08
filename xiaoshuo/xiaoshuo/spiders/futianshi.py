import scrapy
from xiaoshuo.items import XiaoshuoItem

class FutianshiSpider(scrapy.Spider):
    name = 'futianshi'
    allowed_domains = ['xbiquge.la']
    start_urls = ['http://www.xbiquge.la/0/951/']

    def parse(self, response):
        books=response.xpath('//div[@class="box_con"]/div')
        for book in books:
            item=XiaoshuoItem()
            item["zhangming"]=book.xpath('./dl/dd/a/text()').extract()
            url=book.xpath('./dl/dd/a/@href').extract()
            item["fanye"]='http://www.xbiquge.la'+eval(url)
            yield scrapy.FormRequest(url=item["fanye"],meta={'item':item},callback=self.parse_in,
                                     dont_filter=True)
    def parse_in(self,response):
        books=response.xpath('//div[@class="box_con"]')
        for book in books:
            item=XiaoshuoItem()
            item["zhengwen"]=book.xpath('./div[3]/text()').extract()
            yield item







