# -*- coding: utf-8 -*-
import scrapy
from doubanSpider.items import DoubanspiderItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        pic_list = response.xpath("//ol[@class='grid_view']/li/div/div[@class='pic']")
        info_list = response.xpath("//ol[@class='grid_view']/li/div/div[@class='info']")
        print(pic_list[0])
        print(info_list[0])

        """
        进行后续分页查询
        """

