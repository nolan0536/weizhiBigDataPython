import scrapy
from lianfang.items import LianfangItem

class ErshoufangSpider(scrapy.Spider):
    name = 'ershoufang'
    allowed_domains = ['bj.lianjia.com']
    start_urls = ['https://bj.lianjia.com/ershoufang/co32/']

    def parse(self, response):
        jobs=response.xpath('//ul[@class="sellListContent"]/li')
        for job in jobs:
            item=LianfangItem()
            item["title"]=job.xpath('./div/div/a/text()').extract()[0]
            item["xinxi"]=job.xpath('./div/div[3]/div/text()').extract()[0]
            item["jiage"]=job.xpath('./div/div[6]/div/span/text()').extract()[0]
            item["danjia"]=job.xpath('./div/div[6]/div[2]/span/text()').extract()[0]
            item["dizhi"]=job.xpath('./div/div[2]/div/a[2]/text()').extract()[0]
            yield item
            pages=100
            for page in range(2,pages):
                url="https://bj.lianjia.com/ershoufang/pg{}co32/".format(page)
                yield scrapy.Request(url=url,callback=self.parse)
