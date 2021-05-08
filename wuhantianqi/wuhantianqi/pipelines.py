# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class WuhantianqiPipeline(object):

    def __init__(self):
        self.db=pymysql.connect(host="localhost",user="root",password="root",port=3306,db="tianqi",charset="utf8")
        self.cursor=self.db.cursor()

    def process_item(self, item, spider):
        print(1111111111111111111111)
        print(item)
        sql="insert into wuhan value('{0}','{1}','{2}','{3}','{4}')".format(item['citydata'],item['week'],item['temperaturn'],item['weather'],item['wind'])
        self.cursor.execute(sql)
        self.db.commit()
        return item
    
    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()
