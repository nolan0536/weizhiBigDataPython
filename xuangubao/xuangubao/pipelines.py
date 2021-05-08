# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class XuangubaoPipeline(object):
    def __init__(self):
        self.lins=open("股票.json","w",encoding="utf-8")
    def process_item(self, item, spider):
        link=json.dumps(dict(item),ensure_ascii=False)+",\n"
        self.lins.write(link)
        return item
