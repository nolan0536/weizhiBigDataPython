import pymysql

class AnjukePipeline(object):
    def __init__(self):
        self.db=pymysql.connect(host="localhost",user="root",password="root",port=3306,db="tianqi",charset="utf8")
        self.cursor=self.db.cursor()
    def process_item(self, item, spider):
        print(111111111111)
        print(item)
        item['title'] = str(item['title']).replace(' ', '').replace('\n', '')
        item['jiage'] = str(item['jiage']) + 'w'
        sql="insert into anjuke value('{0}','{1}','{2}','{3}','{4}','{5}')".format(item['title'],
            item['jushi'],item['xiaoqu'],item['mianji'],item['jiage'],item['danjia'])
        self.cursor.execute(sql)
        self.db.commit()
        return item
    def parse_close(self,spider):
        self.cursor.close()
        self.db.close()