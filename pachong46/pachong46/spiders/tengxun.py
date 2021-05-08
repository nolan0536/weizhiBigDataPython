import scrapy
from pachong46.items import Pachong46Item
import json
class TengxunSpider(scrapy.Spider):
    name = 'tengxun'
    allowed_domains = ['careers.tencent.com']
    start_urls = ['https://careers.tencent.com/']

    def parse(self, response):
        print(111111111111111111111111111111)
        url="https://careers.tencent.com/search.html"
        headers={
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        yield scrapy.Request(url=url,headers=headers,callback=self.parse_on,dont_filter=True)
    def parse_on(self,response):
        print(2222222222222222222222222222222222)
        for page in range(1,959):
            url="https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1617669027358&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn".format(page)
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
            yield scrapy.Request(url,headers=headers,callback=self.parse_in,dont_filter=True)
    def parse_in(self,response):
        print(33333333333333333333333333333333333)
        item=Pachong46Item()
        datas=json.loads(response.text)
        jobs=datas["Data"]["Posts"]
        for job in jobs:
            item["name"]=job.get("RecruitPostName")
            item["dizhi"]=job.get("CountryName")
            item["chengshi"]=job.get("LocationName")
            item["leixing"]=job.get("CategoryName")
            item["jishu"]=job.get("Responsibility")
            item["shijian"]=job.get("LastUpdateTime")
            item["id"]=job.get("RecruitPostId")
            yield item




