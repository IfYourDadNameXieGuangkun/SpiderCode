# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanspiderItem(scrapy.Item):

    name = scrapy.Field()#中文名称
    name_en = scrapy.Field()#英文名称
    director = scrapy.Field()#导演
    actor = scrapy.Field()#主演
    pic = scrapy.Field()#图片
    grade = scrapy.Field()#评分
    count = scrapy.Field()#评价人数
    impression = scrapy.Field()#印象
    time = scrapy.Field()#时间
    country = scrapy.Field()#国家
    content = scrapy.Field()#内容/剧情


