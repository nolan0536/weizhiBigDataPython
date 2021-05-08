# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class BokeyuanPipeline:
    def open_spider(self,spider):
        self.links=open("博客网.json","w",encoding="utf-8")
    def process_item(self, item, spider):
        print(444444444444444444444444444444444444)
        link=json.dumps(dict(item),ensure_ascii=False)+",\n"
        self.links.write(link)
        
        return item
    def close_spider(self,spider):
        self.links.close()
