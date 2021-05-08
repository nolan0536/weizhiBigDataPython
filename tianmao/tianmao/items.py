# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TianmaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field() #标题
    jiage = scrapy.Field() #价格
    yuexiao =scrapy.Field() #月销
    pingjia = scrapy.Field() #评价数
    dianpuurl = scrapy.Field() #店铺url
    dianming = scrapy.Field() #店名
    changzhi = scrapy.Field() #厂址
    cjdh = scrapy.Field() #厂家电话

    pass
