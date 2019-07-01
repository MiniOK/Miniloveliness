#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import requests
import time
import json

"""    
            ---------------爬取个公众平台微信公众号----------------
            1、拥有一个个人订阅号，附上登陆和注册的链接；(微信公众平台:https://mp.weixin.qq.com/)
            2、在登陆的时候单开开发者工具，提取出新的 cookie 和 token
            3、登陆之后点，点击菜单栏“管理”-“素菜管理”，再点击右侧“新建图文素材”
            4、弹出一个标签页，在上面的工具栏中找到“超链接”并点击
            5、弹出一个小窗口，选择“查找文章”，然后输入需要查找的公众号，这里是“科技美学”作为例子

"""
# 目标 url
url = "https://mp.weixin.qq.com/cgi-bin/appmsg"

# 使用cookie 跳过登陆操作 使用时记得每次都要更新 cookie

headers = {
    "cookie": "pgv_pvi=598769664; pgv_pvid=4452284528; RK=Gc7gIo2xM1; "
              "ptcz=57e2f1ebd2c89c178e903e53f0972ac26ad075b1f6886f6f9743fe51a187116d; "
              "ua_id=Qcrms1D5QH0p2LhcAAAAAGDT7ileAlnXaGnkcznOv_E=; pgv_si=s2265750528;"
              " cert=eGM_1LHigvlOi_A7_zCJUD6j4Ur7_Jpz; noticeLoginFlag=1; mm_lang=zh_CN; "
              "rewardsn=; wxtokenkey=777; uuid=1402a2bb2f08beb9eea296059e39b94f; bizuin=3899248551;"
              " ticket=eabf9b26a4a9f06c92994d23a0f7a44161be7bb9; ticket_id=gh_2578037faf50; data_bizuin=3899248551;"
              " data_ticket=iV1cZNneXt949cCd4RyBAp3tf2nk1GG7B+iX7A2KPjQ/d9l7PcDANYSVMvNbJD5Q; "
              "slave_sid=X201eWpxS0FiWUNnQU9pcTh0VTVWXzRTOTVlZXBUNldNTlZxaHVKbE1UQjEyNzI1aTNxTDVUV0h1S"
              "2IyX0tqMUZJWkdITnVyeGUxU0g3cEc5UGlDT2l6QzJhU29nNDJIRmpZbzFxamluOGVmdGFUaWFsU2VjMDd2Qk9FbE"
              "1wcW1QM25NaHA4THpDN3ROSWVq; slave_user=gh_2578037faf50; xid=f6c65b08094c19a82c3ff97ad2d406ec; "
              "openid2ticket_op89p6GF0jI9BSSL5hxiiQ8jF_Jo=H++bcHXPHVsfz25HOX3yMso5lVvHZaHah0kIsOZleEE=",

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

    "token": "1565410159",  # 未来重新爬取的时候记得换 token
    "lang": "zh_CN",
    "f": "json",
    "ajax": "1",
    "random": "0.7497681226366124",
    "action": "list_ex",
    "begin": "0",
    "count": "5",
    "query": "",
    "fakeid": "MjM5MDQ4MzU5NQ==",  # “科技美学”公众号的 fakeid
    "type": "9",

}

# 使用 get 方法进行提交
content_json = requests.get(url, headers=headers, params=data).json()
# 返回了一个 json，里面是每一页的信息
# print(content_json)
# print(type(content_json))

for item in content_json["app_msg_list"]:
    print(item["title"], "url", item["link"])
