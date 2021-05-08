import scrapy
import json
from bilibili.items import BilibiliItem
class BiliSpider(scrapy.Spider):
    name = 'bili'
    allowed_domains = ['www.bilibili.com']
    start_urls = ['http://www.bilibili.com/']

    def parse(self, response):
        print(11111111111111111111111111111)
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        totalpage=50
        for page in range(1,int(totalpage)):
            url = "https://api.bilibili.com/x/web-interface/search/type?context=&search_type=article&page={}&order=&keyword=%E9%BE%99%E7%8F%A0&category_id=&__refresh__=true&_extra=&highlight=1&single_column=0".format(page)
            yield scrapy.Request(url,headers=headers,callback=self.parse_in,dont_filter=True)

    def parse_in(self,response):
        print(22222222222222222222222222222)
        result=json.loads(response.text)
        datas=result['data']['result']
        for data in datas:
            item=BilibiliItem()
            item["title"]=data.get("title")
            item["category_name"]=data.get("category_name")
            item["desc"]=data.get("desc")
            item["type"]=data.get("type")
            yield item


