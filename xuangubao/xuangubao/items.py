# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XuangubaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    symbol=scrapy.Field()
    change_percent=scrapy.Field()
    stock_chi_name=scrapy.Field()
    price_change=scrapy.Field()
    pass
