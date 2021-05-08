import scrapy
import json
from tengxun34.items import Tengxun34Item
class TengxunSpider(scrapy.Spider):
    name = 'tengxun'
    allowed_domains = ['careers.tencent.com']
    start_urls = ['https://careers.tencent.com/']

    def parse(self, response):
        # print(11111111111111111111111111111111)
        url="https://careers.tencent.com/search.html"
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        yield scrapy.Request(url,headers=headers,callback=self.parse_in,dont_filter=True)
    def parse_in(self,response):
        # print(2222222222222222222222222222222222222222)

        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        pages=904
        for page in range(1,int(pages)+1):
            print(page)
            url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1614817098969&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn".format(page)
            yield scrapy.Request(url,headers=headers,callback=self.parse_on,dont_filter=True)
    def parse_on(self,response):
        # print(3333333333333333333333333333333)
        # print(response)
        result=json.loads(response.text)
        datas=result["Data"]["Posts"]
        print(datas)
        for data in datas:
            item=Tengxun34Item()
            item["CategoryName"]=data.get("CategoryName")
            item["guojia"]=data.get("CountryName")
            item["diqu"]=data.get("LocationName")
            item["time"]=data.get("LastUpdateTime")
            item["gangwei"]=data.get("RecruitPostName")
            item["postid"]=data.get("PostId")
            yield item


