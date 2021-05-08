# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field() #书名
    price = scrapy.Field() #价格
    author = scrapy.Field() #作者
    pingjia = scrapy.Field() #评价数
    press = scrapy.Field() #出版社
    time = scrapy.Field() #出版时间
    jianjie=scrapy.Field()
    pass
