# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
class IthomePipeline(object):
    def __init__(self):
        print(111)
        self.conn=pymysql.connect(host='localhost',user='root',password='root',port=3306,charset='utf8',db='data')
        self.cursour=self.conn.cursor()
    def proocess_item(self,item,spider):
        print(1111111111111111111111111111)
        sql="insert into ithome value('{0}','{1}','{2}','{3}')".format(item["title"],item["time"],item["zuozhe"],item["zebian"])
        print(sql)
        self.cursour.execute(sql)
        self.conn.commit()
        return item
    def process_close(self,spider):
        self.cursour.close()
        self.conn.close()