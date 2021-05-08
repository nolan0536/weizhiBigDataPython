# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
class YouyuanwangPipeline(object):
    def __init__(self):
        self.db=pymysql.connect(host='localhost',user='root',password='root',port=3306,charset='utf8',db='tianqi')
        self.cursor=self.db.cursor()
    def process_item(self, item, spider):
        print(111111111111111111)
        item["neixindubai"]=str(item["neixindubai"]).replace(' ','')
        sql="insert into youyuanwang value('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(item['wangming'],
            item['jiguan'],item['tizhong'],item['xueli'],item['jibenxinxi'],item['neixindubai'],item['yuexin'])
        self.cursor.execute(sql)
        self.db.commit()
    def parse(self,spider):
        self.cursor.close()
        self.db.close()