import redis
import pymysql
import json

def parse():
    redis_name=redis.Redis(host="127.0.0.1",port=6379,db=0)

    mysql_name=pymysql.connect(host="localhost",user="root",password="root",port=3306,charset="utf8",db="tianqi")

    datas=redis_name.lrange("gupiaojson",0,-1)

    for data in datas:
        print(data)
        item=json.loads(data)
        print(item)
        cursor = mysql_name.cursor()
        sql="insert into xuangubao value('{0}',{1},'{2}',{3})".format(item["symbol"],item["change_percent"],                                                             item["stock_chi_name"],item["price_change"])
        print(sql)
        cursor.execute(sql)
        mysql_name.commit()
    cursor.close()

if __name__=="__main__":
    parse()
