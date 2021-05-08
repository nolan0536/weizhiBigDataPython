# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ErshoufangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    xiaoquming=scrapy.Field()
    shoujia=scrapy.Field()
    danjia=scrapy.Field()
    mianji=scrapy.Field()
    xiangxi=scrapy.Field()
    fangyuantese=scrapy.Field()
