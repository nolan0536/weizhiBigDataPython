import scrapy
from yangti.items import YangtiItem

class PachongSpider(scrapy.Spider):
    name = 'pachong'
    allowed_domains = ['jobs.51job.com']
    start_urls = ['https://jobs.51job.com/houduankaifa/']

    def parse(self, response):
        print(111111111111111111111111111111111111111)
        headers={
            "User-Agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        pages=5058
        for page in range(1,int(pages)):
            url = "https://jobs.51job.com/houduankaifa/p{}/".format(page)
            yield scrapy.Request(url=url,headers=headers,callback=self.parse_on,dont_filter=True)

    def parse_on(self,response):
        print(222222222222222222222222222222222222)
        jobs = response.xpath('//div[@class="detlist gbox"]/div')
        item=YangtiItem()
        for job in jobs:
            item["gongsi"]=job.xpath('./p[1]/a[1]/@title').extract()[0]
            item["gongzuo"]=job.xpath('./p[1]/span[1]/a/@title').extract()[0]
            item["chengshi"]=job.xpath('./p[1]/span[2]/text()').extract()[0]
            item["yuexin"]=job.xpath('./p[1]/span[3]/text()').extract()[0]
            item["gangweizhize"]=job.xpath('./p[3]/text()').extract()[0]
            yield item

