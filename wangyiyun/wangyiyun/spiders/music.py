import scrapy
from wangyiyun.items import  WangyiyunItem
import json
class MusicSpider(scrapy.Spider):
    name = 'music'
    allowed_domains = ['music.163.com']
    start_urls = ['http://music.163.com/']

    def parse(self, response):
        print(111111111111111111111111111)
        url="https://music.163.com/#/my/m/music/playlist?id=2404322145"
        headers={
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        yield scrapy.Request(url,headers=headers,callback=self.parse_in,dont_filter=True)

    def parse_in(self,response):
        print(222222222222222222222222222222)
        url="https://music.163.com/weapi/v6/playlist/detail?csrf_token=4daca56134ac705f76db868b72d00399"
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        data={
            "params":"kM3W0BKjY8sm74ZH1NAuavrIiAD7UzcfXnrp863U+xDAXdnwDZIe9sW5+6/73KP6EWjt1mAT1W6/kEsmLDBvuEB5cvjc/cwmwYQ4rSeO0XORHR+aHWNyPKHK72ml8lzgiV2m2LG7Jj7jkgp7j2YsUEF96xKRzzlGxiFO273Udz0M3OLmI4fxdqWhj1UNS3lKJ2GCzN7+kE+gfzPcTE7TLg0lMmZHGLew/QJ27T2nFhw=",
            "encSecKey":"a8ef09f88e67f291a62d0d58321ff4b1b0059de079e2f63455e0835930668623dfe97d8dc6479b03079efb905a628a1fbd9374c688ab3ac8335faf7e098a7c11ceccefdb18435adf2095ef5dd814b20f0130b466148652f4117274de16c1e3da3dcca2828525b30d859ab783c5c91d2576171ae1d1c3a26c8d2ce83e0c3c748d"
        }
        yield scrapy.FormRequest(url,headers=headers,callback=self.parse_on,formdata=data,dont_filter=True)

    def parse_on(self,response):
        print(333333333333333333333333333333333)
        item=WangyiyunItem()
        result=json.loads(response.text)
        datas=result['playlist']['tracks']
        for data in datas:
            item["geming"]=data.get("name")
            job = data["ar"][0]
            print(job)
            jobs = data["al"]
            print(jobs)
            item["geshou"]=job.get("name")
            item["id"]=data.get("id")
            item["picstr"] = jobs.get('pic_str')
            item["zhuanji"]=jobs.get('name')
            item["picurl"]=jobs.get('picUrl')
            yield item
