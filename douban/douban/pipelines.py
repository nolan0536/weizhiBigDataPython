# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import json
class DoubanPipeline(object):
    def __init__(self):
        self.lino=open('豆瓣top250.json','w',encoding="utf-8")
    def process_item(self, item, spider):
        item['titleen']=str(item['titleen']).replace('\\xa0','')
        item['titleen']=str(item['titleen']).replace('/','')
        item['dyxx']=str(item['dyxx']).replace('\n','')
        item['dyxx']=str(item['dyxx']).replace(' ','')
        item['dyxx']=str(item['dyxx']).replace('xa0','')
        links=json.dumps(dict(item),ensure_ascii=False)+",\n"
        self.lino.write(links)
        print('上传成功')
        return item
