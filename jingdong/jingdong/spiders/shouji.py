import scrapy
from jingdong.items import JingdongItem

class ShoujiSpider(scrapy.Spider):
    name = 'shouji'
    allowed_domains = ['search.jd.com']
    start_urls = ['http://search.jd.com/']

    def parse(self, response):
        headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        pages=100
        for page in range(1,int(pages)):
            url="https://search.jd.com/Search?keyword=iPhone&ev=exbrand_Apple%5E&page={}".format(page)
            yield scrapy.Request(url,headers=headers,callback=self.parse_in,dont_filter=True)
    def parse_in(self,response):
        datas=response.xpath('//*[@id="J_goodsList"]/ul/li')
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        for data in datas:
            url=data.xpath('./div[1]/div[1]/a/@href').extract()[0]
            yield scrapy.Request(url="https:"+url,headers=headers,callback=self.parse_on,dont_filter=True)
    def parse_on(self,response):
        item=JingdongItem()
        item["title"]=response.xpath("/html/body/div[6]/div/div[2]/div[1]/text()").extract()
        item["jiage"]=response.xpath("/html/body/div[6]/div/div[2]/div[3]/div/div[1]/div[2]/span[1]/span[2]/text()").extract()
        item["dianpu"]=response.xpath('//*[@id="crumb-wrap"]/div/div[2]/div[2]/div[1]/div/a/text()').extract()
        item["pinglunshu"]=response.xpath('/html/body/div[6]/div/div[2]/div[3]/div/div[2]/div[1]/a/text()').extract()
        item["fuwu"]=response.xpath('/html/body/div[6]/div/div[2]/div[2]/div[1]/text()').extract()
        yield item