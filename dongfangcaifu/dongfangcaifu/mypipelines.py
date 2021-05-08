import json

class DongfangcaifuPipeline(object):

    def __init__(self):
        self.jsons=open("东方财富网.json","w",encoding="utf-8")

    def process_item(self, item, spider):

        lino=json.dumps(item,ensure_ascii=False)+",\n"
        self.jsons.write(lino)
        return item