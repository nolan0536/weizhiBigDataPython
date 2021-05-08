import scrapy
from bizhan.items import BizhanItem


class GuichuSpider(scrapy.Spider):
    name = 'guichu'
    allowed_domains = ['search.bilibili.com']
    start_urls = ['https://www.bilibili.com/']

    def parse(self, response):
        print(11111111111111111111111111111)
        pages=50
        for page in range(1,int(pages)):
            url="https://search.bilibili.com/all?keyword=%E9%AC%BC%E7%95%9C&from_source=nav_suggest_new&page={}".format(page)
            headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
            yield scrapy.Request(url=url,headers=headers,callback=self.parse_in,dont_filter=True)
    def parse_in(self,response):
        print(22222222222222222222222222222222)
        jobs=response.xpath('//div[@id="all-list"]/div[1]/ul/li')

        for job in jobs:
            item = BizhanItem()
            print(job)
            item["title"]=job.xpath('./a//@title').extract()[0]
            item["lianjie"]=job.xpath('./a//@href').extract()[0]
            url=job.xpath('./a/@href').extract()[0]
            print(url)
            headers={
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
            yield item
            yield scrapy.Request("https:"+url,headers=headers,callback=self.parse_on,dont_filter=True)

    def parse_on(self,response):
        print(3333333333333333333333333333)
        print(response)
