import scrapy
from ithome.items import IthomeItem

class IphoneSpider(scrapy.Spider):
    name = 'iphone'
    allowed_domains = ['ithome.com/']
    start_urls = ['https://www.ithome.com/']

    def parse(self, response):
        datas=response.xpath('//*[@id="nav"]/div[1]/div[1]/a')
        for data in datas:
            url=data.xpath('.//@href').extract()[0]
            headers={
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
            yield scrapy.Request(url="https:"+url,headers=headers,callback=self.parse_on,dont_filter=True)
    def parse_on(self,response):
        datas=response.xpath('//*[@id="list"]/div[1]/ul/li')
        for data in datas:

            url=data.xpath("./a/@href").extract()[0]
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
            yield scrapy.Request(url,headers=headers,callback=self.parse_in,dont_filter=True)

    def parse_in(self,response):
        item=IthomeItem()
        item["title"]=response.xpath('//*[@id="dt"]/div[1]/h1/text()').extract()[0]
        item["time"]=response.xpath('//*[@id="pubtime_baidu"]/text()').extract()[0]
        item["zuozhe"]=response.xpath('//*[@id="author_baidu"]/strong/text()').extract()[0]
        item["zebian"]=response.xpath('//*[@id="editor_baidu"]/strong/text()').extract()[0]
        yield item