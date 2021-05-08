import redis

# pool=redis.ConnectionPool(host='127.0.0.1',port=6379)
# r = redis.Redis(connection_pool=pool)

r = redis.Redis(host="127.0.0.1",port=6379,db = 0)


datas=r.lrange("guosaiJson",0,10)
for data in datas:
    print(data)
    item=data.decode("utf-8")
    print(item)