import pymysql
class DoubanPipeline(object):
    def __init__(self):
        self.db=pymysql.connect(host="localhost",user="root",password="root",port=3306,db="tianqi",charset="utf8")
        self.cursor=self.db.cursor()
    def process_item(self, item, spider):
        # item['dyxx']=str(item['dyxx']).replace('\\n','')
        # item['dyxx']=str(item['dyxx']).replace('\\\\\\','')
    
        item['titlecn']=str(item['titlecn'])
        item['titleen']=str(item['titleen'])
        item['pingfen']=str(item['pingfen'])
        item['pingjiashu']=str(item['pingjiashu'])
        item['jianshu']=str(item['jianshu'])

        print(type(item['titlecn']))
        sql="insert into douban value('{0}','{1}',{2}+0,'{3}','{4}')".format(item['titlecn'],item['titleen'],
            item['pingfen'],item['pingjiashu'],item['jianshu'])
        print(sql)
        self.cursor.execute(sql)
        self.db.commit()
        return item
    def parse(self,spider):
        self.cursor.close()
        self.db.close()