import scrapy
from jobbole.items import JobboleItem
class BoleSpider(scrapy.Spider):
    name = 'bole'
    allowed_domains = ['jobbole.com']
    start_urls = ['http://www.jobbole.com/']

    def parse(self, response):
        url="http://www.jobbole.com/zhengquan/ggfx/"
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        yield scrapy.Request(url,headers=headers,callback=self.parse_in,dont_filter=True)
    def parse_in(self,response):
        print(11111111111111111111111)
        pages=478
        for page in range(1,int(pages)):
            url="http://www.jobbole.com/zhengquan/ggfx/index_{}.html".format(page)
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
            yield scrapy.Request(url,headers=headers,callback=self.parse_on,dont_filter=True)
    def parse_on(self,response):
        print(2222222222222222222222222222)
        datas=response.xpath('//*[@id="stock-left-graphic"]/div')
        for data in datas:
            item=JobboleItem()
            item["title"]=data.xpath('./div[2]/a/h1/text()').extract()
            item["jianjie"]=data.xpath('./div[2]/div[2]/text()').extract()
            item["time"]=data.xpath('./div[2]/div[3]/div[1]/span/text()').extract()
            url=data.xpath('./div[2]/div[1]/a/@href').extract()[0]
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
            yield scrapy.Request(url="http://www.jobbole.com"+url,headers=headers,callback=self.parse_one,dont_filter=True)
    def parse_one(self,response):
        print(333333333333333333333333333333)
        item=JobboleItem()
        item["zhengwen"]=response.xpath("/html/body/div[3]/div[1]/div[3]/div[3]/text()").extract()
        yield item



