# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nick_name = scrapy.Field()
    image_link = scrapy.Field()
    image_path = scrapy.Field()
    pass
