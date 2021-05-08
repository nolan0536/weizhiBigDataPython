# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json
class JobbolePipeline:
    def __init__(self):
        self.links=open("伯乐在线.json","w",encoding="utf-8")
    def process_item(self, item, spider):
        print(555555555555555555555)
        link=json.dumps(dict(item),ensure_ascii=False)+",\n"
        self.links.write(link)
        return item
