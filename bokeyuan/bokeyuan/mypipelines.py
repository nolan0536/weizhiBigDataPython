# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class BokeyuanPipeline(object):
    def __init__(self):
        self.conn=pymysql.connect(host="localhost",password="root",user="root",port=3306,db="lianxi",charset="utf8")
        self.cursor=self.conn.cursor()
    def process_item(self, item, spider):
        print(555555555555555555555555555)
        sql="insert into bokeyuan value('{0}','{1}','{2}','{3}')".format(item["url"],item["zuozhe"],item["time"],item["title"])
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()
    def process_colose(self,spider):
        
        self.cursor.close()
        self.conn.close()