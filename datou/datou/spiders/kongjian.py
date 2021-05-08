import scrapy
from datou.items import DatouItem
import json
class KongjianSpider(scrapy.Spider):
    name = 'kongjian'
    allowed_domains = ['image.baidu.com']
    start_urls = ['https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87']

    def parse(self, response):
        print(1111111111111)
        url='https://image.baidu.com/search/acjson?tn=resultjson_com&logid=7829446680957167358&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=%E7%BE%8E%E5%A5%B3%E5%9B%BE%E7%89%87&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&expermode=&force=&cg=girl&pn=30&rn=30&gsm=1e&1604576151995='
        headers={
            'Content-Type':'text/html;charset=UTF-8'
        }
        yield scrapy.Request(url=url,headers=headers,callback=self.pase_in,dont_filter=True)

    def pase_in(self,response):
        print(22222222222)
        result=json.loads(response.text)
        jobs=result["data"]
        for job in jobs:
            item=DatouItem()
            item['tupianming']=job["fromPageTitle"]
            item['tupianurl']=job["thumbURL"]
            item['width']=job["width"]
            item['height']=job["height"]
            item['type']=job["type"]
            yield item



