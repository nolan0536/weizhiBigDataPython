# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DianyingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    top=scrapy.Field()
    title=scrapy.Field()
    zhuyan=scrapy.Field()
    bofangcishu=scrapy.Field()

    pass
