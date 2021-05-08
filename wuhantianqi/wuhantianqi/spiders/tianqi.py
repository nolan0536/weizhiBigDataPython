import scrapy
from wuhantianqi.items import WuhantianqiItem

class TianqiSpider(scrapy.Spider):
    name = 'tianqi'
    allowed_domains = ['tianqi.com']
    start_urls = ['https://www.tianqi.com/wuhan/']

    def parse(self, response):
        city=response.xpath('//dd[@class="name"]/h2/text()').extract()
        Selector=response.xpath('//div[@class="day7"]')
        data=Selector.xpath('ul[@class="week"]/li/b/text()').extract()
        week=Selector.xpath('ul[@class="week"]/li/span/text()').extract()
        wind=Selector.xpath('ul[@class="txt"]/li/text()').extract()
        weather=Selector.xpath('ul[@class="txt txt2"]/li/text()').extract()
        max=Selector.xpath('div[@class="zxt_shuju"]/ul/li/span/text()').extract()
        min=Selector.xpath('div[@class="zxt_shuju"]/ul/li/b/text()').extract()
        for i in range(7):
            item=WuhantianqiItem()
            item['citydata']=city[0]+data[i]
            item['week']=week[i]
            item['wind']=wind[i]
            item['temperaturn']=max[i]+','+min[i]
            item['weather']=weather[i]
            yield item

