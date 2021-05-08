import scrapy
import re
import json
from guosai.items import GuosaiItem

class HotelscrawlSpider(scrapy.Spider):
    name = 'hotelscrawl'

    start_urls = ['http://localhost:8080/hotelManagement/index.jsp']

    def start_requests(self):
        url='http://localhost:8080/hotelManagement/resources/js/kuCity.js'
        headers={
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'  #请求头 可以在F12检查网络中的html中 xhr
        }
        yield scrapy.FormRequest(url=url,headers=headers,callback=self.get_city)


    def get_city(self,response):

        response=response.text
        print(response)

        response_first = re.findall('\[.*?\]', response, re.S) # url='http://localhost:8080/hotelManagement/resources/js/kuCity.js'就是搜索栏
        print(response_first)
        all_cities=re.findall('[\u4e00-\u9fa5]+',response_first[0])
        print("3333" + str(all_cities))
        url='http://localhost:8080/hotelManagement/getHotels.do' #酒店预订页面的url
        headers={
            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'
        }
        for city in all_cities:
            data={
                'city':city,
                'busDis':'',
                'star':'',
                'isInn':'2',
                'page':'1'
            }

            yield scrapy.FormRequest(url=url,headers=headers,      #把信息传递下去
                                     formdata=data,callback=self.get_page,meta={'city':city},dont_filter=True)

    def get_page(self,response):
        total_page_num=json.loads(response.text)['totalPageNum'] #获取酒店预订页面的总页数

        city=response.meta['city']  #传递城市
        url='http://localhost:8080/hotelManagement/getHotels.do'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        for page in range(1,total_page_num+1):  #把所有的页数都循环点击一遍
            data2={
                'city':city,
                'busDis':'',
                'star':'',
                'isInn':'2',
                'page':str(page)
            }
            yield  scrapy.FormRequest(url=url,headers=headers,
                                      formdata=data2,callback=self.get_hotel_id,meta={'city':city,'page':str(page)})

    def get_hotel_id(self,response):
        hotel_id_list =json.loads(response.text)['hotels'] #获取hotels里的信息  #里面是网页的全部信息
        print(hotel_id_list)
        url='http://localhost:8080/hotelManagement/hotelInfo.do'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        for hotels_dict in hotel_id_list:
            hotel_id=hotels_dict.get('id') #获取id
            price=hotels_dict.get('price') #获取价格
            data_id={
                'id':str(hotel_id)  #需要把id转化为str类型
            }
            yield scrapy.FormRequest(url=url,headers=headers,
                                     formdata=data_id,callback=self.parse,
                                     meta={'price':price},dont_filter=True)
    def parse(self, response):

        item=GuosaiItem()
        hotel_dict=json.loads(response.text)[0]
        # print(999999999999999999999999999999999999999999)
        # print(hotel_dict)
        hotel = {}
        detail = {}
        detail['SEQ'] = hotel_dict.get('seq')
        detail['国家'] = hotel_dict.get('country') #
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
        hotel['detail'] =detail
        item['result']=hotel
        # print(item)
        yield item

