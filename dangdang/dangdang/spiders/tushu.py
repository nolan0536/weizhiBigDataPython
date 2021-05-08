import scrapy
from dangdang.items import DangdangItem

class TushuSpider(scrapy.Spider):
    name = 'tushu'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=python']

    def parse(self, response):
        books=response.xpath('//ul[@class="bigimg"]/li')

        for book in books:
            item=DangdangItem()
            item["name"]=book.xpath('./a[@class="pic"]/@title').extract()
            item["price"]=book.xpath('./p/span[@class="search_now_price"]/text()').extract()
            item["author"]=book.xpath('./p/span[1]/a[1]/text()').extract() if len(book.xpath('./p/span[1]/a[1]/@title').extract())>0 else '无作者信息'
            item["press"]=book.xpath('./p/span[3]/a/@title').extract() if len(book.xpath('./p/span[3]/a/@title').extract())>0 else '无出版信息'
            item["pingjia"]=book.xpath('./p[4]/a/text()').extract()    #评价
            item["time"]=book.xpath('./p[5]/span[2]/text()').extract() if len(book.xpath('./p[5]/span[2]/text()').extract())>0 else '无出版时间'
            item["jianjie"]=book.xpath('./p/text()').extract() if len(book.xpath('./p[2]/text()').extract())>0 else '无简介'
            yield item
         #翻页操作
            pageNum =10

            for page in range(2,pageNum):
                page = 'http://search.dangdang.com/?key=python&act=input&page_index={}'.format(page)

                yield scrapy.Request(page,callback=self.parse)
