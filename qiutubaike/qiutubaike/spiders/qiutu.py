import scrapy
from qiutubaike.items import QiutubaikeItem

class QiutuSpider(scrapy.Spider):
    name = 'qiutu'
    allowed_domains = ['https://qiushibaike.com']
    start_urls = ['http://qiushibaike.com//imgrank/']

    def parse(self, response):
        img_list = response.xpath("//img")
        with open("1.txt","w+",encoding="utf-8") as f:  #w+读写
            for img in img_list:
                src = img.xpath("@src")
                content = src.extract() #提取
                if content:
                    f.write(str(content[0]+"\n")) #utf-8能防止产生乱码
            f.close()
