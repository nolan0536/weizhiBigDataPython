import scrapy
from mingrenmingyan.items import MingrenmingyanItem

class MingyanSpider(scrapy.Spider):
    name = 'mingyan'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']
    def parse(self,response):
        print(333333333333333333333333)
        pages=30
        for page in range(1,int(pages)):
            url="http://quotes.toscrape.com/page/{}/".format(page)
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
            yield scrapy.Request(url=url,headers=headers,callback=self.parse_on)

    def parse_on(self, response):
        print(1111111111111111111111111)
        result=response.xpath('/html/body/div[1]/div[2]/div[1]/div')
        headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        for data in result:
            item=MingrenmingyanItem()
            item["mingyan"]=data.xpath('./span[1]/text()').extract()
            item["zuozhe"]=data.xpath('./span[2]/small/text()').extract()
            url=data.xpath('./span[2]/a/@href').extract()[0]
            item["biaoqian"]=data.xpath('./div/meta/@content').extract()
            yield scrapy.Request(url="http://quotes.toscrape.com"+url,headers=headers,callback=self.parse_in,dont_filter=True)
            yield item
    def parse_in(self,response):
        print(22222222222222222222222)
        item=MingrenmingyanItem()
        item["zuozhejianli"]=response.xpath("/html/body/div/div[2]/div/text()").extract()
        yield item



