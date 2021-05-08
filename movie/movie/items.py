# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movietitle=scrapy.Field()
    movieid=scrapy.Field()
    zonghe=scrapy.Field()
    daoyan=scrapy.Field()
    huamian=scrapy.Field()
    gushi=scrapy.Field()
    yinyue=scrapy.Field()
    canyurenshu=scrapy.Field()
    xiangkan=scrapy.Field()

