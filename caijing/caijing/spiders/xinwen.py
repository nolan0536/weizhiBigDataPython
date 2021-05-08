import scrapy
from caijing.items import CaijingItem

class XinwenSpider(scrapy.Spider):
    name = 'xinwen'
    allowed_domains = ['caijing.com']
    start_urls = ['https://www.caijing.com.cn/']

    def parse(self, response):
        print(1111111111111111111111111111)
        datas=response.xpath('//*[@id="area_index_comm_top1_2011"]/div/div[2]/div[2]/ul[1]/li')
        for data in datas:
            url=data.xpath('./a/@href').extract()[0]
            print(url)
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
            yield scrapy.Request(url=url,headers=headers,callback=self.parse_in,dont_filter=True)

    def parse_in(self,response):
        print(222222222222222222222222222)
        item=CaijingItem()
        datas=response.xpath('/html/body/div[4]/div/div[4]/div[1]/div[2]/div')
        for data in datas:
            item["title"]=data.xpath("./div[1]/a/text()").extract()[0]
            item["div"]=data.xpath("./div[1]/div[1]/span/text()").extract()[0]
            print(item)
            yield item

