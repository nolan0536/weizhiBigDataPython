# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class ZufangPipeline(object):
    def __init__(self):
        self.link=open('济南出租房.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        item['title']=str(item['title']).replace('\\n','').replace(' ','')
        item['leixing']=str(item['leixing']).replace('\xa0','').replace(' ','').replace(',','')
        item['leixing']=str(item['leixing']).replace('\\xa0','').replace('\\n','')
        links=json.dumps(dict(item),ensure_ascii=False)+"'\n"
        self.link.write(links)
        return item
