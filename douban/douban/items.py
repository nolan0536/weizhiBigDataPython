# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titlecn=scrapy.Field()
    titleen=scrapy.Field()
    dyxx=scrapy.Field()
    pingfen=scrapy.Field()
    pingjiashu=scrapy.Field()
    jianshu=scrapy.Field()

