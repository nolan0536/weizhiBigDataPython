import scrapy
from guazi.items import GuaziItem

class ErshoucheSpider(scrapy.Spider):
    name = 'ershouche'
    allowed_domains = ['guazi.com']
    start_urls = ['https://www.guazi.com/weifang/sell/index?ca_s=sem_baiduss&ca_n=zlpcocpc_newshouye&ca_keywordid=182641808909&ca_term=%E4%BA%BA%E4%BA%BA%E7%BD%91%E4%BA%8C%E6%89%8B%E8%BD%A6&ca_transid=8769456846664930957&tk_p_mti=ad.sem_baiduss.zlpcocpc_newshouye.1.187652757160497152']

    def parse(self, response):
        print(111111111111111111111111111)
        datas=['weifang','weihai','linyi']
        pages=100
        # for page in range(1,int(pages)):
        for data in datas:
            url="https://www.guazi.com/{}/buy/o2/#bread".format(data)
            print(url)
            headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
            }
            yield scrapy.Request(url,headers=headers,callback=self.parse_in,dont_filter=True)
    def parse_in(self,response):
        print(222222222222222222222222222222222)
        datas=response.xpath('//html/body/div[6]/ul/li')
        for data in datas:
            print(data)
            item=GuaziItem()
            item["title"]=data.xpath('./a/@title').extract()
            item["nianfen"]=data.xpath('./a/div[1]/text()').extract()
            item["jiage"]=data.xpath('./a/div[2]/p/text()').extract()
            yield item

