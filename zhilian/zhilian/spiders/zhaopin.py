import scrapy
from zhilian.items import ZhilianItem

class ZhaopinSpider(scrapy.Spider):
    name = 'zhaopin'
    allowed_domains = ['sou.zhaopin.com']
    start_urls = ["https://sou.zhaopin.com/?jl=765&kw=python&p=1"]

    def parse(self, response):
        pages=20
        for page in range(1,pages):
            url="https://sou.zhaopin.com/?jl=765&kw=python&p={}".format(page)
            headers={
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
            yield scrapy.Request(url,headers=headers,callback=self.parse_in,dont_filter=True)
    def parse_in(self,response):
        print(1111111111111111111111111111111111)
        # item=[]
        datas=response.xpath('//*[@id="positionList-hook"]/div[1]/div')
        for data in datas:
            url=data.xpath("./a/@href").extract()[0]
            print(url)
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
            yield scrapy.Request(url, headers=headers, callback=self.parse_on, dont_filter=True)
        #     print(data)
        #     item["title"]=data.xpath("./a/div[1]/div[1]/span/span/text()").extract()[0]
        #     item["yuexin"]=data.xpath("./a/div[2]/div[1]/p/text()").extract()
        #     item["dizhi"]=data.xpath("./a/div[2]/div[1]/ul/li[1]/text()").extract()
        #     item["xueli"]=data.xpath("./a/div[2]/div[1]/ul/li[3]/text()").extract()
        #     item["biaoqian"]=data.xpath("./a/div[3]/div[1/div/text()").extract()
        # yield item
    def parse_on(self,response):
        print(response.text())

