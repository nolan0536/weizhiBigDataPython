import scrapy


class ZhihuspiderSpider(scrapy.Spider):
    name = 'zhihuspider'
    allowed_domains = ['zhihu.com']
    start_urls = ['https://www.zhihu.com/search?type=content&q=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0']

    def parse(self, response):
        print(11111111111111)
        url='https://www.zhihu.com/api/v4/search_v3?t=general&q=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&correction=1&offset=91&limit=20&lc_idx=91&show_all_topics=0&search_hash_id=beec4f7726845f7c2168964ef0107879&vertical_info=1%2C1%2C0%2C0%2C0%2C0%2C0%2C0%2C0%2C1'
        print(response.text)
        yield scrapy.Request(url=url,callback=self.parse_in)
    def parse_in(self,response):
        print(22222222)
        