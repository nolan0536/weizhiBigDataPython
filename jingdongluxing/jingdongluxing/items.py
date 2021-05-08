# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JingdongluxingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jiudianming=scrapy.Field()
    xingji=scrapy.Field()
    dizhi=scrapy.Field()
    jiage=scrapy.Field()

    pass
