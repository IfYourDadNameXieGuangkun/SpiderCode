# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['wallhaven.cc']
    start_urls = ['http://wallhaven.cc/']

    def parse(self, response):
        pass
