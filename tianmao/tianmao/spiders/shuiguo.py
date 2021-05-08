import scrapy
from tianmao.items import TianmaoItem

class ShuiguoSpider(scrapy.Spider):
    name = 'shuiguo'
    allowed_domains = ['www.tianmao.com']
    start_urls = ['https://list.tmall.com/search_product.htm?q=%CB%AE%B9%FB&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton']

    def parse(self, response):
        print(1111111111111111111111111111111111111)
        divs=response.xpath('//*[@id="J_ItemList"]/div')

        for div in divs:
            item=TianmaoItem()
            item['title']=div.xpath('./div/p[2]/a/@title')[0].extract()
            item['jiage']=div.xpath('./div/p[1]/em/@title')[0].extract()
            item['yuexiao']=div.xpath('./div/p[3]/span[1]/em/text()')[0].extract()
            item['pingjia']=div.xpath('./div/p[3]/span[2]/a/text()')[0].extract()
            url=div.xpath('./div/div[1]/a/@href')[0].extract()
            item['dianpuurl']=url if "http:" in url else ("http:"+url)

            yield scrapy.FormRequest(url=item['dianpuurl'],meta={'item':item},callback=self.parse_in,
                                     dont_filter=True)
    def parse_in(self,response):
        divs=response.xpath('//*[@id="J_AttrUL"]/')

        for div in divs:
            item=TianmaoItem()
            item['dianming']=div.xpath('./li[1]/@title')
            item['changzhi']=div.xpath('./li[2]/@title')
            item['cjdh']=div.xpath('./li[3]/@title')
        yield item








