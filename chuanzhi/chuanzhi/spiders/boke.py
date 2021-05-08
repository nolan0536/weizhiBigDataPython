import scrapy
from chuanzhi.items import ChuanzhiItem

class BokeSpider(scrapy.Spider):
    name = 'boke'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/subject/brandzly/index.html?jingjiaczpz-PC-1']

    def parse(self, response):
        print(11111111111111111111111111111111)
        url="http://www.itcast.cn/channel/teacher.shtml#ajavaee"
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        yield scrapy.Request(url=url,headers=headers,callback=self.parse_in,dont_filter=True)

    def parse_in(self,response):
        print(22222222222222222222222222)
        datas=response.xpath('/html/body/div[10]/div/div[2]/ul/li')
        item=ChuanzhiItem()
        for data in datas:
            item["laoshi"]=data.xpath('./div[2]/h2/text()').extract()
            item["zhicheng"]=data.xpath('./div[2]/h2/span/text()').extract()
            item["biaoqian"]=data.xpath('./div[2]/h3/span/text()').extract()
            item["chengguo"]=data.xpath('./div[2]/p/text()').extract()
            yield item


