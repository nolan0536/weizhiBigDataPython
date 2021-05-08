# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TubatuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mingcheng=scrapy.Field()
    id=scrapy.Field()
    url=scrapy.Field()
    nick_name=scrapy.Field()
    pic_url=scrapy.Field()
    pic_name=scrapy.Field()
    pass
