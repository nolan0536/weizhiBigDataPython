# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JintougupiaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    chexing=scrapy.Field()
    nianfen=scrapy.Field()
    jiage=scrapy.Field()
    xinche=scrapy.Field()

