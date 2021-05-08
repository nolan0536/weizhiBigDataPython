import scrapy
import json
from doubanfenlei.items import DoubanfenleiItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/tag/#/']

    def parse(self, response):
        print(11111111111111)
        url='https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0'
        headers={
            'Content-Type':'application/json;charset=utf-8'
        }
        for i in range(0,11):
            formdata={
                'sort':'U',
                'range':'0,10',
                'tags':'',
                'start':str(i*20)
            }
            temp=json.dumps(formdata)
            yield scrapy.Request(url=url,headers=headers,body=temp,callback=self.parese_in,dont_filter=True)
#get和post都可以通过body来传递参数
    def parese_in(self,response):
        print(2222222222222222)
        print(response.text)
        result=json.loads(response.text)
        print(result)
        jobs=result['data']
        for job in jobs:
            item=DoubanfenleiItem()
            item['daoyan']=job.get("directors")
            item['pingfen']=job.get("rate")
            item['zhuyan']=job.get("casts")
            item['url']=job.get("url")
            item['title']=job.get("title")
            yield item
            # pages=10
            # for page in range(1,pages):
            #     url='https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start={}'.format(page*20)
            #     yield scrapy.Request(url=url,callback=self.parese_in)
                

