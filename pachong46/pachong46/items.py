# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Pachong46Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    dizhi=scrapy.Field()
    chengshi=scrapy.Field()
    leixing=scrapy.Field()
    jishu=scrapy.Field()
    shijian=scrapy.Field()
    id=scrapy.Field()
