import pymysql

class TianqiPipeline(object):

    def __init__(self):
        self.db=pymysql.connect(host="localhost",user='root',password='root',port=3306,db='tianqi',charset='utf8')
        self.cursor=self.db.cursor()

    def process_item(self, item, spider):
        print(1111111111111)
        print(item)
        print(22222222222)
        print(item['day'])

        for i in range(0,5):
            sql="insert into tianqi value('{0}','{1}','{2}','{3}','{4}')".format(item['day'][i],item['tianqi'][i],item['max'][i],
                item['min'][i],item['fengli'][i])
            self.cursor.execute(sql)
            self.db.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()

