# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class TianmaoPipeline:
    def __init__(self):
        self.db=pymysql.connect(host='localhost', user='root', password='root', port=3306, db='tianqi', charset='utf8')
        self.courser=self.db.cursor()

    def process_item(self, item, spider):
        print(1111111111111111111111111111111111111111)
        sql="insert into tianmao value('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(item['title'],item['jiage'],
            item['yuexiao'],item['pingjia'],item['dianpuurl'],item['dianming'],item['changzhi'],item['cjdh'])
        self.courser.execute(sql)
        self.db.commit()
        return item

    def close_spider(self,spider):
        self.courser.close()
        self.db.close()

