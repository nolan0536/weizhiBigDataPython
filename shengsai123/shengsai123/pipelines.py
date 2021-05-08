# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class Shengsai123Pipeline(object):
    def __init__(self):
        self.links1=open("employee.json","w",encoding="utf-8")
        self.links2=open("salesFactSampless","w",encoding="utf-8")
    def process_item(self, item, spider):
        for key in item.keys():
            if key=="employee":
                print(88888888888888888888)
                link1=json.dumps(dict(item),ensure_ascii=False)+",\n"
                self.links1.write(link1)
            else:
                link2=json.dumps(dict(item),ensure_ascii=False)+",\n"
                self.links2.write(link2)
        return item


