import scrapy
from chuanzhiSpider.items import ChuanzhispiderItem

class ChuanzhiSpider(scrapy.Spider):
    name = 'chuanzhi'
    allowed_domains = ['www.itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#aandroid']

    def parse(self, response):
        teacher_list = response.xpath('//div[@class="li_txt"]')

        for each in teacher_list:
            item = ChuanzhispiderItem()

            name = each.xpath('./h3/text()').extract() #提取里面的内容
            title = each.xpath('./h4/text()').extract()
            info = each.xpath('./p/text()').extractt

            item["name"]=name[0]
            item["title"] = title[0]
            item["info"] = info[0]

            yield item
