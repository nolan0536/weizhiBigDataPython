import redis
r=redis.Redis(host='127.0.0.1',port=6379)
r.set('name','小强')
print(r.get('name'))
# r.setex("name","qiyi",5)
# print(r.get("name"))
# print(r.setnx('name','hah'))
print(r.lpop("new:items"))


# set test 小白
# get test