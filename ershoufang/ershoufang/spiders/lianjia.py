import scrapy
from ershoufang.items import ErshoufangItem

class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['bj.lianjia.com']
    start_urls = ['http://wf.lianjia.com/']

    def parse(self, response):
        print(1111111111111111111111111111111111)
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        pages=100
        for page in range(1,int(pages)):
            url="https://wf.lianjia.com/ershoufang/pg{}/".format(page)
            yield scrapy.Request(url,headers=headers,callback=self.parse_on,dont_filter=True)
    def parse_on(self,response):
        print(222222222222222222222222222222222)
        datas=response.xpath('//*[@id="content"]/div[1]/ul/li')
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        for data in datas:
            item=ErshoufangItem()
            item["title"]=data.xpath("./div[1]/div[1]/a/text()").extract()[0]
            item["xiaoquming"]=data.xpath("./div[1]/div[2]/div[1]/a/text()").extract()[0]
            shoujia=data.xpath("./div[1]/div[6]/div[1]/span/text()").extract()[0]
            item["shoujia"]=shoujia+"万"
            item["danjia"]=data.xpath("./div[1]/div[6]/div[2]/span/text()").extract()[0]
            item["mianji"]=data.xpath("./div[1]/div[3]/div[1]/text()").extract()[0]
    #         url=data.xpath("./a/@href").extract()[0]
    #         yield scrapy.Request(url,headers=headers,callback=self.parse_in,dont_filter=True)
            yield item
    # def parse_in(self,response):
    #     print(33333333333333333333333333)
    #     item=ErshoufangItem()
    #     # item["xiangxi"]=response.xpath("/html/body/div[7]/div[1]/div[2]/div/div[3]/div[2]/text()").extract()[0]
    #     item["fangyuantese"]=response.xpath("/html/body/div[7]/div[1]/div[2]/div/div[5]/div[2]/text()").extract()[0]
    #     yield item

