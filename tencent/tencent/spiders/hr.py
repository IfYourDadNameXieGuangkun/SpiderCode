# -*- coding: utf-8 -*-
import scrapy


"""
腾讯招聘--HR职位爬虫
"""
import logging
logger = logging.getLogger(__name__)
class HrSpider(scrapy.Spider):
    # name = 'hr'
    # allowed_domains = ['careers.tencent.com']
    # start_urls = ['https://careers.tencent.com/jobopportunity.html']
    #
    # def parse(self, response):
    #     logger.warning(response.body.decode("UTF-8"))
    #     #hr_list = response.xpath("//div[@class='search-list']")
    #     hr_list = response.xpath("//div[@class='search-content']")
    #     logger.warning(hr_list)
    #     for hr in hr_list:
    #         item = {}
    #         item["title"] = hr.xpath(".//h4[@class='recruit-title']/text()")
    #         #item["address"] = hr.xpath()
    #         #item["requirement"] = hr.xpath()
    #         yield item

    name = 'hr'
    allowed_domains = ['careers.tencent.com']

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Referer": "https://careers.tencent.com/jobopportunity.html"
    }

