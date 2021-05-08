# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BiqugeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    zuozhe=scrapy.Field()
    zhangjieming=scrapy.Field()
    neirong=scrapy.Field()
    pass
