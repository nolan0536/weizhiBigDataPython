# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings

# class ImagesPipeline(ImagesPipeline):
# IMAGES_STORE=get_project_settings().get("IMAGES_STORE")
class ImagesPipeline(ImagesPipeline):
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")
    # def get_media_request(self,item,info):
    #     image_url=item["image_link"]
    #     print("0000000"+str(image_url))
    #     yield scrapy.Request(image_url)
    # def get_media_requests(self,item,info):
    #     image_url = item["image_link"]
    #     print("0000000" + str(image_url))
    #     yield scrapy.Request(image_url)
    def get_media_requests(self,item,indo):
        image_url = item["image_link"]
        print("000000" + str("image_link"))
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        print("11111111"+str(results))

        image_path=[x["path"] for ok, x in results if ok]
        print(image_path)
        os.rename(self.IMAGES_STORE+"/"+image_path[0],self.IMAGES_STORE+"/ "
                  +item["nick_name"]+".jpg")
        item["image_path"]=self.IMAGES_STORE+"/"+item["nick_name"]
        return item

