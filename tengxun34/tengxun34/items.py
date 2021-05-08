# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Tengxun34Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    CategoryName=scrapy.Field()
    guojia=scrapy.Field()
    diqu=scrapy.Field()
    time=scrapy.Field()
    gangwei=scrapy.Field()
    postid=scrapy.Field()