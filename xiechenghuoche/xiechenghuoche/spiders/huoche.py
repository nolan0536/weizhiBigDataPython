import scrapy
from xiechenghuoche.items import XiechenghuocheItem

class HuocheSpider(scrapy.Spider):
    name = 'huoche'
    allowed_domains = ['www.ctrip.com']
    start_urls = ['https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index']

    def parse(self, response):
        print(111111111111111111111111111)
        print(response)
        url='https://trains.ctrip.com/TrainBooking/Search.aspx?from=beijing&to=shanghai&day=2&fromCn=%25E5%258C%2597%25E4%25BA%25AC&toCn=%25E4%25B8%258A%25E6%25B5%25B7'
        headers={
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 Safari/537.36'
        }
        yield scrapy.Request(url=url,headers=headers,callback=self.parse_on,dont_filter=True)
    def parse_on(self,response):
        print(22222222222222)
        print(response)
        jobs=response.xpath('//div[@class="List-Wrap train_item_list"]/div')
        for job in jobs:
            item=XiechenghuocheItem()
            item['chehao']=job.xpath('./div[1]/div[1]/strong/text()').extract()
            item['chufazhan']=job.xpath('./div[2]/div[2]/span/text()').extract()
            item['chufashijian']=job.xpath('./div[2]/div/strong/text()').extract()
            item['daodashijian']=job.xpath('./div[4]/div[1]/label/strong/text()').extract()
            item['zhongdianzhan']=job.xpath('./div[4]/div[2]/span/text()').extract()
            item['shijian']=job.xpath('./div[3]/div[1]/text()').extract()[0]
            item['jiage']=job.xpath('./div[5]/div[1]/b/text()').extract()
            yield item
