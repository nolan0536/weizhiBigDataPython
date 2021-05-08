# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class ResaleCrawlPipeline(object):
    def __init__(self):
        # 初始化json  文件，设置编码格式为urf-8
        self.file_no = open('sale_fact.json', 'w', encoding='utf-8')
        self.file_e = open('employee.json', 'w', encoding='utf-8')


    def process_item(self, item, spider):
        # 循环遍历所有的item，然后进行判断，如果key值为no_detail_data的，就将item数据写入sale_fact.json文件
        # 如果key值为detail_data_e的，就将item数据写入employee.json文件
        for key in item.keys():
            if key == 'no_detail_data': #把
                line_no = json.dumps(dict(item)['no_detail_data'], ensure_ascii=False) + ",\n"
                self.file_no.write(line_no)
            if key == 'detail_data_e':
                line_e = json.dumps(dict(item)['detail_data_e'], ensure_ascii=False) + ",\n"
                self.file_e.write(line_e)
            return item
