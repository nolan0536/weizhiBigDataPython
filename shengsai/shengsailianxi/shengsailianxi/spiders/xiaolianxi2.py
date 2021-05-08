import scrapy
import re
import json
from shengsailianxi.items import ShengsailianxiItem
class XiaolianxiSpider(scrapy.Spider):
    name = 'xiaolianxi'
    start_urls = ['http://localhost:8080/resale/index.jsp']

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url,callback=self.parse_table_url)

    def parse_table_url(self, response):
        url_key=[]
        url_tager=response.xpath('//ul[@class="nav navbar-nav"]//@href').extract()
        employee=re.findall(r'webpage/(.*?).jsp',url_tager[1])[0]
        salesFactSample=re.findall(r'webpage/(.*?).jsp',url_tager[4])[0]
        url_key.append(employee)
        url_key.append(salesFactSample)
        for key in url_key:
            yield scrapy.FormRequest('http://localhost:8080/resale/list'+key.title()+'.do',
                                     formdata={'page':'1'},callback=self.parse_is_detail,meta={'key':key})

    def parse_is_detail(self, response):
        request=json.loads(response.text)
        key = response.meta["key"]
        total_pagenum=request["totalPageNum"]
        if key=="salesFactSample":
            for page in range(0,int(total_pagenum)+1):
                yield scrapy.FormRequest('http://localhost:8080/resale/listSalesfactsample.do',
                                         formdata={'page':str(page)},callback=self.parse)
        else:
            yield scrapy.FormRequest('http://localhost:8080/resale/list'+key.title()+'.do',
                                     formdata={'page':str(total_pagenum)},callback=self.parse_total_id,
                                     meta={'key':key,'total_pagenum':str(total_pagenum)})

    def parse_total_id(self, response):
        request=json.loads((response.text))
        key=response.meta["key"]
        total_pagenum=response.meta["total_pagenum"]
        delis=request[key+'s']
        zui_id=len(delis)
        quanbu_id=((total_pagenum-1)*15+int(zui_id))
        for id in range(0,int(quanbu_id)+1):
            yield scrapy.FormRequest('http://localhost:8080/resale/get' + key.title() + 'Info.do',
                                     formdata={'id':str(id)},callback=self.parse_others,meta={'key':key})
    def parse_others(self, response):
        item=ShengsailianxiItem()
        request=json.loads(response.text)
        key=response.meta['key']
        if key =='employee':
            item["detail_data_e"]=request
            yield item



    def _parse(self,response):
        item=ShengsailianxiItem()
        request=json.loads(response.text)
        sames=request["no_datail_data"]
        for same in sames:
            item["no_datail_data"]=same
            yield item


