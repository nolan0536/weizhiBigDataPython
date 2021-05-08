# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiechenghuocheItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    chehao=scrapy.Field()
    chufazhan=scrapy.Field()
    chufashijian=scrapy.Field()
    daodashijian=scrapy.Field()
    zhongdianzhan=scrapy.Field()
    shijian=scrapy.Field()
    jiage=scrapy.Field()

