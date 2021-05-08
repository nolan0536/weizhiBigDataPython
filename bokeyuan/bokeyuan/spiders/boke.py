import scrapy
from bokeyuan.items import BokeyuanItem

class BokeSpider(scrapy.Spider):
    name = 'boke'
    allowed_domains = ['cnblogs.com']
    start_urls = ['http://cnblogs.com/']

    # def parse(self, response):
    #     print(111111111111111111111111111111)
    #     url="https://zzk.cnblogs.com/s?w=python"
    #     headers={
    #         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
    #     }
    #     yield scrapy.Request(url,headers=headers,callback=self.parse_in,dont_filter=True)
    def parse(self,response):
        print(3333333333333333333333333333333)
        pages=200
        for page in range(1,int(pages)):
            url="https://www.cnblogs.com/#p{}".format(page)
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
            yield scrapy.Request(url,headers=headers,callback=self.parse_on,dont_filter=True)
    def parse_on(self,response):
        print(22222222222222222222222222222222222)
        datas=response.xpath('//*[@id="post_list"]/article')
        for data in datas:
            item=BokeyuanItem()
            item["url"]=data.xpath('./section/div[1]/a/@href').extract()[0]
            item["zuozhe"]=data.xpath('./section/footer/a/span/text()').extract()[0]
            item["time"]=data.xpath('./section/footer/span[1]/span/text()').extract()[0]
            item["title"]=data.xpath('./section/div/a/text()').extract()[0]
            print(item)
            yield item


