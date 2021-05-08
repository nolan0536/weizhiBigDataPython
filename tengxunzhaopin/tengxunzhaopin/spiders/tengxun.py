import scrapy
from tengxunzhaopin.items import TengxunzhaopinItem
import json

class TengxunSpider(scrapy.Spider):
    name = 'tengxun'
    allowed_domains = ['careers.tencent.com']
    # start_urls=['https://careers.tencent.com/tencentcareer/api/post/Query?pageSize=10&pageIndex=1']
    start_urls=['https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex=1&pageSize=10&language=zh-cn&area=cn']

    def parse(self, response):
        print(response.text)
        content=json.loads(response.text)
        jobs=content["Data"]["Posts"]
        for job in jobs:
            item=TengxunzhaopinItem()
            item['zhiwei']=job["RecruitPostName"]
            item['dizhi']=job["LocationName"]
            item['fabushijian']=job["LastUpdateTime"]
            item['zhize']=job["Responsibility"]
            yield item
            pages=20
            for page in range(2,pages):
                #page='https://careers.tencent.com/tencentcareer/api/post/Query?pageSize=10&pageIndex={}'.format(page)
                page='https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex={}&pageSize=10&language=zh-cn&area=cn'.format(page)
                yield scrapy.Request(page,callback=self.parse)

















































        # tengxun_list=response.xpath('//div[@class="recruit-list"]')
        #
        # for tengxun in tengxun_list:
        #     item=TengxunzhaopinItem()
        #     item['zhiwei']=tengxun.xpath('./a/h4/text()').extract()
        #     item['dizhi']=tengxun.xpath('./a/p[1]/span[2]/text()').extract()
        #     item['fabushijian']=tengxun.xpath('./a/p[1]/span[4]/text()').extract()
        #     item['zhize']=tengxun.xpath('./a/p[2]/text()').extract()
        #     yield item
        #
        #     pages=10
        #     for page in range(2,pages):
        #         page='https://careers.tencent.com/search.html?index={}'.format(page)
        #
        #         yield scrapy.Request(page,callback=self.parse)


