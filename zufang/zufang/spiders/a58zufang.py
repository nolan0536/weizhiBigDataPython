import scrapy
import chardet
from zufang.items import ZufangItem

class A58zufangSpider(scrapy.Spider):
    name = '58zufang'
    allowed_domains = ['jn.58.com']
    start_urls = ['https://jn.58.com/chuzu/']

    def parse(self, response):
        fangjians=response.xpath('//ul[@class="house-list"]/li')
        for fangjian in fangjians:
            item=ZufangItem()
            item['title']=fangjian.xpath('./div[2]/h2/a/text()').extract()
            item['leixing']=fangjian.xpath('./div[2]/p/text()').extract()
            item['weizhi']=fangjian.xpath('./div[2]/p[2]/a[1]/text()').extract()
            item['xiaoquming']=fangjian.xpath('./div[2]/p[2]/a[2]/text()').extract()
            item['jiage']=fangjian.xpath('./div[3]/div[2]/b/text()').extract()
            yield item
            pages=10
            for page in range(2,pages):
                url='https://jn.58.com/chuzu/pn{}/?PGTID=0d3090a7-0010-9c05-4262-0a39437b01e9&ClickID=2'.format(page)
                yield scrapy.Request(url=url,callback=self.parse)


