import scrapy
from xiaoshuopaihang.items import XiaoshuopaihangItem

class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['qidian.com']
    start_urls = ['https://www.qidian.com/rank/yuepiao']

    def parse(self, response):
        books=response.xpath('//*[@id="rank-view-list"]/div/ul/li')
        for book in books:
            item=XiaoshuopaihangItem()
            item["title"]=book.xpath('./div[2]/h4/a/text()').extract()
            item["zuozhe"]=book.xpath('./div[2]/p[1]/a[1]/text()').extract()
            item["leixing"]=book.xpath('./div[2]/p[1]/a[2]/text()').extract()
            item["zhangjie"]=book.xpath('./div[2]/p[3]/a/text()').extract()
            item["time"]=book.xpath('./div[2]/p[3]/span/text()').extract()
            yield item

            pagenum=5
            for page in range(2,pagenum):
                page='https://www.qidian.com/rank/yuepiao?page={}'.format(page)
                yield scrapy.Request(page,callback=self.parse)



