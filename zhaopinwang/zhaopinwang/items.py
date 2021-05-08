# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhaopinwangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    zhiwei=scrapy.Field()
    gongsi=scrapy.Field()
    dizhi=scrapy.Field()
    gongzi=scrapy.Field()



