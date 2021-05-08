import scrapy
import json
from xiecheng.items import XiechengItem
class BeijingSpider(scrapy.Spider):
    name = 'beijing'
    allowed_domains = ['hotels.ctrip.com']
    start_urls = ['https://hotels.ctrip.com/?allianceid=4897&sid=798178&bd_vid=11450967791830399025']

    def parse(self, response):
        print(1111111111111111)
        url="https://hotels.ctrip.com/hotel/beijing1#ctm_ref=hod_hp_sb_lst"
        headers={
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        yield scrapy.Request(url=url,headers=headers,callback=self.parse_in,dont_filter=True)
    def parse_in(self,response):
        print(22222222222222)
        url="https://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx"
        headers = {
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        for page in range(1,20):

            data={
                'page':str(page)
            }
            yield scrapy.FormRequest(url=url,formdata=data,headers=headers,callback=self.parse_on,
                                     dont_filter=True)
    def parse_on(self,response):
        print(33333333333333)
        result=json.loads(response.text)
        print(result)
        jobs=result["hotelMapStreetJSON"]
        for job in jobs:
            item=XiechengItem()
            item["name"]=job["name"]
            item["dizhi"]=job["address"]
            item["pingfen"]=job["score"]
            yield item


