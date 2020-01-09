# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WallpicspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 可以定义>=1个字段,我现在只需要图片的url
    url = scrapy.Field()

