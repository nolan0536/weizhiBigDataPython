import json
class TodaymoviePipeline:
    def __init__(self):
        self.file=open('dianying.json','w',encoding='utf-8')

    def process_item(self, item, spider):
        lino=json.dumps(dict(item),ensure_ascii=False)+",\n"
        self.file.write(lino)
        return item