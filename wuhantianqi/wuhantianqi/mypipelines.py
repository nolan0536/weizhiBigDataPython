import json

class WuhantianqiPipeline(object):
    def __init__(self):
        self.lino=open('tianqi.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        file=json.dumps(dict(item),ensure_ascii=False) + ",\n"
        self.lino.write(file)
        return item