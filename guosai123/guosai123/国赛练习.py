import scrapy
import re
import json
from guosai123.items import Guosai123Item
class GuosaiSpider(scrapy.Spider):
    name = 'guosai'
    allowed_domains = ['localhost:8080']
    start_urls = ['http://localhost:8080/hotelManagement/index.jsp']

    def parse(self, response):
        print(111111111111111111)
        url="http://localhost:8080/hotelManagement/resources/js/kuCity.js"
        headers={
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
        }
        yield scrapy.Request(url=url,headers=headers,callback=self.parse_city,dont_filter=True)

    def parse_city(self,response):
        print(22222222222222222222222)
        result=response.text
        job_citys=re.findall('\[.*?\]',result,re.S)[0]
        citys=re.findall('[\u4e00-\u9fa5]+',job_citys,re.S)
        for city in citys:
            url = 'http://localhost:8080/hotelManagement/getHotels.do'
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
            }
            data1={
                'city': city,
                'busDis':'',
                'star': '[]',
                'isInn': '2',
                'page': '1'
            }
            yield scrapy.FormRequest(url=url,headers=headers,formdata=data1,meta={'city':city},
                                     callback=self.parse_totalpage,dont_filter=True)
    def parse_totalpage(self,response):
        print(33333333333333333333)
        city=response.meta["city"]
        result=json.loads(response.text)
        totalPageNum=result['totalPageNum']
        url = 'http://localhost:8080/hotelManagement/getHotels.do'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        for page in range(1,int(totalPageNum)+1):
            data2={
                'city': city,
                'busDis':'',
                'star': '[]',
                'isInn': '2',
                'page': str(page)
            }
            yield scrapy.FormRequest(url=url,headers=headers,formdata=data2,
                                     callback=self.parse_id,dont_filter=True)
    def parse_id(self,response):
        print(4444444444444444)
        url='http://localhost:8080/hotelManagement/hotelInfo.do'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        result=json.loads(response.text)
        dicts=result['hotels']
        for dict in dicts:
            id=dict.get('id')
            price=dict.get('price')
            data={
                'id': str(id)
            }
            yield scrapy.FormRequest(url=url,headers=headers,formdata=data,meta={'price':price},
                                     callback=self.parse_on,dont_filter=True)
    def parse_on(self,response):
        pass


