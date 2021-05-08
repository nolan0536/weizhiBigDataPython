import pymysql
class LianfangPipeline(object):
    def __init__(self):
        self.db=pymysql.connect(host="localhost",user="root",password="root",port=3306,db="tianqi",charset="utf8")
        self.cursor=self.db.cursor()
    def process_item(self, item, spider):
        print(11111111111111)
        print(item)
        item["title"]=str(item["title"]).replace(' ','')
        item["jiage"] = item["jiage"] + "w"
        item["danjia"] = str(item["danjia"])[2:]
        item["xinxi"]=str(item["xinxi"]).replace('|','-').replace(' ','')
        sql="insert into lianfang value('{0}','{1}','{2}','{3}','{4}')".format(item["title"],item["xinxi"],
                                                                    item["jiage"],item["dizhi"],item["danjia"])
        print(sql)
        self.cursor.execute(sql)
        self.db.commit()
        return item
    def prece_close(self,spider):
        self.cursor.close()
        self.db.close()
