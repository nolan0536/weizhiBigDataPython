import scrapy
from youxi.items import YouxiItem

class YouxispiderSpider(scrapy.Spider):
    name = 'youxispider'
    allowed_domains = ['4399.com']
    start_urls = ['http://www.4399.com/']

    def parse(self, response):
        print(11111111111111111)
        jobs=response.xpath('//ul[@class="tm_list"]/li')
        for job in jobs:
            url=job.xpath('./a/@href').extract()[0]
            print(url)
            headers={
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 Safari/537.36'
            }
            yield scrapy.Request(url='http://www.4399.com'+url,headers=headers,callback=self.parse_in,dont_filter=True)
    def parse_in(self,response):
        print(22222222222222222)
        item=YouxiItem()
        jobs=response.xpath('//div[@class="intr cf"]')
        for job in jobs:
            item["title"]=job.xpath('./div[2]/div[1]/h1/a/text()').extract()
            item["leixing"]=job.xpath('./div[2]/div[2]/a/text()').extract()
            item["jieshao"]=job.xpath('./div[2]/div[4]/div[1]/font/text()').extract()
            zhuanti1=job.xpath('./div[2]/div[3]/a[1]/text()').extract()
            zhuanti2=job.xpath('./div[2]/div[3]/a[2]/text()').extract()
            zhuanti3=job.xpath('./div[2]/div[3]/a[3]/text()').extract()
            item["zhuanti"]=zhuanti1+zhuanti2+zhuanti3
            yield item



