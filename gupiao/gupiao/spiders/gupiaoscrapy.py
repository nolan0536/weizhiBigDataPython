import scrapy
import pymysql
from scrapy import Selector

class GupiaoscrapySpider(scrapy.Spider):
    name = 'gupiaoscrapy'
    allowed_domains = ['s.askci.com']
    start_urls = ['https://s.askci.com/stock/a/0-0?reportTime=2019-12-31&pageNum=1#QueryCondition']

    def parse(self, response):
        db=pymysql.connect(host='localhost', user='root', password='root', port=3306, db='tianqi',charset='utf8')#连接数据库
        curosr=db.cursor() #创建游标
        items = response.xpath("//tbody//tr").getall() #查找需要的内容
        for item in items:
            value1=Selector(text=item).xpath('//td[1]//text()').extract()

            value2=Selector(text=item).xpath('//td[2]/a//text()').extract()

            value3=Selector(text=item).xpath('//td[3]/a//text()').extract()

            value4=Selector(text=item).xpath('//td[4]//text()').extract()
            value5=Selector(text=item).xpath('//td[5]//text()').extract()
            value6=Selector(text=item).xpath('//td[6]//text()').extract()
            value7=Selector(text=item).xpath('//td[7]//text()').extract()
            value8=Selector(text=item).xpath('//td[8]//text()').extract()
            value9=Selector(text=item).xpath('//td[9]//text()').extract()
            # #sql语句
            sql = "insert into gupiao value({0}+0,{1}+0,'{2}','{3}','{4}','{5}','{6}','{7}',{8}+0)"\
                .format(value1[0],value2[0],value3[0],value4[0],value5[0],value6[0],value7[0],value8[0],value9[0])
            print(sql)
             #执行sql语句
            curosr.execute(sql)             #str_to_date函数是将时间格式的字符串（str），按照所提供的显示格式转化为DATETIME类型
            db.commit() #提交事务
        curosr.close()
        db.close()
        pass

