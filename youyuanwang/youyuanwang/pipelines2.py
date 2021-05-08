import redis
import json
r=redis.Redis(host='127.0.0.1',port=6379,db=0)

class youyuanwangjson(object):
    def process_item(self,item,spider):
        link=json.dumps(dict(item),ensure_ascii=False)+",\n"
        print(link)
        r.lpush("youyuanwagjson",link)
        return item