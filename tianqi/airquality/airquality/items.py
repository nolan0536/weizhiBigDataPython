# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AirqualityItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    yuefen = scrapy.Field()
    AQL = scrapy.Field()
    zldj = scrapy.Field()
    pm25 = scrapy.Field()
    pm10 = scrapy.Field()
    so2 = scrapy.Field()
    co = scrapy.Field()
    no2 = scrapy.Field()
    o3 = scrapy.Field()

    pass
