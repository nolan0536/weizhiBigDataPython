import scrapy
import json
import re
from movie.items import MovieItem
class JingangchuanSpider(scrapy.Spider):
    name = 'jingangchuan'
    allowed_domains = ['movie.mtime.com']
    start_urls = ['http://movie.mtime.com/268304/']

    def parse(self, response):
        print(111111111111111111111111)
        headers={
            'Content-Type': 'application/x-javascript; charset=utf-8'
        }
        url='http://service.library.mtime.com/Movie.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Library.Services&Ajax_CallBackMethod=GetMovieOverviewRating&Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Fmovie.mtime.com%2F268304%2F&t=20201138233792170&Ajax_CallBackArgument0=268304'
        yield scrapy.FormRequest(url=url,headers=headers,callback=self.parse_in, dont_filter=True)
    def parse_in(self,response):
        print(response.text)
        pattern=re.compile(r'=(.*?);')
        result=pattern.findall(response.text)[0]
        movie=json.loads(result)
        movieTitle=movie.get("value").get("movieTitle")
        values=movie.get("value").get("movieRating")
        item = MovieItem()
        item["movietitle"]=movieTitle
        item["movieid"]=values.get("MovieId")
        item["zonghe"]=values.get("RatingFinal")
        item["daoyan"]=values.get("RDirectorFinal")
        item["huamian"]=values.get("ROtherFinal")
        item["gushi"]=values.get("RPictureFinal")
        item["yinyue"]=values.get("RShowFinal")
        item["canyurenshu"]=values.get("Usercount")
        item["xiangkan"]=values.get("AttitudeCount")

        return item
