import pymysql
class Tengxun34mysql(object):
    def __init__(self):
        print(222222222222222222222222222)
        self.conn=pymysql.connect(host='localhost',user='root',password='root',port=3306,db='tianqi',charset='utf8')
        self.cursor=self.conn.cursor()
    def process_item(self, item, spider):
        print(1111111111111111)
        print(item)
        item["CategoryName"]=str(item["CategoryName"])
        item["guojia"]=str(item["guojia"])
        item["diqu"]=str(item["diqu"])
        item["time"]=str(item["time"])
        item["gangwei"]=str(item["gangwei"])
        item["postid"]=str(item["postid"])
        sql="insert into tengxun value('{0}','{1}','{2}','{3}','{4}','{5}')".format(item["CategoryName"],item["guojia"],
                                         item["diqu"],item["time"],item["gangwei"],item["postid"])
        print(sql)
        self.cursor.execute(sql)
        self.conn.commit()
        return item
    def colse(self,spider):
        self.cursor.close()
        self.conn.close()