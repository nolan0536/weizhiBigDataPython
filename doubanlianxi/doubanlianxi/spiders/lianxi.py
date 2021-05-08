import scrapy
import json
from doubanlianxi.items import DoubanlianxiItem
class LianxiSpider(scrapy.Spider):
    name = 'lianxi'
    allowed_domains = ['xuangubao.com']
    start_urls = ['https://xuangubao.cn/']

    def parse(self, response):
        print(1111111111111)
        print(response.text)
        url='https://baoer-api.xuangubao.cn/api/v6/message/newsflash?limit=5&subj_ids=9,10,723,35,469,821&platform=pcweb'
        header={
            'content-type':'application/json;charset=UTF-8'
        }
        yield scrapy.Request(url=url,headers=header,callback=self.parse_in,dont_filter=True)
    def parse_in(self,response):
        print(2222222222222222)
        result=json.loads(response.text)
        print(result)
        jobs=result["data"]["messages"]
        for job in jobs:
            item=DoubanlianxiItem()
            item['id']=job.get("id")
            item['title']=job.get("title")
            item['summary']=job.get("summary")
            yield item
            
