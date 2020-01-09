# -*- coding: utf-8 -*-
import scrapy
from doubanSpider.items import DoubanspiderItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    #start_urls = ['https://movie.douban.com/top250']
    #start_urls = ['https://accounts.douban.com/passport/login']
    base_url = "https://movie.douban.com/top250?start={}"
    page = 0


    # # def parse(self, response):
    # #     pic_list = response.xpath("//ol[@class='grid_view']/li/div/div[@class='pic']")
    # #     #info_list = response.xpath("//ol[@class='grid_view']/li/div/div[@class='info']")
    # #
    # #
    # #     #循环遍历图片以及详细地址
    # #
    # #     for pic_ in pic_list:
    # #         #print(pic_.xpath("./em/text()"))
    # #         print(pic_.xpath("//a/@href").extract_first())
    # #         if 'login' in pic_.xpath("//a/@href").extract_first():
    # #             self.login(response)
    # #         print('\n')
    # #         #print(pic_.xpath("//a/@href"))
    # #     """
    # #     进行后续分页查询
    # #     """
    #
    def start_requests(self):

        return [scrapy.FormRequest("https://accounts.douban.com/",meta={"cookiejar":1},callback=self.parse_before_login)]


    def parse_before_login(self,response):
        #print("登录前表单填充")
        #print(response.body.decode("UTF-8"))
        return scrapy.FormRequest(
            url='https://accounts.douban.com/j/mobile/login/basic',
            method='POST',  # 指定访问方式
            formdata={
                'ck': '',
                'name': '13135699022',
                'password': 'money4761425',
                'remember': 'false',
                'ticket': ''
            },
            meta={'cookiejar': response.meta['cookiejar']},
            dont_filter=True,  # 不进行去重处理
            callback=self.parse_after_login
        )


    def parse_after_login(self, response):
            print(response.meta['cookiejar'])
            #print(response.body.decode("UTF-8"))
            page = self.page*25
            if page<=225:
                url = self.base_url.format(page)
                yield scrapy.Request(url=url, meta={'cookiejar':response.meta['cookiejar']},callback=self.parse_item,dont_filter=True)


    def parse_item(self,response):
        pic_list = response.xpath("//ol[@class='grid_view']/li/div/div[@class='pic']")
        #info_list = response.xpath("//ol[@class='grid_view']/li/div/div[@class='info']")
        #print(pic_list)


        #循环遍历图片以及详细地址

        for pic_ in pic_list:
            #print(pic_.xpath("./em/text()"))
            print(pic_.xpath("a/@href").extract_first())
            #pic_css_list = pic_.css("a::attr(href)").extract()[0]
            #print(pic_css_list)

        """
        进行后续分页查询
        """











