# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json
class MoviePipeline(object):
    def __init__(self):
        self.link=open("电影信息.json","w",encoding="utf-8")
    def process_item(self, item, spider):
        print(1111111111111111111)
        print('爬取的数据为：')
        print(item)
        links=json.dumps(dict(item),ensure_ascii=False)+",\n"
        self.link.write(links)
        return item
