# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class DianyingPipeline(object):
    def __init__(self):
        self.lino=open("电影排行top50.json",'w',encoding="utf8")
    def process_item(self, item, spider):
        jeson=json.dumps(dict(item),ensure_ascii=False)+",\n"
        self.lino.write(jeson)
        return item
