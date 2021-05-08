# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql
class ErshoufangPipeline(object):
    def __init__(self):
        self.conn=pymysql.connect(host="localhost",user="root",password="root",port=3306,db="lianxi",charset="utf8")
        self.cursor=self.conn.cursor()
    def process_item(self, item, spider):
        print(6666666666666666666666666666666666666666)
        item["title"]=item["title"].replace("\u3000",",")
        print(item["title"])
        item["fangyuantese"]=item["fangyuantese"].replace(" ","").replace("\n","").replace("'","")
        item["xiangxi"]=item["xiangxi"].replace(" ","").replace("\n","").replace("'","")
        sql="insert into lianfang value('{0}','{1}','{2}','{3}','{4}')".format(item["title"],item["xiaoquming"],item["shoujia"],item["danjia"],item["mianji"])
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()
    def process_close(self,spider):
        self.cursor.close()
        self.conn.close()