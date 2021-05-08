# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnjukeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    mianji=scrapy.Field()
    xiaoqu=scrapy.Field()
    jushi=scrapy.Field()
    jiage=scrapy.Field()
    danjia=scrapy.Field()

    pass
