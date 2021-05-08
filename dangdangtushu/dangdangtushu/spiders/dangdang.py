import scrapy
from dangdangtushu.items import DangdangtushuItem

class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['book.dangdang.com']
    start_urls = ['http://book.dangdang.com/']

    def parse(self, response):
        print(11111111111111111111111111111111111111111111)
        headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        pages=100
        for page in range(1,int(pages)+1):
            print(page)
            url="http://category.dangdang.com/pg{}-cp01.16.00.00.00.00.html".format(page)
            yield scrapy.Request(url,headers=headers,callback=self.parse_in,dont_filter=True)
    def parse_in(self,response):
        print(22222222222222222222222222222222222222222)
        books=response.xpath('//*[@id="component_59"]/li')
        for book in books:
            item=DangdangtushuItem()
            item["title"]=book.xpath('./a/@title').extract()
            item["shiyongxing"]=book.xpath('./p[2]/text()').extract()
            item["jiage"]=book.xpath('./p[3]/span[1]/text()').extract()
            item["zuozhe"]=book.xpath('./p[5]/span[1]/a/@title').extract()
            yield item
        

