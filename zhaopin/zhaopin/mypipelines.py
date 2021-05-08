import pymysql

class ZhaopinPipeline(object):
    def __init__(self):
        self.db=pymysql.connect(host="localhost",user="root",password="root",port=3306,db="tianqi",charset="utf8")
        self.cursor=self.db.cursor()
    def process_item(self, item, spider):
        print(1111111111111)
        print(item)
        for i in range(0,20):
            sql="insert into zhaopin value('{0}','{1}','{2}')".format(item['zhiwei'][i],item['yuexin'][i],item['gongsi'][i])
            self.cursor.execute(sql)
            self.db.commit()
        return item
    def prose_closs(self,spider):
        self.cursor.close()
        self.db.close()