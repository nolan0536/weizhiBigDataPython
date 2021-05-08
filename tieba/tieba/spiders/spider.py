import scrapy
from tieba.items import TiebaItem

class Spider(scrapy.Spider):
    name = 'tieba'
    allowed_domains = ['baidu.com']
    start_urls = ['https://tieba.baidu.com/f?kw=%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB',]

    def parse(self, response):

        item = TiebaItem()
        item['title'] = response.xpath('//li/div/div[2]/div[1]/div[1]/a/text()').extract()
        item['author'] = response.xpath('//li/div/div[2]/div[1]/div[2]/span[1]/span[1]/a/text()').extract()
        item['reply'] = response.xpath('//li/div/div[1]/span/text()').extract()  # TODO 前两条评论无法输出
        print(item)
        yield item




        #翻页
        next_page = response.xpath('//*[@id="frs_list_pager"]/a[10]').get() #使用Xpath 提取网页的下一页
        if next_page:
            #拼接网址
            #next_url = 'https://tieba.baidu.com/f?kw=%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB'+next_page
            next_url = response.urljoin(next_page)  #绝对路径
            #发出请求Request   callback 是回调函数 就是将请求得到的响应交给自己处理
            yield scrapy.Request(next_url,callback=self.parse)  #生成器
