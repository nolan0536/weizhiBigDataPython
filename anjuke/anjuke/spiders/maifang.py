import scrapy
from anjuke.items import AnjukeItem

class MaifangSpider(scrapy.Spider):
    name = 'maifang'
    allowed_domains = ['weifang.anjuke.com']
    start_urls = ['https://weifang.anjuke.com/sale/']

    def parse(self, response):
        jobs=response.xpath('//*[@id="houselist-mod-new"]/li')
        for job in jobs:
            item=AnjukeItem()
            item["title"]=job.xpath('./div[2]/div/a/text()').extract()[0]
            item["jushi"]=job.xpath('./div[2]/div[2]/span[1]/text()').extract()[0]
            item["xiaoqu"]=job.xpath('./div[2]/div[3]/span/@title').extract()[0]
            item["mianji"]=job.xpath('./div[2]/div[2]/span[2]/text()').extract()[0]
            item["jiage"]=job.xpath('./div[3]/span[1]/strong/text()').extract()[0]
            item["danjia"]=job.xpath('./div[3]/span[2]/text()').extract()[0]
            yield item
            pages=20
            for page in range(2,pages):
                url='https://weifang.anjuke.com/sale/p{}/#filtersort'.format(str(page))
                yield scrapy.Request(url=url,callback=self.parse)



