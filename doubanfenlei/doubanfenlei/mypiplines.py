import pymysql

class DoubanfenleiPipeline(object):
    def __init__(self):
        self.db=pymysql.connect(host="localhost",user="root",password="root",port=3306,db="tianqi",charset="utf8")
        self.cursor=self.db.cursor()
    def process_item(self, item, spider):
        print(111111111111)
        print(item)
        daoyan=''
        for i in item["daoyan"]:
            daoyan=daoyan+'-'+str(i)
        zhuyan=''
        for j in item["zhuyan"]:
            zhuyan=zhuyan+'-'+str(j)

        sql="insert into douban1 value('{0}','{1}','{2}',{3}+0,'{4}')".format(item["title"],str(daoyan)[1:],str(zhuyan)[1:],
                                                                              item["pingfen"],item["url"])
        print(sql)
        self.cursor.execute(sql)
        self.db.commit()
        return item
    def process_closs(self,spider):
        self.cursor.close()
        self.db.close()