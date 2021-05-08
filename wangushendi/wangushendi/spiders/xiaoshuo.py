import scrapy
from wangushendi.items import WangushendiItem
import re
class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['xdingdiannn.com']
    start_urls = ['http://www.xdingdiann.com/ddk24020/']

    def parse(self, response):
        jobs=response.xpath('//div[@id="list"]/dl/dd')
        for job in jobs:
            url=job.xpath('./a/@href').extract()[0]
            print(url)
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 Safari/537.36'
            }
            yield scrapy.Request(url='http://www.xdingdiann.com'+url,headers=headers,callback=self.parse_in,dont_filter=True)
    def parse_in(self,response):
        print(22222222222222)
        print(response)
        jobs=response.xpath('//div[@class="content_read"]')
        item=WangushendiItem()
        item["zhangming"]=jobs.xpath('./div[2]/div[2]/h1/text()').extract()
        result=response.text
        item["xiaoshuo"]=re.findall(r'<div id="content">(.*?)<script>',result,re.S)[0]
        yield item
