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
        # 使用正则表达式获取employee和saleFactSamples两个字符串，构建分页表单（页数：1）和对应的url
        # 发起post请求，将两个字符串通过参数的方式传递到下一个函数
        url_key = []
        url_target = response.xpath("//ul[@class='nav navbar-nav']//@href").extract()
        employee = re.findall('webpage/(.*?).jsp', url_target[1])[0]    #提取员工信息
        sales_fact_sample = re.findall('webpage/(.*?).jsp', url_target[4])[0]   #提取商品零售记录
        url_key.append(employee)
        url_key.append(sales_fact_sample)
        for key in url_key:              #拼接成一个新的url
            yield scrapy.FormRequest('http://localhost:8080/resale/list' + key.title() + '.do',
                                     formdata={'page': '1'}, callback=self.parse_is_detail, meta={'key': key})#初始化key属性
    # def parse_table_url(self, response):
    #     url_tagel = response.xpath("//ul[@class='nav navbar-nav']//@href").extract()
    #     url_key=[]
    #     employee=re.findall('webpage/(.*?).jsp',url_tagel[1])[0]
    #     salesFactSample=re.findall('webpage/(.*?).jsp',url_tagel[4])[0]
    #     url_key.append(employee)
    #     url_key.append(salesFactSample)
    #     for key in url_key:
    #         yield scrapy.FormRequest('http://localhost:8080/resale/list' + key.title() + '.do',
    #                                  fromdata={'page':'1'},meta={"key":key},callback=self.parse_is_detail)

    def parse_is_detail(self, response):
        result = json.loads(response.text)
        key = response.meta["key"]
        total_page = result["totalPageNum"]
        if key=='salesFactSample':
            for page in range(0,int(total_page)+1):
                yield scrapy.FormRequest('http://localhost:8080/resale/listSalesfactsample.do',
                                         formdata={"page":str(page)},callback=self.parse)
        else:
            yield scrapy.FormRequest('http://localhost:8080/resale/list' + key.title() + '.do',
                                     formdata={"page":str(total_page)},callback=self.parse_total_id,
                                     meta={"key":key,"total_page":str(total_page)})
    #
    def parse_total_id(self, response):
        result =json.loads(response.text)
        key = response.meta["key"]
        total_page = response.meta["total_page"]
        delis = result[key+"s"]
        zui_id=len(delis)
        total_id_numb = ((int(total_page)-1)*15)+(int(zui_id))
        for id_tagel in range(0,int(total_id_numb)+1):
            yield scrapy.FormRequest('http://localhost:8080/resale/get' + key.title() + 'Info.do',
                                     formdata={"id":str(id_tagel)},callback=self.parse_others,meta={"key":key})
    #
    def parse_others(self, response):
        item = ShengsailianxiItem()
        result=json.loads(response.text)
        key = response.meta["key"]
        if key=='employee':
            item["detail_data_e"]=result
            yield item
    def parse(self, response):
        item = ShengsailianxiItem()
        result = json.loads(response.text)
        sames = result["salesFactSamples"]
        for same in sames:
            item["no_detail_data"]=same
            yield item



    # def parse_is_detail(self, response):
    #     # 获取返回的response对象，获取参数值和总分页数
    #     # 判断是否有详情页，如果没有（saleFactSample），循环遍历构建每一页的表单和相应的url   发起post请求
    #     # 如果有详情页（employee）构建最后一页表单和相应的url  发起post请求
    #     result = json.loads(response.text) #返回网页的文本数据并转换为python对象
    #     key = response.meta['key']  #把属性传递给key
    #     total_pages = result['totalPageNum']  # 获取所有表的总页数
    #     if key == 'salesFactSample':
    #         for page in range(0, int(total_pages) + 1): #int（）转化为整数
    #             yield scrapy.FormRequest('http://localhost:8080/resale/listSalesfactsample.do',#http://localhost:8080/resale/webpage/salesFactSample.jsp
    #                                      formdata={'page': str(page)}, callback=self.parse)
    #     else: #构建最后一页表单和相应的url
    #         yield scrapy.FormRequest('http://localhost:8080/resale/list' + key.title() + '.do',
    #                                  formdata={'page': str(total_pages)}, callback=self.parse_total_id,
    #                                  meta={'total_pages': str(total_pages), 'key': key})

    # def parse_total_id(self, response):
    #     #对详情页进行解析
    #     # 获取返回的response对象，获取参数key值和总分页数
    #     # 获取最后一页的id数，统计出总id数，然后循环遍历构建id的表单和相应的url
    #     # 发起post请求
    #     result = json.loads(response.text)   #返回网页的文本数据并转换为python对象
    #     # print(result)  在最后一页里{'employees': [{'employee_id': 1142开头 我们需要的是employees的信息 所以key是employee需要加s
    #     total_pages = response.meta['total_pages'] #最后一页
    #     key = response.meta['key'] #employee
    #     detail = result[key + 's']   #最后一页id数  #employees
    #     # print(detail)
    #     last_page_id_numb = len(detail)  # 获取最后一页的id数
    #     total_id_numb = ((int(total_pages) - 1) * 15) + int(last_page_id_numb)  # 通过计算  求出该表的总id数
    #     for id_target in range(0, int(total_id_numb) + 1):      # 循环请求该表的每一个id的详情页
    #         yield scrapy.FormRequest('http://localhost:8080/resale/get' + key.title() + 'Info.do',
    #                                  formdata={'id': str(id_target)}, callback=self.parse_others, meta={'key': key})
        #请求员工信息表中的所有详情页并传递给回调函数
    # def parse_others(self, response):
    #     # 获取返回的response对象，获取参数key值
    #     # 将employee的结果映射到item对象中
    #     detail_data = json.loads(response.text) #把上一层的所有员工详细信息转化成python对象
    #     key = response.meta['key']
    #     item = ShengsailianxiItem()
    #     if key == 'employee':
    #         item['detail_data_e'] = detail_data  #返回所有id的详情页
    #         yield item
    #
    # def parse(self, response):
    #     # 获取返回的response对象，获取参数key值
    #     # 将salesFactSamples的结果映射到item对象中
    #     item = ShengsailianxiItem()
    #     result = json.loads(response.text)
    #     sales_fact_samples = result['salesFactSamples']  # list  #所有信息
    #     for sample in sales_fact_samples:
    #         item['no_detail_data'] = sample
    #         yield item

    def parse_table_url(self, response):
        url_tagel=response.xpath('//ul[@class="nav navbar-nav"]//@href').extract()
        url_key=[]
        employee=re.findall('webpage/(.*?).jsp',url_tagel[1])[0]
        salesFactSample=re.findall('webpage/(.*?).jsp',url_tagel[4])[0]
        url_key.append(employee)
        url_key.append(salesFactSample)
        for key in url_key:
            yield scrapy.FormRequest('http://localhost:8080/resale/list'+key.title()+'.do',
                                     formdata={'page':'1'},meta={'key':key},callback=self.parse_is_detail)
    def parse_is_detail(self, response):
        request=json.loads(response.text)
        key=response.meta["key"]
        totalpagenum=request["totalPageNum"]
        if key=="salesFactSample":
            for page in range(0,int(totalpagenum+1)):
                yield scrapy.FormRequest('http://localhost:8080/resale/listSalesfactsample.do',
                                         formdata={'page':str(page)},callback=self.parse)
        else:
            yield scrapy.FormRequest('http://localhost:8080/resale/list'+key.title()+'.do',
                                     formdata={'page':str(totalpagenum)},callback=self.parse_total_id(),
                                     meta={'totalpagenum':str(totalpagenum),'key':key})


    def parse_total_id(self, response):
        request=json.loads(response.text)
        key=response.meta["key"]
        totalpagenum=response.meta["totalpagenum"]
        delis=request[key+'s']#查找最后一页id有哪些
        zuihou_id=len(delis) #最后一页id数列
        quanbu_id=(totalpagenum-1)*15+zuihou_id
        for id in range(0,int(quanbu_id+1)):
            yield scrapy.FormRequest('http://localhost:8080/resale/get' + key.title() + 'Info.do',
                                     formdata={'id':str(id)},meta={'key':key},callback=self.parse_others)

    def parse_others(self, response):
        item=ShengsailianxiItem()
        resule=json.loads(response.text)
        key=response.meta['key']
        if key=='employee':
            item["detail_data_e"]=resule
            yield item
    def parse(self, response):
        item=ShengsailianxiItem()
        result=json.loads(response.text)
        sames=result["salesFactSample"]
        for same in sames:
            item["no_detail_data_e"]=same
            yield item
