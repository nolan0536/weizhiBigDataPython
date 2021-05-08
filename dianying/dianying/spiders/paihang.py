import scrapy
from dianying.items import DianyingItem

class PaihangSpider(scrapy.Spider):
    name = 'paihang'
    allowed_domains = ['1905.com']
    start_urls = ['https://www.1905.com/vod/rank/t0a0o3.shtml']

    def parse(self, response):
        infos=response.xpath('//div[@class="tableRANK"]/dl')
        for info in infos:
            item=DianyingItem()
            item["top"]=info.xpath('./dt[1]/b/text()').extract()
            item["title"]=info.xpath('./dt[3]/a/text()').extract()
            item["zhuyan"]=info.xpath('./dt[4]/span/a/text()').extract()
            item["bofangcishu"]=info.xpath('./dt[5]/span/text()').extract()
            yield item


