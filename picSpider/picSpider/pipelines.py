# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
logger = logging.getLogger(__name__)

class PicspiderPipeline(object):
    def process_item(self, item, spider):
        # 需要开启pipline
        #name = item['name']

        #logger.warning('PicspiderPipeline')
        #logger.warning(item)
        return item

class PicspiderPipeline1(object):
    def process_item(self, item, spider):
        #需要开启pipline
        #name = item['name']
        pic = dict(item)
        name = pic['name']
        print(name)
        #logger.warning("PicspiderPipeline111:{}",name)
        #logger.warning(item)
        return item
