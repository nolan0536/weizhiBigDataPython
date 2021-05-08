import scrapy
from zhaopin.items import ZhaopinItem

class ZhaopinscripySpider(scrapy.Spider):
    name = 'zhaopinscripy'
    allowed_domains = ['zp.cc']
    start_urls = ['http://www.zp.cc/']

    def parse(self, response):
        books=response.xpath('//div[@class="hj-jobs"]')
        for book in books:
            item=ZhaopinItem()
            item['zhiwei']=book.xpath('./div/div[2]/div[1]/a/text()').extract()
            item['yuexin']=book.xpath('./div/div[2]/div[2]/text()').extract()
            item['gongsi']=book.xpath('./div/div[4]/a/text()').extract()
            yield item


