import redis
R=redis.Redis(host="127.0.0.1",port=6379,db=0)
datas=R.lrange("bili:items",0,-1)
for data in datas:
    item=data.decode("utf-8")
    print(item)