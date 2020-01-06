# -*- coding: utf-8 -*-
import scrapy


"""
腾讯招聘--HR职位爬虫
"""
import logging
logger = logging.getLogger(__name__)
class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['careers.tencent.com']
    start_urls = ['https://careers.tencent.com/search.html?pcid=40008']

    def parse(self, response):
        logger.warning(response.body.decode("UTF-8"))
        #hr_list = response.xpath("//div[@class='search-list']")
        hr_list = response.xpath("//div[@class='search-content']")
        logger.warning(hr_list)
        for hr in hr_list:
            item = {}
            item["title"] = hr.xpath(".//h4[@class='recruit-title']/text()")
            #item["address"] = hr.xpath()
            #item["requirement"] = hr.xpath()
            yield item

