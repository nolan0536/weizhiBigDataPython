# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangtushuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    shiyongxing=scrapy.Field()
    jiage=scrapy.Field()
    zuozhe=scrapy.Field()
