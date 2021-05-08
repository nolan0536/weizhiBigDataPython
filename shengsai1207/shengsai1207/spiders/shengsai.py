import scrapy
import re
import json
from shengsai1207.items import Shengsai1207Item
class ShengsaiSpider(scrapy.Spider):
    name = 'shengsai'
    allowed_domains = ['localhost:8080']
    start_urls = ['http://localhost:8080/resale/index.jsp']
    def start_requests(self):
        print(1111111111111111111111111111111111111)
        # 请求零售网站的首页url
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_table_url)
    def parse_table_url(self, response):
        print(111111111111111111111111111111111)
        url_heads=response.xpath('//ul[@class="nav navbar-nav"]//@href').extract()
        keys=[]
        employee=re.findall("webpage/(.*?).jsp",url_heads[1])[0]
        salesFactSample=re.findall("webpage/(.*?).jsp",url_heads[4])[0]
        keys.append(employee)
        keys.append(salesFactSample)
        for key in keys:
            print(key)
            url="http://localhost:8080/resale/list"+key.title()+".do"
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }
            data={
                "page": "1"
            }
            yield scrapy.FormRequest(url=url,headers=headers,formdata=data,dont_filter=True,
                                     callback=self.parse_totalpage,meta={'key':key})

    def parse_totalpage(self,response):
        print(2222222222222222222222222222222)
        key=response.meta["key"]
        result=json.loads(response.text)
        totalPageNum=result["totalPageNum"]
        if key=="salesFactSample":
            url = "http://localhost:8080/resale/listSalesfactsample.do"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }
            for page in range(0,int(totalPageNum)+1):
             data={
                 "page":str(page)
             }
             yield scrapy.FormRequest(url,headers=headers,callback=self.parse_on,formdata=data,
                                      dont_filter=True)
        else:
            url = "http://localhost:8080/resale/listEmployee.do"
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
            }
            data={
                "page": str(totalPageNum)
            }
            yield scrapy.FormRequest(url,headers=headers,callback=self.parse_id,dont_filter=True,
                                     formdata=data,meta={'totalpage':totalPageNum,'key':key})
    def parse_id(self,response):
        print(333333333333333333333333333333333333333)
        totalpage=response.meta["totalpage"]
        key=response.meta["key"]
        result=json.loads(response.text)
        zui_ids=result[key+'s']
        zui_id=len(zui_ids)
        quan_ids=(totalpage-1)*15+zui_id
        for id in range(0,int(quan_ids)+1):
            print(id)
            data={
                "id":str(id)
            }
            # url='http://localhost:8080/resale/get'+key.title()+'Info.do'
            url="http://localhost:8080/resale/getEmployeeInfo.do"
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
            }
            yield scrapy.FormRequest(url=url, headers=headers, formdata=data, callback=self.parse_in,
                                     dont_filter=True, meta={'key': key})

    def parse_in(self,response):
        print(444444444444444444444444444444444444)
        key=response.meta["key"]
        result = json.loads(response.text)
        if key=="employee":
            item=Shengsai1207Item()
            item["employee"]=result
            yield item
    def parse_on(self,response):
        print(5555555555555555555555555555555)
        item=Shengsai1207Item()
        result=json.loads(response.text)
        sames=result["salesFactSamples"]
        for same in sames:
            item["salasfactsample"]=same
            yield item

