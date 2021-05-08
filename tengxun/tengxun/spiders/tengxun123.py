import scrapy
from tengxun.items import TengxunItem
import json
class Tengxun123Spider(scrapy.Spider):
    name = 'tengxun123'
    allowed_domains = ['careers.tencent.com']
    start_urls = ['http://careers.tencent.com/']

    def parse(self, response):
        url="https://careers.tencent.com/search.html"
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        yield scrapy.Request(url,headers=headers,callback=self.parse_in,dont_filter=True)
    def parse_in(self,response):
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        pages=803
        for page in range(1,int(pages)):
            url="https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1609326656337&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn".format(page)
            yield scrapy.Request(url,headers=headers,callback=self.parse_on,dont_filter=True)
    def parse_on(self,response):
        result=json.loads(response.text)
        jobs=result["Data"]["Posts"]
        for job in jobs:
            item=TengxunItem()
            item["guojia"]=job.get("CountryName")
            item["chengshi"]=job.get("LocationName")
            yield item

