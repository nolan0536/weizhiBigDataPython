import requests
import json
from lxml import etree

def process():
    pages=11
    for page in range(0,pages):
        url="https://movie.douban.com/top250?start={}&filter=".format(page*25)
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
        }
        response=requests.get(url,headers=headers)
        reques=response.text
        html=etree.HTML(reques)
        print(html)
        jobs=html.xpath('//*[@id="content"]/div/div[1]/ol/li')
        item={}
        for job in jobs:
            item["title"]=job.xpath("./div[1]/div[2]/div[1]/a/span/text()")[0]
            item["mingyan"]=job.xpath('./div[1]/div[2]/div[2]/p[2]/span/text()')
            print(item)
            links=open("豆瓣top250.json","a",encoding="utf-8")
            link=json.dumps(dict(item),ensure_ascii=False)+",\n"
            links.write(link)



if __name__=='__main__':
    process()
