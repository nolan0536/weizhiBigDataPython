import scrapy
import json
from jingdongluxing.items import JingdongluxingItem

class JiudianSpider(scrapy.Spider):
    name = 'jiudian'
    allowed_domains = ['hotel.jd.com']
    start_urls = ['https://hotel.jd.com/list.html?_charset_=utf-8&cityId=36&arriveDate=2020-11-09&leaveDate=2020-11-10']

    def parse(self, response):
        print(111111111111111)
        url='https://hotel.jd.com/api/json/getHotelList'
        headers={
            'content-type':'application/x-www-form-urlencoded'
        }
        yield scrapy.FormRequest(url=url,headers=headers,callback=self.parse_on,dont_filter=True)
    def parse_on(self,response):
        print(333333333333333333333333333333)
        url='https://hotel.jd.com/api/json/getBrowseHistory?_=1604880614113'
        headers = {
            'content-type': 'application/x-www-form-urlencoded'
        }
        yield scrapy.FormRequest(url=url, headers=headers, callback=self.parse_in, dont_filter=True)
    def parse_in(self,response):
        print(222222222222222)
        result=json.loads(response.text)
        print(result)
        jobs=result["body"]["list"]
        for job in jobs:
            item=JingdongluxingItem()
            item['jiudianming']=job.get("name")
            item['xingji']=job.get("star")
            item['dizhi']=job.get("address")
            item['jiage']=job.get("price")
            yield item
