import scrapy
import json
import re
from tubatu.items import TubatuItem
class ZhuangxiuSpider(scrapy.Spider):
    name = 'zhuangxiu'
    allowed_domains = ['xiaoguotu.to8to.com']
    start_urls = ['https://xiaoguotu.to8to.com/tuce/']

    def parse(self, response):
        url_tager=response.xpath('//div[@oldaid]')
        content_id_search = re.compile(r"(\d+)\.html")
        for item in url_tager:
            info={}
            info["content_name"]=item.xpath('./div/a/text()').extract_first()
            info["content_url"]=item.xpath('./div/a/@href').extract_first()
            info["content_id"]=content_id_search.search(info["content_url"]).group(1)
            url='https://xiaoguotu.to8to.com/case/list?a2=0&a12=&a11={}}&a1=0'.format(info["content_id"])
            yield scrapy.FormRequest(url=url,callback=self.parse_in,
                                     meta=info)
    def parse_in(self, response):
        # content_name=response.meta["content_name"]
        # content_url=response.meta["content_url"]
        # content_id=response.meta["content_id"]
        result=json.loads(response.text)["dataImg"]
        for items in result:
            for item in items["album"]:
                tubatu=TubatuItem()
                tubatu["nick_name"]=item["1"]["n"]
                



