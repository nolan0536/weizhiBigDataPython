# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class QuanguozhaopinPipeline(object):
    def __init__(self):
        self.links=open("招聘.json","w",encoding="utf-8")
    def process_item(self, item, spider):
        print(44444444444444444444444444)
        print(item)
        item['dizhi']=str(item['dizhi']).replace('\\t','').replace('\\r\\n','').replace(' ','')
        limk=json.dumps(dict(item),ensure_ascii=False)+",\n"
        self.links.write(limk)
        return item
