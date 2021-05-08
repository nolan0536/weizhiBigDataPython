# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XiaoshuopaihangItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field() #标题
    zuozhe = scrapy.Field() #作者
    leixing = scrapy.Field() #类型
    zhangjie = scrapy.Field() #章节
    time = scrapy.Field() #时间
    pass
