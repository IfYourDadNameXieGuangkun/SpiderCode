# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class WallpicspiderPipeline(object):

    def __init__(self):
        self.file = open('url.txt','w',encoding='utf8')

    def process_item(self, item, spider):
        print("打印图片地址%s"%item['url'])
        self.file.write(item['url']+'\n')
        return item

    def close_spider(self):
        self.file.close()