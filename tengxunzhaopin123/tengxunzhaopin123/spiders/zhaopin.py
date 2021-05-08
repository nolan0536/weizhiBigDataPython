import scrapy
import json
from tengxunzhaopin123.items import Tengxunzhaopin123Item

class ZhaopinSpider(scrapy.Spider):
    name = 'zhaopin'
    allowed_domains = ['careers.tencent.com']
    start_urls = ['https://careers.tencent.com/']

    def parse(self, response):
        print(111111111111111111111111111)
        url='https://careers.tencent.com/search.html'
        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 Safari/537.36'
        }
        yield scrapy.Request(url=url,headers=headers,callback=self.parse_in,dont_filter=True)

    def parse_in(self,response):
        print(2222222222222222222222222222)
        url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1605339528516&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=1&pageSize=10&language=zh-cn&area=cn'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 Safari/537.36'
        }
        yield scrapy.Request(url=url, headers=headers, callback=self.parse_on, dont_filter=True)
        pages=683
        for page in range(1,int(pages)+1):
            url='https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1605339528516&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'.format(page)
            yield scrapy.Request(url=url,callback=self.parse_on,dont_filter=True)
    def parse_on(self,response):
        print(33333333333333333333333333)
        result=json.loads(response.text)
        print(result)
        datas=result["Data"]["Posts"]
        for data in datas:
            item=Tengxunzhaopin123Item()
            item['title']=data["RecruitPostName"]
            item['dizhi']=data["LocationName"]
            item['leixing']=data["ProductName"]
            item['shijian']=data["LastUpdateTime"]
            item['url']=data["PostURL"]
            item['zhize']=data["Responsibility"]
            postid=data["PostId"]
            print(postid)
            yield item
            url='https://careers.tencent.com/jobdesc.html?postId={}'.format(postid)
            yield scrapy.Request(url=url,callback=self.parse_ons,dont_filter=True)
    def parse_ons(self,response):
        print(444444444444444444444444)
        print(response)
        item=Tengxunzhaopin123Item()
        item['yaoqiu']=response.xpath('//html/body/div/div[4]/div[3]/div/div[1]/div[4]/div[2]/ul/li/text()').extract()
        yield item

