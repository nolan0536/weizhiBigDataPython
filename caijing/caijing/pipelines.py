# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class CaijingPipeline:
    def __init__(self):
        self.conner=pymysql.connect(host="localhost",port=3306,user="root",password="root",charset="utf8",db="bisai")
        self.cousor=self.conner.cursor()
    def process_item(self, item, spider):
        print(555555555555555555555555)
        sql="insert into xinwen1 values('{0}','{1}')".format(item["title"],item["div"])
        print(sql)
        self.cousor.execute(sql)
        self.conner.commit()
        return item
    def stop_spider(self,spider):
        self.cousor.close()
        self.conner.close()