# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TianqiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    day = scrapy.Field()
    tianqi = scrapy.Field()
    max = scrapy.Field()
    min = scrapy.Field()
    fengli = scrapy.Field()
