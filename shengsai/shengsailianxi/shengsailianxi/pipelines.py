# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class ShengsailianxiPipeline:
    # def __init__(self):
    #     self.json_e=open("employee.json","w",encoding="utf-8")
    #     self.json_s=open("sale_fact.json","w",encoding="utf-8")
    # def
    #     for key in item.keys():
    #         if key == "detail_data_e":
    #             leson_e=json.dumps(dict(item)["detail_data_e"],ensure_ascii=False)+",\n"
    #             self.json_e.write(leson_e)
    #         if key =="no_detail_data":
    #             leson_s=json.dumps(dict(item)["no_detail_data"],ensure_ascii=False)+",\n"
    #             self.json_s.write(leson_s)
    #     return item

    def __init__(self):
        self.json_e=open("yuangongxinxi.json","w",encoding="utf-8")
        self.json_s=open("shangpinxiaoshou.json","w",encoding="utf-8")
    def process_item(self, item, spider):
        for key in item.keys():
            if key=="detail_data_e":
                leson_e=json.dumps(dict(item)["detail_data_e"],ensure_ascii=False)+",\n"
                self.json_e.write(leson_e)
            if key=="no_detail_data":
                leson_s=json.dumps(dict(item)["no_detail_data"],ensure_ascii=False)+",\n"
                self.json_s.write(leson_s)
        return item
