import pymysql

class DianyingPipeline(object):
    def __init__(self):
        self.db=pymysql.connect(host="localhost",user="root",password="root",port=3306,db="tianqi",charset="utf8")
        self.cursor=self.db.cursor()
    def process_item(self, item, spider):
        yantyan=''
        for y in item["zhuyan"]:
            yantyan=yantyan+'-'+str(y)

        sql="insert into dianyingtop value('{0}','{1}','{2}','{3}')".format(item["top"][0],item["title"][0],str(yantyan)[1:],str(item["bofangcishu"][0]).replace(',',''))

        self.cursor.execute(sql)
        self.db.commit()
        return item
    def parse(self,spider):
        self.cursor.close()
        self.db.close()
