import scrapy


class PachongSpider(scrapy.Spider):
    name = 'pachong'
    allowed_domains = ['as.meituan.com']
    start_urls = ['https://as.meituan.com/meishi/']

    def parse(self, response):
        fenleis=response.xpath('//ul[@class="more clear" data-reactid="29"]/li/a/text()').extract()
        fenleiid=response.xpath('//ul[@class="more clear" data-reactid="29"]/li/a//@data-reactid').extract()
        citys=response.xpath('//ul@[class="more clear" data-reactid="89"]/li/span/b/text()').extract()
        
