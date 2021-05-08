import pymysql
import json
class TENGXUNitem(object):
    def __init__(self):
        print(77777777777777777777777777777777777)
        self.conn=pymysql.connect(host="localhost",user="root",password="root",charset="utf8",port=3306,db="data")
        self.cursor=self.conn.cursor()
    def process_item(self,item,spider):
        print(44444444444444444444444444444)
        sql="insert into zhaopin value('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(item["name"],item["id"],item["dizhi"],
            item["chengshi"],item["leixing"],item["jishu"],item["shijian"])
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()