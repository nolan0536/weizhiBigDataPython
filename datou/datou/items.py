# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DatouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tupianming=scrapy.Field()
    tupianurl=scrapy.Field()
    width=scrapy.Field()
    height=scrapy.Field()
    type=scrapy.Field()
    
    pass
