import scrapy
import re
import json
from shengsai123.items import Shengsai123Item

class ShengsaiSpider(scrapy.Spider):
    name = 'shengsai'

    # allowed_domains = ['localhost:8080/']
    start_urls = ['http://localhost:8080/resale/index.jsp']

    def start_requests(self):
        print(11111111111111111111111111)
        # 请求零售网站的首页url
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse_table_url)
    def parse_table_url(self,response):
        print(2222222222222222222222222222)
        ul_tages=response.xpath('//ul[@class="nav navbar-nav"]//@href').extract()
        keys=[]
        employee=re.findall('webpage/(.*?).jsp',ul_tages[1])[0]
        salesFactSample=re.findall('webpage/(.*?).jsp',ul_tages[4])[0]
        keys.append(employee)
        keys.append(salesFactSample)
        # print(keys)
        # for key in keys:
        #     yield scrapy.FormRequest('http://localhost:8080/resale/list'+key.title()+'.do',
        #                              formdata={'page':'1'},callback=self.parse_totalpage,meta={'key':key})

        for key in keys:
            print(key)
            # 拼接成一个新的url
            yield scrapy.FormRequest('http://localhost:8080/resale/list' + key.title() + '.do',
                                     formdata={'page': '1'}, callback=self.parse_is_detail,
                                     meta={'key': key})  # 初始化key属性

    def parse_is_detail(self,response):
        print(333333333333333333333333333333)
        result=json.loads(response.text)
        totalPageNum=result["totalPageNum"]
        key=response.meta['key']
        if key=="salesFactSample":
            for page in range(1,int(totalPageNum)+1):
                yield scrapy.FormRequest(url='http://localhost:8080/resale/listSalesfactsample.do',
                                         formdata={'page':str(page)},callback=self.parse)
        else:
            yield scrapy.FormRequest(url='http://localhost:8080/resale/get'+key.title()+'.do',
                                     formdata={'page':str(totalPageNum)},callback=self.parse_id,
                                     meta={'key':key,'totalPageNum':str(totalPageNum)})
    def parse_id(self,response):
        print(4444444444444444444444444)
        result=json.loads(response.text)
        key=response.meta['key']
        totalPageNum=response.meta['totalPageNum']
        detail = result[key+'s']
        last_zuiid=len(detail)
        id_numb=((int(totalPageNum)-1)*15)+int(last_zuiid)
        for id in range(0,int(id_numb)+1):
            yield scrapy.FormRequest(url='http://localhost:8080/resale/get'+key.title()+'.do',
                                     formdata={'id':str(id)},callback=self.parse_on,
                                     meta={'key':key})
    def parse_on(self,response):
        print(555555555555555555555555555555555)
        result=json.loads(response.text)
        item=Shengsai123Item()
        key=response.meta["key"]
        if key=="employee":
            item["employee"]=result
            yield item


    def parse(self, response):
        print(66666666666666666666666666666)
        item = Shengsai123Item()
        result=json.loads(response.text)
        print(type(result))
        print(result)
        sames=result['salesFactSamples']


        print(777777777777)
        for same in sames:

            item['salesFactSample']=same
            yield item
