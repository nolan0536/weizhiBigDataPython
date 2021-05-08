import scrapy
from jiudianlianxi.items import JiudianlianxiItem

class JiudianSpider(scrapy.Spider):
    name = 'jiudian'
    allowed_domains = ['hotel.jd.com']
    start_urls = ['https://wf.zu.fang.com/']

    def parse(self, response):
        print(1111111111111111111)
        jobs=response.xpath('//div[@class="houseList"]/dl')
        for job in jobs:
            item=JiudianlianxiItem()
            item['title']=job.xpath('./dd/p/a/text()').extract()
            qu=job.xpath('./dd/p[3]/a[1]/span/text()').extract()
            er=job.xpath('./dd/p[3]/a[2]/span/text()').extract()
            san=job.xpath('./dd/p[3]/a[3]/span/text()').extract()
            item['dizhi']=qu+er+san
            item['jiage']=job.xpath('./dd/div[2]/p/span/text()').extract()
            yield item
            pages=52
            for page in range(32,pages):
                url='https://wf.zu.fang.com/house/i{}/?rfss=1-994ca4af32802b871b-67'.format(page)
                yield scrapy.Request(url=url,callback=self.parse)




