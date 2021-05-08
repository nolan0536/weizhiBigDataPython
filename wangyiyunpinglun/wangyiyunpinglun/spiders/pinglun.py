import scrapy
from wangyiyunpinglun.items import WangyiyunpinglunItem

class PinglunSpider(scrapy.Spider):
    name = 'pinglun'
    allowed_domains = ['music.163.com']
    start_urls = ['http://music.163.com/']

    def parse(self, response):
        url="https://music.163.com/#/my/m/music/playlist?id=2404322145"
        headers={
            "user-agent":" Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        yield scrapy.Request(url,headers=headers,callback=self.parse_in,dont_filter=True)
    def parse_in(self,response):
        print(11111111111111111111111111111)
        datas=response.xpath('//*[@id="auto-id-4J7uXKOB4d0WnGwK"]/table/tbody/tr')
        print(datas)
        for data in datas:
            url=data.xpath('./tr[1]/td[2]/div[1]/div[1]/div[1]/span[1]/a/@href').extract()[0]
            print(url)
            headers = {
                "user-agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
            yield scrapy.Request(url="https://music.163.com/#"+url,headers=headers,callback=self.parse_on,dont_filter=True)
    def parse_on(self,response):
        print(2222222222222222222222222222)
        item=WangyiyunpinglunItem()
        item["geming"]=response.xpath('//*[@id="auto-id-xHbZH3h5IWnRT1Tt"]/div[3]/div[1]/div/div/div[1]/div[1]/div[2]/div[1]/div/em/text()').extract()
        item["geshou"]=response.xpath('//*[@id="auto-id-xHbZH3h5IWnRT1Tt"]/div[3]/div[1]/div/div/div[1]/div[1]/div[2]/p[1]/span/a/text()').extract()
        item["zhuanji"]=response.xpath('//*[@id="auto-id-xHbZH3h5IWnRT1Tt"]/div[3]/div[1]/div/div/div[1]/div[1]/div[2]/p[2]/a/text()').extract()
        item["pls"]=response.xpath('//*[@id="auto-id-51FTVAT4FUEM5GWS"]/div[1]/span/span/text()').extract()
        item["pl"]=response.xpath('//*[@id="auto-id-Z250qbb2XQMw3csF"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/text()').extract()
        yield item
