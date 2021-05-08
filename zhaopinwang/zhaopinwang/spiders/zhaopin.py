import scrapy
import json
from zhaopinwang.items import ZhaopinwangItem

class ZhaopinSpider(scrapy.Spider):
    name = 'zhaopin'
    allowed_domains = ['zhaopin.com']
    start_urls = ['https://www.zhaopin.com/']

    def parse(self, response):
        print(11111111111111)
        url='https://sou.zhaopin.com/?jl=530&kw=python&kt=3'
        headers={
            'content-type': 'application/json;charset=UTF-8'
        }
        yield scrapy.Request(url=url,headers=headers,callback=self.parse_in,dont_filter=True)
    def parse_in(self,response):
        print(22222222222222)
        print(response.text)
        url=r'https://fe-api.zhaopin.com/c/i/sou?at=f391a2fdfd0a4cbb9947f7eb589ee633&rt=7e3fa7da78ef450ca93777be4c2a82cf&_v=0.35316303&x-zp-page-request-id=fd8c59846af8427f922288cba94ae6a7-1604972067492-868813&x-zp-client-id=743730a1-e140-4c37-b501-c8fbf9659fa4&MmEwMD=5ZlqYoCtrgtxeVixAXgwLW5H0Bv8M2lolHcoujatQMWjD6p5kfq62VLiU_fJ_3Q1xjJgeWaAfdciuzOTk8YylxyB28KMWvBwk.3FqNmgQ5p16ocij1SjVRyyIolBGORgx7cWiEWlida02nOucLFXwL4.4xsNDAYxqy5.xMrACpmbEPD2bnfM8E71ygr0CBQj3kW4tD6urqqNGneLfu2rM7TJLZvs.Zf7qyJMGBYCZlbpvtyLYxg4Mesajhkp3DO4qNZeGz_9kcQJIOPZtU5Z7yUMvu9ga7Yyp1roXPZghpyiaeTF4SkqqGKF9uhos962J4q_WpvSY9wIjrgnU4dONlAerqJMa6EQpRXGLmYmI17rYn_dl3vsASJM6FYp6hRmnoyGQT69GZlncptVi1g4AqhKx'
        headers={
            'content-type': 'application/json;charset=UTF-8'
        }
        for i in range(1,5):
            data={
                'at': "f391a2fdfd0a4cbb9947f7eb589ee633",
                'cityId': "530",
                'companyType': "-1",
                'employmentType': "-1",
                'eventScenario': "pcSearchedSouIndex",
                'jobWelfareTag': "-1",
                'kt': "3",
                'kw': "python",
                'pageSize': "30",
                'rt': "7e3fa7da78ef450ca93777be4c2a82cf",
                'start': str(i*30),
                'userCode': "1087495082",
                'workExperience': "-1"
            }
            yield scrapy.FormRequest(url=url,headers=headers,formdata=data,callback=self.parse_on,
                                     dont_filter=True)
    def parse_on(self,response):
        print(333333333333333333333)
        result=json.loads(response.text)
        print(result)
        jobs=result["data"]["results"]
        for job in jobs:
            item=ZhaopinwangItem()
            item['zhiwei']=job.get("jobName")
            item['gongsi']=job["company"]["name"]
            item['dizhi']=job["city"]["display"]
            item['gongzi']=job.get("salary")
            yield item

