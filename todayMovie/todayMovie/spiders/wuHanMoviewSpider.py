import scrapy
import re
from todayMovie.items import TodaymovieItem

class WuhanmoviewspiderSpider(scrapy.Spider):
    name = 'wuHanMoviewSpider'
    allowed_domains = ['mtime.com']
    start_urls = ['http://theater.mtime.com/China_Hubei_Province_Wuhan_Wuchang/4316/']

    def parse(self, response):
        selector = response.xpath('/html/body/script[3]/text()')[0].extract()
        moviesStr = re.search('"movies":\[.*?\]',selector).group()   # 在整个字符串中搜索第一个匹配的值
        movieList = re.findall('{.*?}',moviesStr)
        print(1111111111111)
        print(movieList)
        for movie in movieList:
            print(type(movie))
            mDic=eval(movie) #将字符串str当作有效的表达式来求职并返回结果
            print(type(mDic))
            item=TodaymovieItem()
            item['titlecn']=mDic.get("movieTitleCn")
            item['titleen']=mDic.get('movieTitleEn')
            item['director']=mDic.get('director')
            item['runtime']=mDic.get('runtime')
            item['zhuyan']=mDic.get('actor')
            item['juqing']=mDic.get('viewProperty')
            # yield item
            # item=TodaymovieItem()
            # item['titlecn']=movie.get("movieTitleCn")
            # item['titleen']=movie.get("movieTitleEn")
            # item['director']=movie.get("director")
            # item['runtime']=movie.get("runtime")
            # item['zhuyan']=movie.get("actor")
            # item['juqing']=movie.get("viewProperty")
            yield item