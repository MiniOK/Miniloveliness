# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ExampleHongniangItem(Item):
    """
    中国红娘网站 女用户 简单字段
    """
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 用户名称
    nickname = Field()
    # 用户 id
    loveid = Field()
    # 用户的照片
    photos = Field()
    # 用户的年龄
    age = Field()
    # 用户的身高
    height = Field()
    # 用户是否已婚
    ismarried = Field()
    # 用户的年收入
    yearincome = Field()
    # 用户的学历
    education = Field()
    # 用户的地址
    workaddress = Field()
    # 用户的内心独白
    soliloquy = Field()
    # 用户的性别
    gender = Field()

