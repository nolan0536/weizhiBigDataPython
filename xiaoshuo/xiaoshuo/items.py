# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaoshuoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    zhangming=scrapy.Field()
    zhengwen=scrapy.Field()
    fanye=scrapy.Field()