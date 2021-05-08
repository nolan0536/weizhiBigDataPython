from resale_crawl.items import ResaleCrawlItem
import scrapy
import json
import re
from scrapy_redis.spiders import RedisCrawlSpider
class SalesSpider(RedisCrawlSpider):
    name = "xiaolianxi"
    start_urls = ['http://localhost:8080/resale/index.jsp']

    def start_requests(self):
        print(1111111111111111111111111111111111111)
        # 请求零售网站的首页url
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_table_url)
    def parse_table_url(self,response):
        print(222222222222222222222222222222222222222)
        url_pages=response.xpath('//ul[@class="nav navbar-nav"]//@href').extract()
        keys=[]
        employee=re.findall('webpage/(.*?).jsp',url_pages[1])[0]
        salesFactSample=re.findall('webpage/(.*?).jsp',url_pages[4])[0]
        keys.append(employee)
        keys.append(salesFactSample)
        for key in keys:
            print(key)
            url='http://localhost:8080/resale/list'+key.title()+'.do'
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 Safari/537.36'
            }
            data={
                'page':'1'
            }
            yield scrapy.FormRequest(url=url,headers=headers,formdata=data,
                                     meta={'key':key},callback=self.parse_totalpage,dont_filter=True)
    def parse_totalpage(self,response):
        print(333333333333333333333333333333333333333333)
        result=json.loads(response.text)
        totalPageNum=result["totalPageNum"]
        key=response.meta["key"]
        if key=="salesFactSample":
            for page in range(0,int(totalPageNum)+1):
                url='http://localhost:8080/resale/listSalesfactsample.do'
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 Safari/537.36'
                }
                data = {
                    'page': str(page)
                }
                yield scrapy.FormRequest(url=url,headers=headers,formdata=data,
                                         callback=self.parse,dont_filter=True)
        else:
            url='http://localhost:8080/resale/listEmployee.do'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 Safari/537.36'
            }
            data = {
                'page': str(totalPageNum)
            }
            yield scrapy.FormRequest(url=url,headers=headers,formdata=data,
                                     callback=self.parse_in,dont_filter=True,meta={'key':key,'totalPageNum':totalPageNum})

    def parse_in(self,response):
        print(44444444444444444444444444444444444)
        result=json.loads(response.text)
        key=response.meta["key"]
        totalPageNum=response.meta["totalPageNum"]
        zui_id=result[key+'s']
        zui_ids=len(zui_id)
        quan_ids=(totalPageNum-1)*15+zui_ids
        print(quan_ids)
        for id in range(0,int(quan_ids)+1):
            url='http://localhost:8080/resale/get'+key.title()+'Info.do'
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 Safari/537.36'

            }
            data={
                'id':str(id)
            }
            yield scrapy.FormRequest(url=url,headers=headers,formdata=data,callback=self.parse_on,
                                     dont_filter=True,meta={'key':key})
    def parse_on(self,response):
        print(5555555555555555555555555555555555)
        key=response.meta['key']
        result=json.loads(response.text)
        item=ResaleCrawlItem()
        if key=="employee":
            item['detail_data_e']=result
            yield item

    def parse(self,response):
        print(66666666666666666666666666666666)
        item=ResaleCrawlItem()
        result=json.loads(response.text)
        sames=result["salesFactSamples"]
        for same in sames:
            item["no_detail_data"]=same
            yield item



