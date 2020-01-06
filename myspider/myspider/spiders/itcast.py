# -*- coding: utf-8 -*-
import scrapy

"""
scrapy genspider itcast itcast.cn

"""
class ItcastSpider(scrapy.Spider):
    name = 'itcast' #爬虫名称-->对应命令中的参数 itcast
    allowed_domains = ['itcast.cn'] #允许爬取的范围-->对应命令中的参数 itcast.cn
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml'] #最开始请求的url地址,自动生成的,需要修改成我们需要爬取网站

    def parse(self, response):
        print(response)
        #处理start_urls地址对应的响应
        #res1 = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        #print("----------"+res1)
