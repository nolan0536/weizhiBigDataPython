# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class AirqualityPipeline(object):
    def __init__(self):
        self.conn=pymysql.connect(host='localhost',user='root',password='root',port=3306,db='tianqi',charset='utf8')
        self.cursor=self.conn.cursor()
    def process_item(self, item, spider):
        if (len(item)==9):
            values=item
                # sql语句
            insert_sql = "insert into wether value(str_to_date('{0}','%Y-%m-%D'),{1}+0,'{2}',{3}+0,{4}+0,{5}+0,{6}+0,{7}+0,{8}+0)"\
                .format(values["yuefen"],values["AQL"],values["zldj"],values["pm25"],values["pm10"],values["so2"],values["co"],values["no2"],values["o3"][:-2])
        self.cursor.execute(insert_sql)
        self.conn.commit()

        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()