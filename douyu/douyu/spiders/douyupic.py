import scrapy
import json
from douyu.items import DouyuItem

class DouyupicSpider(scrapy.Spider):
    name = 'douyupic'
    allowed_domains = ['capi.douyucdn.cn']
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    offset = 0
    start_urls = [url+str(offset)]

    def parse(self, response):
        data=json.loads(response.text)["data"]
        print("--------")
        for each in data:
            item=DouyuItem()
            item["nick_name"]=each["nickname"]
            item["image_link"]=each["vertical_src"]
            print("+++++++++"+str(item))
            yield item
            self.offset+=1
            yield scrapy.Request(self.url+str(self.offset),callback=self.parse)
        pass
