import scrapy

from jintougupiao.items import JintougupiaoItem
class GupiaoSpider(scrapy.Spider):
    name = 'gupiao'
    allowed_domains = ['www.guazi.com']
    start_urls = ['https://www.guazi.com/weifang/buy/o2/#bread']

    def parse(self, response):
        print(1111111111111111111)
        print(response.text)
        jobs=response.xpath('//ul[@class="carlist clearfix js-top"]/li')
        for job in jobs:
            item=JintougupiaoItem()
            item['chexing']=job.xpath('./a/@title').extract()
            item['nianfen']=job.xpath('./a/div/text()').extract()
            item['jiage']=job.xpath('./a/div[2]/p/text()').extract()
            item['xinche']=job.xpath('./a/div[2]/em/text()').extract()
            yield item

