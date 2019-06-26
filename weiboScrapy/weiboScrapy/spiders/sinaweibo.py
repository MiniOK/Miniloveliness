# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from weiboScrapy.items import WeiboscrapyItem, Fan


class SinaweiboSpider(scrapy.Spider):
    """
    微博是个需要用户验证的网站，所以 cookie 和 header 是一定要配置的
    获取这个很简单，打开 chrome，按下 F12，输入网址：weibo.com。
    然后登陆你的账号，选中工具栏中的 network，这时候你在右边的工具栏中发现所需的条目
    """
    name = 'sinaweibo'
    allowed_domains = ['weibo.com']
    start_urls = ['http://weibo.com/']

    def __init__(self):
        self.cookie = {'_T_WM': 'c2f229efc05784054394e41b6445a61b',
                       'SCF': 'Akr9hguT2JWcdhKSTRaClyatnlQEwrE3E4oDA7QOKf-NATrmqcIO4GhB2IpGQz1PSyYsBz3vjlbFvHNjyYqnkjM.',
                       'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9W5WavXZSGh-flM42rmNd2CH5JpX5K-hUgL.FoqESKMX1K2f1K-2dJLoIEy_Ig4Di--Ri-i8i-20i--fiK.0i-2ci--Ri-zXiKL2i--Ri-zXiKL2',
                       'SUB': '_2A25wFZYnDeRhGeBM7lUV-S_JwjmIHXVT-TpvrDV6PUJbkdAKLRjzkW1NRK0U5yeV4tuMWa7YXXy-0hn7udgaGXWO',
                       'SUHB': '03oFH9YAaoobvM', 'SSOLoginState': '1561454198'}
        self.header = {
            'Referer': 'https://weibo.cn/'
        }

    def start_requests(self):
        return [Request("https://weibo.cn/6257491595/", callback=self.parse,
                        cookies=self.cookie, headers=self.header)]

    def parse(self, response):
        weibo_item = WeiboscrapyItem()
        # 获取所有类名为‘c’ 的元素
        wbs = response.xpath("//div[@class = 'c']")
        weibo_item['user'] = response.url

        for i in range(len(wbs) - 2):
            comment_href = ""
            divs = wbs[i].xpaath("./div")
            weibo_item['observer'] = []
            weibo_item['content'] = divs[0].xpath(
                './span[@class = "ctt"]/text()').extract()[0]
            if len(divs) == 1:
                a = divs[0].xpath('./a')
                if len(a) > 0:
                    for j in range(len(a)):
                        weibo_item['support_number'] = a[-4].xpath(
                            './text()').extract()[0]
                        weibo_item['transpond_number'] = a[-3].xpath(
                            './text()').extract()[0]
                        weibo_item['comment_number'] = a[-2].xpath(
                            './text()').extract()
                        comment_href = a[-2].xpath('./@href').extract()[0]
                weibo_item['date'] = divs[0].xpath(
                    './span[@class="ct"]/text()').extract()[0]

            if len(divs) == 2:
                a = divs[1].xpath('./a')
                if len(a) > 0:
                    for j in range(len(a)):
                        weibo_item['support_number'] = a[-4].xpath(
                            './text()').extract()[0]
                        weibo_item['transpond_number'] = a[-3].xpath(
                            './text()').extract()[0]
                        weibo_item['comment_number'] = a[-2].xpath(
                            './text()').extract()[0]
                        comment_href = a[-2].xpath('./@href').extract()[0]
                weibo_item['date'] = divs[1].xpath(
                    './span[@class="ct"]/text()').extract()[0]
            yield Request(comment_href, meta={'item': weibo_item}, callback=self.parse_comment)

    def parse_comment(self, response):
        observer_item = Fan()
        # selector = Selector(response)
        weibo_item = response.meta['item']
        comment_list = []

        comment_records = response.xpath('//div[@class="c"]')
        for comment_record in comment_records[3:-1]:
            observer_item['user'] = comment_record.xpath(
                './a[1]/text()').extract()[0]
            try:
                observer_item['content'] = comment_record.xpath(
                    './span[@class="ctt"]').extract()[0]
            except Exception:
                observer_item['content'] = ''
            comment_list.append(dict(observer_item))

        weibo_item['observer'].extend(comment_list)

        if response.xpath(
                '//*[@id="pagelist"]/form/div/a/text()').extract()[0] == u'下页':
            next_href = response.xpath(
                '//*[@id="pagelist"]/form/div/a/@href').extract()[0]
            yield Request('https://weibo.cn' + next_href, meta={'item': weibo_item}, callback=self.parse_comment)
        else:
            yield weibo_item
