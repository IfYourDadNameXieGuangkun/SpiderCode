# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymongo
class DmozspiderPipeline(object):
    def __init__(self):
        self.file = open('item.jl','w',encoding='utf-8')
    def process_item(self, item, spider):
        #print(item)
        line = json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.file.write(line)
        return item



class MongoPipeline(object):
    collection_item = 'scrapy_item'

    def __init__(self,mongo_url,mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    @classmethod
    def from_crwal(cls,crawler):
        return cls(
            mongo_url=crawler.settings.get("MONGO_URL"),
            mongo_db=crawler.setting.get("MONGO_DATABASE",'item')
        )

