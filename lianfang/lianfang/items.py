# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LianfangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    xinxi=scrapy.Field()
    jiage=scrapy.Field()
    danjia=scrapy.Field()
    dizhi=scrapy.Field()