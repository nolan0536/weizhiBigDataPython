import scrapy
from catering_crawl.items import CateringCrawlItem



class CateringScrapy(scrapy.Spider):

    name = 'catering'
    start_urls =['http://192.168.29.54:8080/foods/details']

    def parse(self, response):
        print(1111111111111111111111111111111111111)
        """
        函数功能：
        1、使用xpath语法提取城市、主营类型、主营类型对应的id；
        2、循环遍历提取数据，构建新参数，筛选出不同城市不同主营类型的店铺信息；
        3、信息以及页码数以参数的形式传递到下一个函数。
        """
        # citys =response.xpath('//ul[@class="more clear" data-reactid="80"]/li/text()').extract()   # 所有城市
        # cateIds = response.xpath('//ul class="more clear" data-reactid="20"/li/a//@id').extract()    # 所有主营分类id
        # food_types =response.xpath('//ul class="more clear" data-reactid="20"/li/text()').extract()  # 所有主营分类
        citys =   # 所有城市
        cateIds =   # 所有主营分类id
        food_types =   # 所有主营分类

        # zip将主营类型id和主营类型进行合并，将两个值以参数的形式传给下一个函数。
        for cateId, f_type in zip(cateIds, food_types):
            for city in citys:
                yield scrapy.Request(',callback=self.parse_next_page,
                                     meta={'food_type': , 'city':,'cateId': ,'page':'1' })

    def parse_next_page(self, response):
        print(222222222222222222222222222222222222)
        """
        函数功能：
        1、获取上一个函数传递过来的参数；
        2、如果存在其他页店铺信息，将新的page（页码数）传递到url中请求新页码url，
        需要关键参数的传递，以及函数本身的回滚，完成函数内部循环。
        3、将“城市”、“主营分类”和“页数”以参数的形式传递到下一个函数，用于整合店铺所有信息的汇总。

        说明：判断是否有下一页，由于网站分页用的是js组件自动生成，无法通过爬虫获取到其中的页码数，
        所以这里通过判断下一页是否存在内容来完成分页爬虫。
        """
        # 获取关键的四个参数
        food_type = response.meta['food_type']
        city = response.meta['city']
        cateId = response.meta['cateId']
        page = response.meta['page']

        # xpath提取页面的店家ul标签中的内容
        restaurant_urls =
        # 返回的xpath选择器内容不为空，表示当前页面或者下一页存在需要的内容，如果urls为空，则不请求下一页
        if restaurant_urls:
            # 提取店家的详情页面的url，并请求相应的页面
            for rs_url in restaurant_urls:
                yield scrapy.Request(,callback=self.parse_restaurant,meta={})
            # 假设有下一页
            next_page = int(page) + 1
            # page页码数+1，继续请求相应的url
            yield scrapy.Request()


    def parse_restaurant(self, response):
        print(3333333333333333333333333333333333)
        """
        此函数完成：
        使用xpath匹配需要提取的字段数据，并将数据保存在item对象中。
        """
        item =CateringCrawlItem()
        item['date'] =response.xpath('//*[@id="app"]/section/div/div[2]/div[1]/div[3]/p[10]/text()').extract()[0].strip()		#日期
        item['rs_name'] = response.xpath('//*[@id="app"]/section/div/div[2]/div[1]/div[1]/text()').extract()[1].strip()        #名称
        item['food_type'] =response.meta["food_type"].strip()       #主营类型
        item['url'] =  response.xpath('//*[@id="app"]/section/div/div[2]/div[1]/div[3]/p[9]/text()').extract()[0].strip()             #url
        item['feature_food'] = response.xpath('//*[@id="app"]/section/div/div[2]/div[1]/div[3]/p[4]/text()').extract()[0].strip()     #特色菜
        item['comment'] =response.xpath('//*[@id="app"]/section/div/div[2]/div[1]/div[3]/p[5]/text()').extract()[0].strip()           #评论数
        item['sale_cumulative'] = response.xpath('//*[@id="app"]/section/div/div[2]/div[1]/div[3]/p[6]/text()').extract()[0].strip()  #销售人次
        item['score'] =response.xpath('//*[@id="app"]/section/div/div[2]/div[1]/div[2]/p/text()').extract()[0].strip()        #评分
        item['sale'] = response.xpath('//*[@id="app"]/section/div/div[2]/div[1]/div[3]/p[7]').extract()[0].strip()     #销量
        item['sale_vol'] = response.xpath('//*[@id="app"]/section/div/div[2]/div[1]/div[3]/p[8]/text()').extract()[0].strip()     #销售额
        item['city'] =response.meta["city"].strip()          #城市
        item['address'] =  response.xpath('//*[@id="app"]/section/div/div[2]/div[1]/div[3]/p[1]/text()').extract()[1].strip()     #地址
        item['phone'] = response.xpath('//*[@id="app"]/section/div/div[2]/div[1]/div[3]/p[2]/text()').extract()[1].strip()        #电话

        yield item
