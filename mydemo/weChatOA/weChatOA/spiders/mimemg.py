# -*- coding: utf-8 -*-
__author__ = "Mini_OK"
import scrapy
from weChatOA.items import WechatoaItem
import time


class MimemgSpider(scrapy.Spider):
    name = 'mimemg'
    allowed_domains = ['mp.weixin.qq.com']
    start_urls = ["https://mp.weixin.qq.com/s?__"
                  "biz=MjM5MDQ4MzU5NQ==&mid=2658990781&idx=1&"
                  "sn=1df1b8a30b8b07464af3df6f4f4ebd3d&"
                  "chksm=bdcc4f598abbc64f059900e48c1d7fc54252a628c1f2a74e5d89795af8f31431bccdda02c344&"
                  "scene=21&token=1227810139&lang=zh_CN#wechat_redirect"]

    def parse(self, response):
        item = WechatoaItem()

        post_user = response.xpath('//*[@id="meta_content"]/a')
        item['source'] = post_user.xpath('text()').extract()[0]
        # item['inputtime'] = time.strftime(time.localtime(time.time()))
        item['is_delete'] = 0
        for sel in response.xpath('//*[@id="js_content"]/section[5]/section/section/span/a'):
            item['link'] = sel.xpath('@href').extract()[0]
            item['title'] = sel.xpath('text()').extract()[0]
        yield item
