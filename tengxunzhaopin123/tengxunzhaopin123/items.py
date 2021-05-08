# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Tengxunzhaopin123Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    dizhi=scrapy.Field()
    leixing=scrapy.Field()
    shijian=scrapy.Field()
    url=scrapy.Field()
    yaoqiu=scrapy.Field()
    zhize=scrapy.Field()
    pass
