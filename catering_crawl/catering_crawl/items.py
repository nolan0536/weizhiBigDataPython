# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CateringCrawlItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    """
    映射需要提取的scrapy字段，定义对应的item
    """
    date = scrapy.Field()
    rs_name = scrapy.Field()
    food_type = scrapy.Field()
    url = scrapy.Field()
    feature_food = scrapy.Field()
    comment = scrapy.Field()
    sale_cumulative = scrapy.Field()
    score = scrapy.Field()
    sale = scrapy.Field()
    sale_vol = scrapy.Field()
    city = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
    pass
