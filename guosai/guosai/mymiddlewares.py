
import json
import redis

# pool=redis.ConnectionPool(host='127.0.0.1',port=6379)
# r = redis.Redis(connection_pool=pool)
r = redis.Redis(host="127.0.0.1",port=6379,db = 0)

class GuosaiJSON(object):
    # def __init__(self):
    #     self.store_file = open('酒店.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        line_no=json.dumps(dict(item),ensure_ascii=False)+",\n"
        # self.store_file.write(line_no)
        print(line_no)
        r.lpush("guosaiJson", line_no)
        return item

# class GuosaiCSV(object):
#     def __init__(self):
#         self.gscsv=open('guosaai.csv','w',encoding='utf-8')
#         self.writer = csv.writer(self.gscsv)
#         self.jedge=True
# 
# 
#     def process_item(self, item, spider):
#         print(2222222)
#         id_name_key = [k for k, v in item['result']['detail'].items()]
#         if self.jedge==True:
# 
#             self.writer.writerow(id_name_key)
#             self.jedge=False
# 
# 
#         id_name_values = [v for k, v in item['result']['detail'].items()]
#         self.writer.writerow(id_name_values)
#         return item
# 
#     def close_spider(self,spider):
#         self.gscsv.close()

