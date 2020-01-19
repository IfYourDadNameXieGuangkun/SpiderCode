# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DmozspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    detail_link = scrapy.Field()
    desc = scrapy.Field()
    same_link = scrapy.Field()
