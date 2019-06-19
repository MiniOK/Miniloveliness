#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
import time
import json

"""爬取微信公众号"""
# 目标 url
url = "https://mp.weixin.qq.com/cgi-bin/appmsg"

# 使用cookie 跳过登陆操作
headers = {
    "cookie": "pgv_pvid=3935696216; pgv_pvi=7815173120; RK=IV7gdI2BO1; ptcz=c251e84a0e5ac630c67db3370967b36339d81f0dd28d4149ffca84f97b5038ea; cuid=6214388916; o_cookie=549975935; pac_uid=1_549975935; tvfe_boss_uuid=e88a9a55a8555a05; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2257ce3b076d1348819922d45a8b00e77a%22%2C%22%24device_id%22%3A%22166b3e72cce2f8-0e0dbe0b0d0b64-4c734611-2073600-166b3e72ccf353%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22_latest_ADTAG%22%3A%22sidebar%22%7D%7D; mobileUV=1_168bbb22031_13d58; gid=3fc9d006-f602-4920-8463-06457574a6e7; ua_id=vunVHym3U1JtJ9moAAAAALRJEIrzyk6QQTGPsge49uc=; pgv_info=ssid=s2675506840; _ga=GA1.2.376737519.1560927388; _gid=GA1.2.2092196920.1560927388; noticeLoginFlag=1; remember_acct=549975935%40qq.com; mm_lang=zh_CN; pgv_si=s4117214208; cert=niUJAJ13TmvG8XkrsufCnWpWM9fcvw2I; sig=h017725c4b32db1de5cd9c4999806d3b81515cf62959a8ac7f4a85612a04aa669dde27470da6f645d7c; uuid=9fd9b903800f6b26a55f626b32131922; bizuin=3899248551; ticket=6ac5ad5d70defea80c3abf0b67fdacf1c0daa09f; ticket_id=gh_2578037faf50; data_bizuin=3899248551; data_ticket=oCqHFn2UbxBhE1dHXnILDdnbZ+r3ZRoWsp2BXy8n+1akqgB5xwG9TCkgyh6P7hDr; slave_sid=SWRmcHVCMmlxU2xWOVd5Slh0T3RQNzZGSDZCMHRaQUhtQ1RGQ2p5bkJTejZzbldxOUJjUWZvTlM2WHltOHY3QjMwSHl2alIxVXNZZ2ZURjl4em1McnE5elFodlBSdG5NNXZUTHVVMzZLMWF5Y2dGT25GeEUyUFo4NTBWU0h1NEdDV1B5dHdYRk9KQ21TYng5; slave_user=gh_2578037faf50; xid=698c386cd738097246132e3f72b1c7c8; openid2ticket_op89p6GF0jI9BSSL5hxiiQ8jF_Jo=OEnKCj39K7xks89VxToN3tHddNai+WDuv6croPuNt9E=",

    # "cookie":"slave_user=gh_2578037faf50; Path=/; Secure; HttpOnly",
    # "cookie":"slave_sid=SWRmcHVCMmlxU2xWOVd5Slh0T3RQNzZGSDZCMHRaQUhtQ1RGQ2p5bkJTejZzbldxOUJjUWZvTlM2WHltOHY3QjMwSHl2alIxVXNZZ2ZURjl4em1McnE5elFodlBSdG5NNXZUTHVVMzZLMWF5Y2dGT25GeEUyUFo4NTBWU0h1NEdDV1B5dHdYRk9KQ21TYng5; Path=/; Secure; HttpOnly",

    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3704.400 QQBrowser/10.4.3587.400"
}

"""
需要提交的data
以下个别字段是否一定需要还未验证
注意修改 yourtoken， number
number 表示从 number 页开始爬取，为 5 的倍数， 从 0 开始，例如 0/5/10
token 可以使用 Chrome 自带的工具进行获取
fakeid 是公众号独一无二的一个 id，等同于后面的 __biz
"""

data = {
    # "t": "media/appmsg_edit_v2",
    # "action": "edit",
    # "token": "1815541067",
    # "lang": "zh_CN",
    # "f": "json",
    # "ajax": "1",
    # "random": "0.2823096857992018",
    # "query":"科技美学",
    # "fakeid": "MjM5MDQ4MzU5NQ==",  # 伪造id
    # "begin": "0",
    # "count": "5",

    "token": "1815541067",
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1",
    "random": "0.7497681226366124",
    "action": "list_ex",
    "begin": "0",
    "count": "5",
    "query": "",
    "fakeid": "MjM5MDQ4MzU5NQ==",
    "type": "9",

    # "token": "1815541067",  # 标记
    # "lang": "zh_CN",
    # "f": "json",
    # "ajax": "1",
    # "action": "search_biz",
    # "begin": "0",
    # "count": "5",
    # "random":"0.2823096857992018",
    # # "query": "",
    # "fakeid": "MjM5MDQ4MzU5NQ==",  # 伪造id
    # "type": "9",
}

# 使用 get 方法进行提交
content_json = requests.get(url, headers=headers, params=data).json()
# 返回了一个 json，里面是每一页的信息
print(content_json)
print(type(content_json))

for item in content_json["app_msg_list"]:
    print(item["title"], "url", item["link"])
