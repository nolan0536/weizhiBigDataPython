# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class DangdangPipeline(object):
    def process_item(self, item, spider):
        db = pymysql.connect(host="localhost",user="root",password="root",db="tianqi",charset="utf8")
        cursor = db.cursor()
        name=item["name"][0]
        author=item["author"][0]
        price=item["price"][0].strip('¥') #删除货币标志
        pingjia=str(item["pingjia"][0])[:-3] #转换成字符串模式 截取从开始到倒数第三个字符之前的
        press=item["press"][0]
        time=str(item["time"][0]).strip(' /') #删除时间前面的’/‘
        jianjie=item["jianjie"][0]
        # time=str(item["time"][0]).split("/")[1] #删除时间前面的’/‘  #截取

        #对数据库进行插入操作，将提取到的item对象中的数据插入到tianqi数据库的dd数据表中
                                                                 #日期需要进行转义
        sql = "insert into dd value('{0}',{1}+0,'{2}','{3}','{4}',str_to_date('{5}','%Y-%m-%D'),'{6}')".format(name,price,author,pingjia,press,time,jianjie)
        print(sql)
        cursor.execute(sql)
        db.commit()
        #关闭游标对象和数据库对象
        cursor.close()
        db.close()
        return item
