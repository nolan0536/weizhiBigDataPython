import scrapy

#创建爬虫类 并继承自scrapy.Spider 最基础的类

class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili' #爬虫名字 #必须唯一
    allowed_domains = ['xicidaili.com']  #允许采集的域名
    #start_urls = [f'http://xicidaili.com//nn/{page}' for page in range(1,3685)] #开始采集的网站
    start_urls = ['http://xicidaili.com']
    #解析响应数据 提取数据 或者网址等   #response就是网页源码

    def start_requests(self):
        reqs=[]

        for i in range(1,3685):
            req = scrapy.Request("http://xicidaili.com/nn/%s"%i)
            reqs.append(req)
        return reqs


        ip_list =response.xpath('//table[@id="ip_list"]')
        trs = ip_list[0].xpath("tr")
        items=[]
        for ip in trs[1:]:
            pre_item = CollectipsItem()
            pre_item["ip"] = ip.xpath('td[3]/text()')[0].extract()
            pre_item["port"] = ip.xpath('td[4]/text()')[0].extract()
            pre_item["position"] = ip.xpath('string(td[5])')[0].extract().strip()
            pre_item["type"] = ip.xpath('td[7]/text()')[0].extract()
            items.append(pre_item)
 # def parse(self, response):
    #     #提取数据         #双斜杠表示选择任意一个节点 #text（）文本内容
    #     response.xpath('//title/text()').extract()  #extract 提取
    #     selectors = response.xpath('//tr') #选择所有的tr标签
    #     for selector in selectors:
    #         ip = selector.xpath('./td[2]/text()').get()  #get获取一个 get aLL为获取多个
    #         port = selector.xpath('./tf[3]/text()').get()
    #         print(ip, port)
    #     #翻页操作
    #     next_page = response.xpath('//a[@class="next_page"]/@hred').get() #使用Xpath 提取网页的下一页
    #     if next_page:
    #         print(next_page)
    #         #拼接网址
    #         #next_url = 'https://www.xicidaili.com'+next_page
    #         next_url = response.urljoin(next_page)  #绝对路径
    #         #发出请求Request   callback 是回调函数 就是将请求得到的响应交给自己处理
    #         yield scrapy.Request(next_url,callback=self.parse())  #生成器
    #                     Request()发出请求 类似requests.get()
    #                     callback 是将发出去的请求得到的响应交给自己处理
    #         回调函数不用写（）只写函数名字