import pymysql
class YangtiPipeline(object):
    def __init__(self):
        self.db=pymysql.connect(host="localhost",port=3306,charset="utf8",user="root",password="root",db="guosai")
        self.cursor=self.db.cursor()
    def process_item(self, item, spider):
        print(444444444444444444444)
        sql="insert into gongzuo value('{0}','{1}','{2}','{3}','{4}')".format(item["gongsi"],item["gongzuo"],
            item["chengshi"],item["yuexin"],item["gangweizhize"])
        print(sql)
        self.cursor.execute(sql)
        self.db.commit()
        return item
    def close(self,spider):
        self.cursor.close()
        self.db.close()