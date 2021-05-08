# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql

class XiaoshuopaihangPipeline(object):
    def process_item(self, item, spider):
        db=pymysql.connect(host="localhost",user="root",password="root",db="tianqi",charset="utf8")
        cursor=db.cursor()
        title=item["title"][0]
        zuozhe=item["zuozhe"][0]
        leixing=item["leixing"][0]
        zhangjie=item["zhangjie"][0]
        time=item["time"][0]
        sql = "insert into xiaoshuo value('{0}','{1}','{2}','{3}',str_to_date('{4}','%Y-%m-%D %H:%i'))".format(title,zuozhe,leixing,zhangjie,time)
        print(sql)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        db.close()
        return item
