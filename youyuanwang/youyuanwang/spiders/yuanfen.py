import scrapy
from youyuanwang.items import YouyuanwangItem
#from scrapy_redis.spiders import RedisCrawlSpider
# from scrapy.spiders import CrawlSpider
class YuanfenSpider(scrapy.Spider):
    name = 'yuanfen'
    allowed_domains = ['youyuan.com']
    start_urls = ['http://www.youyuan.com/']

    def parse(self, response):
        print(11111111111111111111111111)
        pages=10
        for page in range(1,int(pages)+1):
            url='http://www.youyuan.com/find/shanghai/mm18-0/advance-0-0-0-0-0-0-0/p{}/###'.format(page)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 Safari/537.36'
            }
            yield scrapy.Request(url=url,headers=headers,callback=self.parse_in,dont_filter=True)

    def parse_in(self,response):
        print(22222222222222222222222)
        jobs=response.xpath('//ul[@class="mian search_list"]/li')
        for job in jobs:
            url=job.xpath('./dl/dt/a/@href').extract()[0]
            print(url)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 Safari/537.36'
            }
            yield scrapy.Request(url='http://www.youyuan.com'+url,headers=headers,callback=self.parse_on,
                                 dont_filter=True)
    def parse_on(self,response):
        print(33333333333333333)
        item=YouyuanwangItem()
        item["wangming"]=response.xpath('//html/body/div[2]/div/dl/dd/div[1]/strong/text()').extract()[0]
        item["jibenxinxi"]=response.xpath('//html/body/div[2]/div/dl/dd/p/text()').extract()[0]
        item["neixindubai"]=response.xpath('//html/body/div[4]/ul/li[1]/p/text()').extract()[0]
        item["jiguan"]=response.xpath('//html/body/div[4]/ul/li[2]/div/ol[1]/li[1]/span/text()').extract()[0]
        item["tizhong"]=response.xpath('//html/body/div[4]/ul/li[2]/div/ol[1]/li[2]/span/text()').extract()[0]
        item["xueli"]=response.xpath('//html/body/div[4]/ul/li[2]/div/ol[1]/li[3]/span/text()').extract()[0]
        item["yuexin"]=response.xpath('//html/body/div[4]/ul/li[2]/div/ol[1]/li[4]/span/text()').extract()[0]
        yield item


