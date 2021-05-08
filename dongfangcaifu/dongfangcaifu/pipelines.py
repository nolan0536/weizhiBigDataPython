# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class DongfangcaifuPipeline(object):
    def __init__(self):
        self.db=pymysql.connect(host="localhost",user="root",password="root",port=3306,db="tianqi",charset="utf8")
        self.cursor=self.db.cursor()
    def process_item(self, item, spider):
        print(11111111111111111111)
        print(item)
        sql="insort into rongzi value('{0}','{1}','{2}','{3}','{4}','{5}')".format(item['id'],
            item['jiancheng'],item['shoupanjia'],item['zhangdiefu'],item['zijin'],item['shizhibi'])
        self.cursor.execute(sql)
        self.db.commit()
        return item
    def parse(self,spider):
        self.cursor.close()
        self.db.close()