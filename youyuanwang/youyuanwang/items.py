# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YouyuanwangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    wangming=scrapy.Field()
    jibenxinxi=scrapy.Field()
    neixindubai=scrapy.Field()
    jiguan=scrapy.Field()
    tizhong=scrapy.Field()
    xueli=scrapy.Field()
    yuexin=scrapy.Field()
    pass
