# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class GuosaiPipeline(object):

    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='root', port=3306, db='guosai', charset='utf8')

        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        print(111)
        data = item['result']
        data_detail = item['result']['detail']

        sql="insert into hotels value('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}'," \
            "'{13}','{14}','{15}','{16}','{17}','{18}','{19}','{20}','{21}','{22}','{23}','{24}','{25}','{26}')".format(data['name'],
             data_detail['SEQ'],data_detail['业务部门'],data_detail['剩余房间'],data_detail['国家'],data_detail['图片数'],
             data_detail['城市'],data_detail['城市平均实住间夜'],data_detail['城市直销拒单率'],data_detail['处于商圈'],data_detail['拒单率是否小于等于直销城市均值'],
             data_detail['是否为客栈'],data_detail['最低房间价格'],data_detail['用户点评数'],data_detail['省份'],
             data_detail['酒店实住订单'],data_detail['酒店实住间夜'],data_detail['酒店总订单'],data_detail['酒店总间夜'],data_detail['酒店星级'],
             data_detail['酒店直销实住订单'],data_detail['酒店直销实住间夜'],data_detail['酒店直销拒单'],data_detail['酒店直销拒单率'],data_detail['酒店直销订单'],
             data_detail['酒店直销间夜'],data_detail['酒店评分'])
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()

        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
