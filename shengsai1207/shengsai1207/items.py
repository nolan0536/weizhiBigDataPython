# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Shengsai1207Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    employee=scrapy.Field()
    salasfactsample=scrapy.Field()
    pass
