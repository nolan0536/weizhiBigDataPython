# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import redis

class BilibiliPipeline:
    def __init__(self):
        self.link=open("bilibili.json","w",encoding="utf-8")
        self.R=redis.Redis(host="127.0.0.1",port=6379,db=0)
    def process_item(self, item, spider):
        print(3333333333333333333333333333)
        links=json.dumps(dict(item),ensure_ascii=False)+",\n"
        self.R.lpush("Bilibilijson",links)
        self.link.write(links)
        return item
