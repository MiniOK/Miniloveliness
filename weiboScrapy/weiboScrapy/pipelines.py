# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


class WeiboscrapyPipeline(object):

    def __init__(self):
        self.f = open('result.txt', "a+")

    def process_item(self, item, spider):
        line = json.dumps(dict(item) + '\n')
        self.f.write(line)
        return item

    def close_spider(self):
        self.f.close()
