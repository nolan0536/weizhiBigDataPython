import scrapy
from diba.items import DibaItem
import re
class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['23us.com']
    start_urls = ['http://23us.com/']

    def parse(self, response):
        print(1111111111111111111)
        url='https://www.23us.com/html/64/64889/'
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 Safari/537.36'
        }
        yield scrapy.Request(url=url,headers=headers,callback=self.parse_on,dont_filter=True)
    def parse_on(self,response):
        print(22222222222222222222222222222)
        # print(response.text)
        jobs=response.xpath('//*[@id="at"]/tr/td')
        # result=response.xpath('//*[@id="a_main"]/div[2]/dl/dd[7]/text()[1]').extract()
        # print(result)
        for job in jobs:
            url=job.xpath('./a/@href').extract()[0]
            print(url)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 Safari/537.36'
            }
            yield scrapy.Request(url='https://www.23us.com/html/64/64889/'+url,headers=headers,callback=self.parse_in,
                                 dont_filter=True)
    def parse_in(self,response):
        print(33333333333333333333333333333333)
        print(response)
        result=response.text
        item=DibaItem()
        item['biaoti']=response.xpath('//*[@id="amain"]/dl/dd[1]/h1/text()').extract()
        item['neirong']=response.xpath('//*[@id="contents"]/text()').extract()
        # item['neirong']=re.findall(r'<dd id="contents" style="font-size: 22px; color: rgb(0, 0, 0);">(.*?)</dd>',result,re.S)
        yield item




