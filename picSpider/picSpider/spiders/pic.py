# -*- coding: utf-8 -*-
import scrapy
import logging
from picSpider.items import PicspiderItem
logger = logging.getLogger(__name__)

class PicSpider(scrapy.Spider):
    name = 'pic'
    allowed_domains = ['ivsky.com']
    #start_urls = ['https://www.ivsky.com/search.php?q={}'.format("狗")]
    start_urls = ['https://www.ivsky.com/tupian/katongchangjing_t19606/',]

    def parse(self, response):
        #logger.warning(response.body.decode("UTF-8"))
        img_list = response.xpath("//div[@class='il_img']/a/img")
        print(img_list)
        items = []
        for img in img_list:
            item = PicspiderItem()
            # image = img.xpath("@src").extract_first()
            # name = img.xpath("@alt").extract_first()
            item["name"] = img.xpath("@alt").extract_first()
            item["image_url"] = img.xpath("@src").extract_first()
            items.append(item)
            yield item
