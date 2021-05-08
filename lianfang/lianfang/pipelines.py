# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class LianfangPipeline(object):
    def __init__(self):
        self.links=open("二手房.json","w",encoding="utf-8")
    def process_item(self, item, spider):
        print(1111111111111)
        print(item)
        item["jiage"]=item["jiage"]+"w"
        item["danjia"]=str(item["danjia"])[2:]
        link=json.dumps(dict(item),ensure_ascii=False)+",\n"
        self.links.write(link)
        return item
