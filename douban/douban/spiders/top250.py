import scrapy
from douban.items import DoubanItem

class Top250Spider(scrapy.Spider):
    name = 'top250'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        dianyings=response.xpath('//ol[@class="grid_view"]/li')
        for dianying in dianyings:
            item=DoubanItem()
            item['titlecn']=dianying.xpath('./div/div[2]/div/a/span[1]/text()').extract()[0]
            item['titleen']=dianying.xpath('./div/div[2]/div/a/span[2]/text()').extract()[0]
            item['dyxx']=dianying.xpath('./div/div[2]/div[2]/p/text()').extract()[0]
            item['pingfen']=dianying.xpath('./div/div[2]/div[2]/div/span[2]/text()').extract()[0]
            item['pingjiashu']=dianying.xpath('./div/div[2]/div[2]/div/span[4]/text()').extract()[0]
            item['jianshu']=dianying.xpath('./div/div[2]/div[2]/p/span[1]/text()').extract()[0]
            yield item
            pageNum = 10

            for page in range(1, pageNum):
                page = 'https://movie.douban.com/top250?start={}&filter='.format(page*25)

                yield scrapy.Request(page, callback=self.parse)




