# -*- coding: utf-8 -*-
import scrapy
from wallPicSpider.items import WallpicspiderItem

class PicSpider(scrapy.Spider):
    page = 1
    name = 'pic'
    allowed_domains = ['wallhaven.cc']
    start_urls = ['https://wallhaven.cc/search?q=id%3A5&ref=fp&page={}'.format(page)]
    def parse(self, response):
        img_list = response.xpath("//div[@id='thumbs']/section/ul/li/figure/img")
        for img in img_list:
            item = WallpicspiderItem()
            url = img.xpath("@data-src").extract_first()
            item['url'] = url
            yield item
