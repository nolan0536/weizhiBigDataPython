import scrapy
import json
from xuangubao.items import XuangubaoItem
class GupiaoSpider(scrapy.Spider):
    name = 'gupiao'
    allowed_domains = ['xuangubao.cn']
    start_urls = ['http://xuangubao.cn/']

    def parse(self, response):
        print(11111111111111)
        url="https://flash-api.xuangubao.cn/api/stage2/plate/top_info?count=9&fields=all"
        headers={
            'content-type':'application/json;charset=UTF-8'
        }
        yield scrapy.Request(url=url,headers=headers,callback=self.parse_in,dont_filter=True)

    def parse_in(self,response):
        print(22222222222222)
        result=json.loads(response.text)
        print(result)
        jobs1=result["data"]["bottom_plate_info"]
        for jobs2 in jobs1:
            result1=jobs2["led_falling_stocks"]["items"]
            for job in result1:
                item=XuangubaoItem()
                item['symbol']=job.get("symbol")
                item['change_percent']=job.get("change_percent")
                item['stock_chi_name']=job.get("stock_chi_name")
                item['price_change']=job.get("price_change")
                yield item

