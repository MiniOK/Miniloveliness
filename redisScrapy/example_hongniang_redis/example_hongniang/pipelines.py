# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

"""
一般我们使用 open() 打开文件就 ok了，但是我们爬虫或者其他方式得到一些数据时
会有编码不统一的问题，所以就统一转换为 unicode。此时写入 open方式打开的文件就有问题了

怎么办，我们将编码变成 str 类型，但是太麻烦了，我们要把得到的东西先 decode 为 unicode
再encode为str

当然，代替者繁琐操作的就是 codecs.open()
"""

import codecs
import json


class ExampleHongniangPipeline(object):
    def __init__(self):
        self.file = codecs.open(filename='zhongguohongniang.csv', mode='w+', encoding='utf-8')

    def process_item(self, item, spider):
        res = dict(item)
        # 如果直接将字典形式数据写入文件，会发生错误
        # 所以需要将字典形式的值，转换成字符串，写入文件中
        json_str = json.dumps(res, ensure_ascii=False)
        self.file.write(json_str)
        self.file.write('.\n')

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.file.close()
