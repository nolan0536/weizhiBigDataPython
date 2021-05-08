# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyiyunItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    geming=scrapy.Field()
    geshou=scrapy.Field()
    zhuanji=scrapy.Field()
    id=scrapy.Field()
    picurl=scrapy.Field()
    picstr=scrapy.Field()

