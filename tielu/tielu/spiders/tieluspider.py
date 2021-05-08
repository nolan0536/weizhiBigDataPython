import scrapy
import json
from tielu.items import TieluItem

class TieluspiderSpider(scrapy.Spider):
    name = 'tieluspider'
    allowed_domains = ['12306.cn']
    start_urls = ['https://www.12306.cn/index/']

    def parse(self, response):
        print(11111111111111111111111111111)
        url='https://kyfw.12306.cn/otn/lcQuery/init'
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 Safari/537.36'
        }
        yield scrapy.Request(url=url,headers=headers,callback=self.parse_on,dont_filter=True)
    def parse_on(self,response):
        print(222222222222222222222222222)
        url='https://kyfw.12306.cn/lcquery/query?train_date=2020-11-27&from_station_telecode=WFK&to_station_telecode=BJP&middle_station=&result_index=0&can_query=Y&isShowWZ=N&purpose_codes=00&lc_ciphertext=rFdkZHyN2mlEHeVvvUS63m5p%2BT2jPLPBn71V5SysQod5XqTiHZIVCQ%3D%3D'
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 Safari/537.36'
        }
        yield scrapy.Request(url=url,headers=headers,callback=self.parse_in,dont_filter=True)
    def parse_in(self,response):
        print(333333333333333333333333333)
        result=json.loads(response.text)
        print(result)
        jobs=result["data"]["middleList"]
        for job in jobs:
            item=TieluItem()
            item['shichang']=job.get("all_lishi")
            item['jiage']=job.get("all_lishi_minutes")
            item['daozhanshijian']=job.get("arrive_time")
            item['chufashijian']=job.get("start_time")
            item['riqi']=job.get("train_date")
            item['chufa']=job.get("from_station_name")
            item['daozhan']=job.get("end_station_name")
            yield item
