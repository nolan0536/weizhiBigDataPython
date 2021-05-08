# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class XiaoshuoPipeline(object):
    def __init__(self):
        self.lino=open('伏天氏.json','w',encoding='utf-8')
    def process_item(self, item, spider):
        item["zhengwen"]=str(item["zhengwen"]).replace('&nbsp','')
        item["zhengwen"]=str(item["zhengwen"]).replace('<br>','')
        link=json.dumps(dict(item),ensure_ascii=False)+",\n"
        self.lino.write(link)
        return item
