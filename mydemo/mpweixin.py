#!/usr/bin/env python 
# -*- coding:utf-8 -*-

_author_ = "Mini_OK"

from selenium import webdriver
import time
from lxml import etree
from pyquery import PyQuery as pq
import re


class Crawling:
    """                                               ------------------爬取客户端微信公众号-------------------
    1、首先登陆微信（电脑，手机端都可以，Charles也可以抓取手机端的接口，不过需要设置，推荐登陆电脑客户端微信）点击订阅号，点进去需要爬取的微信公众号。
    """

    def __init__(self):
        """使用 Charles 抓包工具进行抓取公众号的 url， 只要Charles 一关闭 url就会失效 不知道为什么会这样 有待考察"""

        # self.url = "https://mp.weixin.qq.com/mp/getmasssendmsg?__biz=MjM5MDc4NjY0MA==&uin=ODUzMDYzNzE3&key=fcd3044b76e22d08a90399cef040db4e16426fa42508f1e8b2469ea1a6809763a61da265d628a82ca8d7df109a957dd77a756bbb7a563f4872595888da9bfade1473e45ce216c477a7a994071d81e5aa&devicetype=Windows+7&version=62060833&lang=zh_CN&ascene=7&pass_ticket=T03uPB3LV1SOPws3oAcVrZ%2F9AB7eGwPMtYBkecmqWOFAwDlaGtNWn2DM37HCZ4hz"

        self.url = "https://mp.weixin.qq.com/mp/getmasssendmsg?__biz=MjM5MDc4NjY0MA==&uin=ODUzMDYzNzE3&key=49a6b6e526a2abae8074afb6c3f64d3e3bb461a4a42d5d637293ef9add3c15594f146412a6f7d6793b002fccce838caca33c90cc06fcb41fe94eed2704e6c14bfe5469cfc8a0c1e2b0b25b016072c697&devicetype=Windows+7&version=62060833&lang=zh_CN&ascene=7&pass_ticket=j%2BHbFcl86BG4XfbCGBnT4XjX9ay88ysBKY5RaAPH2oum2P3kgxZ0fdVTLeOnN9CI"
        # 此处着重强调 下面的url是上面的 url 粘到浏览器中转换过来的 在浏览器中显示正常 但是在这就回打不开页面  先保留这个问题
        # self.url = "https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MjM5MDc4NjY0MA==&scene=124&#wechat_redirect"

        self.opt = webdriver.ChromeOptions()
        # # 设置headers
        # opt.add_argument('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36')
        self.driver = webdriver.Chrome(options=self.opt)
        self.driver.get(self.url)

        # print(driver.page_source)
        # 构造一个XPath解析对象并对 HTML 文本进行自动修正
        self.html = etree.HTML(self.driver.page_source)
        # 输出修正后的结果，类型是 bytes
        self.result = etree.tostring(self.html)
        # print(result)
        # print(result.decode("utf-8"))

    def down_move(self):
        """模拟下滑"""
        # 将滚动条移动到页面的底部
        js = "var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script(js)
        time.sleep(3)
        # # 将滚动条移动到页面的顶部
        # js = "var q=document.documentElement.scrollTop=0"
        # self.driver.execute_script(js)
        # time.sleep(3)
        # # 若要对页面中的内嵌窗口中的滚动条进行操作，要先定位到该内嵌窗口，在进行滚动条操作
        # js = "var q=document.getElementById('id').scrollTop=100000"
        # self.driver.execute_script(js)
        # time.sleep(3)

    def extract_link(self):
        """提取标题和链接"""
        # 提取所有的标题
        ress = self.html.xpath("//h4/text()")
        # 提取所有的链接
        res = self.html.xpath("//h4/@hrefs")
        return ress, res
        # return list(zip(ress, res))

    def open_a_url(self):
        """ 打开每一个链接的文章"""

        _, res = self.extract_link()  # 只需要链接 标题忽略
        for urli in res:
            self.driver.get(urli)
            time.sleep(3)

    def write_json(self):
        ress, res = self.extract_link()
        time.sleep(3)
        self.open_a_url()
        with open("aother.json", "w+") as fp:
            for (item1, item2) in list(zip(ress, res)):
                # ''.join() 是 tuple 转 str
                # print("(", flag, ")", "".join(item).strip())

                # 写入文件
                fp.write("".join(item1).strip() + '\n')
                fp.write("".join(item2).strip() + '\n')


if __name__ == '__main__':
    crawl = Crawling()
    # l = []

    # 控制浏览器模拟下滑的过程 使用了循环才下滑的效果明显
    # for i in range(1, 5):
    #     crawl.down_move()
    #     # 每下滑一页 将当前页的数据获取出来 添加到列表中 （想的太天真 并没有实现这一想法）
    #     l.append(crawl.extract_link())
    #     time.sleep(3)
    #
    # for i in l:
    #     print(i)
    # crawl.write_json()
    crawl.write_json()
