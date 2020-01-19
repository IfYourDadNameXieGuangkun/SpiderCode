# -*- coding: utf-8 -*-
import scrapy
from dmozSpider.items import DmozspiderItem


class DmozSpider(scrapy.Spider):
    name = 'dmoz'
    allowed_domains = ['www.dmozdir.org/']
    start_urls = ['http://www.dmozdir.org/Goin.asp']

    '''
    1.爬取当前页面上的数据
    '''
    # def parse(self, response):
    #     li_list = response.xpath("//ul[@class='listitem']/li")
    #     for li in li_list:
    #         item = DmozspiderItem()
    #         item['name'] = li.xpath('./h4/@title').extract_first()
    #         item['detail_link'] = li.xpath('./h4/a/@href').extract_first()
    #         item['desc'] = li.xpath('./p/text()').extract_first()
    #         item['same_link'] = li.xpath('./address/a/@href').extract_first()
    #         yield item


    '''
    2.爬取二级页面上的数据
    '''

    def parse(self, response):
        try:
            if response.status==403:
                page_num = response.url.split('=')[-1]
                page_index = response.url.split('=')[-2]
                next_url = page_index+"="+str(int(page_num)+1)
            else:
                next = response.xpath("//div[@class='PageNumbers']/a[@title='下一页']/@href").extract_first()
                next_url = response.urljoin(next)

            yield scrapy.Request(next_url,callback=self.parse,dont_filter=True)
            yield scrapy.Request(next_url,callback=self.prase_all,dont_filter=True)
        except Exception:
            page_num = response.url.split('=')[-1]
            page_index = response.url.split('=')[-2]
            next_url = page_index + "=" + str(int(page_num) + 1)
            yield scrapy.Request(next_url, callback=self.parse, dont_filter=True)


    def prase_all(self,response):
            li_list = response.xpath("//ul[@class='listitem']/li")
            for li in li_list:
                item = DmozspiderItem()
                item['name'] = li.xpath('./h4/@title').extract_first()
                item['detail_link'] = li.xpath('./h4/a/@href').extract_first()
                item['desc'] = li.xpath('./p/text()').extract_first()
                item['same_link'] = li.xpath('./address/a/@href').extract_first()
                yield item




