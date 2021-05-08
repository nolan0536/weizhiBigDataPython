import redis
import json
class XuangubaoPipeline(object):
    def __init__(self):
        self.r=redis.Redis(host="127.0.0.1",port=6379,db=0)
    def process_item(self, item, spider):
        links=json.dumps(dict(item),ensure_ascii=False)
        self.r.lpush("gupiaojson",links)

        return item
