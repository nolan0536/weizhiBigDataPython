# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhaopinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    zhiwei=scrapy.Field()
    yuexin=scrapy.Field()
    gongsi=scrapy.Field()
    pass
