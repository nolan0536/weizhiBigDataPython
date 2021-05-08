# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class AnjukePipeline(object):
    def __init__(self):
        self.links=open('安居客.json','w',encoding="utf-8")
    def process_item(self, item, spider):
        print(111111111111111111)
        print(item)
        item['title']=str(item['title']).replace(' ','').replace('\n','')
        item['jiage']=str(item['jiage'])+'w'
        link=json.dumps(dict(item),ensure_ascii=False)+",\n"
        self.links.write(link)
        return item
