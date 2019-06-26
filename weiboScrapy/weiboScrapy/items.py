# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field, Item


class WeiboscrapyItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user = Field()  # 博主 url
    content = Field()  # 微博的内容
    support_number = Field()  # 点赞人数
    transpond_number = Field()  # 转发人数
    comment_number = Field()  # 评论人数
    date = Field()  # 日期
    observer = Field()  # 该微博对应的所有评论


class Fan(Item):
    user = Field()
    content = Field()
