# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import pymysql

class GuosailianxiPipeline:
    def __init__(self):
        self.conn=pymysql.connect(host="localhost",user="root",password="root",port=3306,charset="utf8",db="data")
        self.corsor=self.conn.cursor()
    def process_item(self,item,spider):
        print(1111111111111111111111)
        sql="insert into guosai value('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(item["id"],
        item["seq"],item["name"],item["guojia"],item["shengfen"],item["chengshi"],item["jiage"])
        print(sql)
        self.corsor.execute(sql)
        self.conn.commit()
        return item
    def closs_spider(self,spider):
        self.corsor.close()
        self.conn.close()