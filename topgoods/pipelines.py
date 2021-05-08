# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class TopgoodsPipeline(object):
    def process_item(self, item, spider):
        db=pymysql.connect(host='localhost',user='root',password='root',db='tianqi',charest='utf8')
        cursor=db.cursor()
        GOODS_PRICE = item["GOODS_PRICE"]
        GOODS_NAME = item["GOODS_NAME"]
        GOODS_URL = item["GOODS_URL"]
        SHOP_NAME = item["SHOP_NAME"]
        SHOP_URL =  item["SHOP_URL"]
        COMPANY_NAME = item["COMPANY_NAME"]
        COMPANY_ADDRESS = item["COMPANY_ADDRESS"]
        sql = "insert into tianmao value('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(GOODS_PRICE,GOODS_NAME,GOODS_URL,SHOP_NAME,SHOP_URL,COMPANY_NAME,COMPANY_ADDRESS)
        print(sql)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return item
