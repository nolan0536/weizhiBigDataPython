import scrapy
from quanguozhaopin.items import QuanguozhaopinItem

class ZhaopinSpider(scrapy.Spider):
    name = 'zhaopin'
    allowed_domains = ['zp.cc']
    start_urls = ['http://www.zp.cc/job/beijing/']

    def parse(self, response):
        print(11111111111111111111111111)
        jobs=response.xpath('//div[@class="job_left_sidebar"]/div')
        for job in jobs:
            url=job.xpath('./div[2]/div[3]/a/@href').extract()[0]
            print(url)
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 Safari/537.36'
            }

            yield scrapy.Request(url=url,headers=headers,callback=self.parse_in,dont_filter=True)
            pages=44
            for page in range(2,int(pages)+1):
                url='http://www.zp.cc/job/beijing/index.php?all=0_0_0_0_0_0_0_0&tp=0&page={}'.format(page)
                yield scrapy.Request(url=url,callback=self.parse)
    def parse_in(self,response):
        print(2222222222222222222222222222)
        item=QuanguozhaopinItem()
        item['zhiwei']=response.xpath('//div[@class="job_details_top"]/div/div[2]/div/h1/text()').extract()
        item['yuexin']=response.xpath('//div[@class="job_details_top"]/div/div[2]/div/div[1]/span/text()').extract()
        item['dizhi']=response.xpath('//div[@class="job_details_top"]/div/div[2]/div/div[2]/text()').extract()
        item['zhiweimiaoshu']=response.xpath('//div[@class="job_details_top"]/div/div[2]/div/div[3]/span/text()').extract()
        item['xinxi']=response.xpath('//div[@class="w1200"]/div/div[2]/div[2]/p/text()').extract()
        yield item

