# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class Shengsai1207Pipeline(object):
    def __init__(self):
        self.A=open("employee.json","w",encoding="utf-8")
        self.B=open("salesfactsamples.json","w",encoding="utf-8")
    def process_item(self, item, spider):
        for key in item.keys():
            if key=="employee":
                links=json.dumps(dict(item)["employee"],ensure_ascii=False)+",\n"
                self.A.write(links)
            else:
                link=json.dumps(dict(item)["salasfactsample"],ensure_ascii=False)+",\n"
                self.B.write(link)
        return item
