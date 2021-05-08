# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import re


class CateringCrawlPipeline(object):

    def __init__(self):
        """
        此函数：实例化csv对象，并写入表头数据。
        """
        #写模式打开文件data.csv
        #编码utf-8
        # 采用newline参数阻止csv数据与数据之间生成空白行
        self.file = open("data.csv","w",encoding="utf-8",newline="")
        self.writer =csv.writer(self.file)
        self.writer.writerow(['所属年月', '商家名称', '主营类型', '店铺URL',
                              '特色菜', '累计评论数', '累计销售量', '店铺评分',
                              '本月销量', '本月销售额', '城市', '商家地址', '电话'])

    def process_item(self, item, spider):
        """
        此函数：对数据进行简单的预处理，使得输出的csv数据整体整齐
        """
        # 通过正则表达式等操作对数据预处理
        date = ''.join(re.findall('(\d{4}-\d{1,2}-\d{1,2})', item['date']))
        rs_name = item['rs_name']
        food_type = item['food_type']

        url = ''.join(re.findall('url:(.*)',item["url"]))
        # feature_food = ''.join(re.findall(': (.*)', item['feature_food']))
        feature_food = ''.join(re.findall('：(.*)', item['feature_food']))
        print(feature_food)
        comment = ''.join(re.findall('(\d+.\d+)',item["comment"]))
        sale_cumulative = ''.join(re.findall('(\d+.\d+)',item["sale_cumulative"]))
        score = item['score']
        sale = ''.join(re.findall('(\d+.\d+)',item["sale"]))
        sale_vol = ''.join(re.findall('(\d+.\d+)',item["sale_vol"]))
        city = item['city']
        address = item['address']
        phone = item['phone']

        self.writer.writerow([date, rs_name, food_type, url, feature_food, comment, sale_cumulative, score,
                              sale, sale_vol, city, address, phone])

        return item

    def close_spider(self, spider):
        # 关闭爬虫时顺便将文件保存退出
        self.file.close()
