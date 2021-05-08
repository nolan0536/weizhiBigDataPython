import scrapy
from scrapy.selector import Selector
import pymysql

class ShujukuspiderSpider(scrapy.Spider):
    name = 'shujukuspider'
    allowed_domains = ['docs.microsoft.com']
    start_urls = ['https://docs.microsoft.com/zh-cn/sql/mdx/mdx-function-reference-mdx?view=sql-server-2017']

    def parse(self, response):
        db=pymysql.connect(host='localhost', user='root', password='root', port=3306, db='tianqi',charset='utf8')
        curosr=db.cursor()
        items = response.xpath("//tbody//tr").getall()
        for item in items:
            value=Selector(text=item).xpath("//td[1]/a/span[1]//text()").extract()
            value1=Selector(text=item).xpath("//td[2]/span[1]//text()").extract()
            print(value1)
            print("!!!!!!")
            sql = "insert into fun_test value('{0}','{1}')".format(value[0],value1[0])
            print(sql)
            curosr.execute(sql)            #str_to_date函数是将时间格式的字符串（str），按照所提供的显示格式转化为DATETIME类型
            db.commit()
        curosr.close()
        db.close()
        pass

