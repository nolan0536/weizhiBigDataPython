# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DongfangcaifuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id=scrapy.Field()
    jiancheng=scrapy.Field()
    shoupanjia=scrapy.Field()
    zhangdiefu=scrapy.Field()
    zijin=scrapy.Field()
    shizhibi=scrapy.Field()

    pass
