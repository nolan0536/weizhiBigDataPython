import scrapy
import re
import json
from guosai.items import GuosaiItem
from scrapy_redis.spiders import RedisCrawlSpider

class HotelscrawlSpider(RedisCrawlSpider):
    name = 'new'
    start_urls = ['http://localhost:8080/hotelManagement/index.jsp']

    def start_requests(self):
        print(11111111111111111111111111)
        url='http://localhost:8080/hotelManagement/resources/js/kuCity.js'
        herders={
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        yield scrapy.Request(url=url,headers=herders,callback=self.start_city,dont_filter=True)
    def start_city(self,response):
        print(22222222222222222222222222222222222222222)
        response=response.text
        datas=re.findall('\[.*?\]',response,re.S)[0]
        citys=re.findall('[\u4e00-\u9fa5]+',datas,re.S)
        url='http://localhost:8080/hotelManagement/getHotels.do'
        headers={
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        for city in citys:
            data={
                'city': city,
                'busDis':'',
                'star': '[]',
                'isInn': '2',
                'page': '1'
            }
            yield scrapy.FormRequest(url=url,headers=headers,callback=self.start_totalpage,formdata=data,
                                     meta={'city':city},dont_filter=True)
    def start_totalpage(self,response):
        print(333333333333333333333333333333333333)
        city=response.meta['city']
        result=json.loads(response.text)
        totalPageNum=result.get("totalPageNum")
        url = 'http://localhost:8080/hotelManagement/getHotels.do'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        for page in range(1,int(totalPageNum)+1):
            data1 = {
                'city': city,
                'busDis': '',
                'star': '[]',
                'isInn': '2',
                'page': str(page)
            }
            yield scrapy.FormRequest(url=url,headers=headers,callback=self.start_id,formdata=data1,
                                     meta={'city':city,'page':page},dont_filter=True)

    def start_id(self,response):
        print(44444444444444444444444444444444444444444)
        result=json.loads(response.text)
        hotels=result["hotels"]
        url='http://localhost:8080/hotelManagement/hotelInfo.do'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        for hotel in hotels:
            id=hotel.get("id")
            price=hotel.get("price")
            print(price)
            data={
                'id':str(id)
            }
            yield scrapy.FormRequest(url=url,headers=headers,callback=self.parse,formdata=data,
                                      meta={'price':price},dont_filter=True)
            

    def parse(self,response):
        print(55555555555555555555555555555555555555555)
        jobs=json.loads(response.text)
        for job in jobs:
            item=GuosaiItem()
            item['diqu']=job.get("bus_district")
            item['city']=job.get("city")
            item['price']=response.meta['price']
            item['country']=job.get("country")
            item['department']=job.get("department")
            item['hotel_name']=job.get("hotel_name")
            yield item



