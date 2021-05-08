# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GuosaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #result=scrapy.Field()
    diqu=scrapy.Field()
    city=scrapy.Field()
    country=scrapy.Field()
    department=scrapy.Field()
    hotel_name=scrapy.Field()
    price=scrapy.Field()
    pass
