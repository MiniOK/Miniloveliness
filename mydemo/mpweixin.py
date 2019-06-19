#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from selenium import webdriver
import time, requests
from lxml import etree
from pyquery import PyQuery as pq
import re


# url = "https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MjM5MjAxNDM4MA==&scene=124&#wechat_redirect"
#
# opt = webdriver.ChromeOptions()
# # 设置headers
# # opt.add_argument('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.884.400 QQBrowser/9.0.2524.400')
# driver = webdriver.Chrome(options=opt)
# driver.get(url)


def main():
    b = webdriver.Chrome()
    b.get("http://baidu.com")
    time.sleep(5)
    b.quit()


if __name__ == '__main__':
    main()
