# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class TestpipelinePipeline(object):
    def process_item(self, item, spider):
        # if item["come_from"] == "itcast1":
        #     pass
        # elif item["com_from"] == "itcast2":
        #     pass

        if spider.name == "itcast1":
            pass
        elif spider.name == "itcast2":
            pass
        return item
