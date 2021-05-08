# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class BizhanPipeline:
    def __init__(self):
        self.link=open("bilibili.json","w",encoding="utf-8")
    def process_item(self, item, spider):
        links=json.dumps(dict(item),ensure_ascii=False)+",\n"
        self.link.write(links)
        print(links)
        return item
