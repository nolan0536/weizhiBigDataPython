# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShengsaiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    no_detail_data_e=scrapy.Field()
    detail_data_e=scrapy.Field()

    pass
