# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TodaymovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titlecn=scrapy.Field()
    titleen=scrapy.Field()
    director=scrapy.Field()#导演
    runtime=scrapy.Field()#电影时长
    zhuyan=scrapy.Field()
    juqing=scrapy.Field()
    pass
