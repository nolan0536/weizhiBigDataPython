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
        print(555555555555555555555555)
        hotel_dict=json.loads(response.text)[0]
        item=Guosai123Item()
        hotel = {}
        detail = {}
        detail['SEQ'] = hotel_dict.get('seq')
        detail['国家'] = hotel_dict.get('country')  #
        detail['省份'] = hotel_dict.get('province')
        detail['城市'] = hotel_dict.get('city')
        detail['处于商圈'] = hotel_dict.get('bus_district')
        detail['是否为客栈'] = hotel_dict.get('is_inn')
        detail['酒店星级'] = hotel_dict.get('star_level')
        detail['业务部门'] = hotel_dict.get('department')
        detail['剩余房间'] = hotel_dict.get('num_room')
        detail['图片数'] = hotel_dict.get('num_pic')
        detail['酒店评分'] = hotel_dict.get('grade')
        detail['用户点评数'] = hotel_dict.get('num_comment')
        detail['城市平均实住间夜'] = hotel_dict.get('c_avg_real_tehr')
        detail['酒店总订单'] = hotel_dict.get('h_all_order')
        detail['酒店总间夜'] = hotel_dict.get('h_all_tehr')
        detail['酒店实住订单'] = hotel_dict.get('h_real_order')
        detail['酒店实住间夜'] = hotel_dict.get('h_real_tehr')
        detail['酒店直销订单'] = hotel_dict.get('h_direct_order')
        detail['酒店直销间夜'] = hotel_dict.get('h_direct_tehr')
        detail['酒店直销实住订单'] = hotel_dict.get('h_direct_real_order')
        detail['酒店直销实住间夜'] = hotel_dict.get('h_direct_real_tehr')
        detail['酒店直销拒单'] = hotel_dict.get('h_real_reject')
        detail['酒店直销拒单率'] = hotel_dict.get('h_pr_real_reject')
        detail['城市直销拒单率'] = hotel_dict.get('c_pr_real_reject')
        detail['拒单率是否小于等于直销城市均值'] = hotel_dict.get('is_real_reject')
        detail['最低房间价格'] = str(response.meta['price'])
        hotel['name'] = hotel_dict.get('hotel_name')
        hotel['detail'] = detail
        item['result'] = hotel
        # print(item)
        yield item


# def parse(self, response):
    #     print(11111111111111111111111)
    #     url='http://localhost:8080/hotelManagement/resources/js/kuCity.js'
    #     headers={
    #         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    #     }
    #     yield scrapy.Request(url=url,headers=headers,callback=self.parse_city,dont_filter=True)
    # def parse_city(self,response):
    #     print(22222222222222222222222)
    #     response=response.text
    #     print(response)
    #     job_citys=re.findall('\[.*?\]',response,re.S)[0]
    #     citys=re.findall('[\u4e00-\u9fa5]+',job_citys,re.S)
    #     url='http://localhost:8080/hotelManagement/getHotels.do'
    #     headers={
    #         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    #     }
    #     for city in citys:
    #         data1={
    #             'city': city,
    #             'busDis':'',
    #             'star': '[]',
    #             'isInn': '2',
    #             'page': '1'
    #         }
    #         yield scrapy.FormRequest(url=url,
    #                                  headers=headers,formdata=data1,meta={'city':city},
    #                                  callback=self.parse_total,dont_filter=True)
    # def parse_total(self,response):
    #     print(33333333333333333333333333333333)
    #     result=json.loads(response.text)
    #     totalPageNum=result['totalPageNum']
    #     city=response.meta["city"]
    #     url='http://localhost:8080/hotelManagement/getHotels.do'
    #     headers = {
    #         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    #     }
    #     for page in range(1,int(totalPageNum)+1):
    #         data2={
    #             'city': city,
    #             'busDis':'',
    #             'star': '[]',
    #             'isInn': '2',
    #             'page': str(page)
    #         }
    #         yield scrapy.FormRequest(url=url,headers=headers,meta={'city':city,'page':page},
    #                                  formdata=data2,callback=self.parse_in,dont_filter=True)
    # def parse_in(self,response):
    #     print(444444444444444444444444444)
    #     result=json.loads(response.text)
    #     print(result)
    #     list_id=result['hotels']
    #     url='http://localhost:8080/hotelManagement/hotelInfo.do'
    #     headers={
    #         'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    #     }
    #     for data_id in list_id:
    #         id=data_id.get('id')
    #         price=data_id.get('price')
    #         data={
    #             'id':str(id)
    #         }
    #         yield scrapy.FormRequest(url=url,headers=headers,meta={'price':price},
    #                                  formdata=data,callback=self.parse_on,dont_filter=True)


