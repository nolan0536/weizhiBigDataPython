from urllib import request
import requests练习
import os
import time

def get_image(keywords,num):
    url="https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=index&fr=&hs=0&xthttps=111111&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E7%80%91%E5%B8%83&oq=%E7%80%91%E5%B8%83&rsp=-1"
    headers = {    #请求头
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4259.3 Safari/537.36",
        "Host": "image.baidu.com",
        "Referer": "https: // image.baidu.com /"
    }



    sendData = {} #发送二进制字符串
    send_data = data.splitlines()  #读取文本文件的数据
    try:
        for i in send_data:
            data_list = i.split(':') #进行分割
        if len(data_list)==2: #如果有两个的话 把他们分成对应的键值对
            key,value = data_list
            if key and value:
                sendData[key] = value
    except Exception as e:
        print(e)
    sendData["word"] = sendData["queryWord"] = keywords
    sendData["rn"] = str(1*num)
    response = requests练习.get(url=url, headers=headers, params=sendData)
    content = response.json()['data']
    for index,src in enumerate(content):
        image_url =src.get("middleURL")
        if os.path.exists("image"):
            pass
        else:
            os.mkdir("image")
        if image_url and os.path.exists("image"):
            name = "./image/image_%s_%s.jpg"%(index,keywords)
            try:request.urlretrieve(url=image_url,filename=name)
            except Exception as e:
                print(e)
            else:
                print("%s is download"%name)
                time.sleep(1)
if __name__ =="__main__":
    keywords = input("请输入要爬取图片内容：")
    num = int(input("想要多少输入多少:"))
    get_image(keywords,num)
