# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GuosailianxiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id=scrapy.Field()
    seq=scrapy.Field()
    name=scrapy.Field()
    guojia=scrapy.Field()
    chengshi=scrapy.Field()
    shengfen=scrapy.Field()
    jiage=scrapy.Field()
    pass
