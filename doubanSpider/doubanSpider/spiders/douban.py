# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        res1 = response.xpath("//ol[@class='grid_view']//span[@class='title']/text()")
        print("输出"+res1)
