import requests
from bs4 import BeautifulSoup


def bs4():
    """BeautifulSoup"""
    link = "http://tuijian.hao123.com/finance"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    r = requests.get(link, headers=headers)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    # 使用 beautisoup 提取html 文本中需要的标签
    first_title = soup.find_all("a")

    for links in first_title:
        print(links.name, links.get_text())


def regex():
    import re
    """正则表达式

        首先，正则表达式大致分为以下几部分：
        1/  元字符
        2/  模式
        3/  函数
        4/  re 内置对象用法
        5/  分组用法
        6/  环视用法

    所有关于正则表达式的操作都使用 pyrhon 标准库中的 re 模块
    一/ 元字符
        .           匹配任意字符（不包括换行符）
        ^           匹配开始位置，多行模式下匹配每一行的开始
        $           匹配结束位置，多行模式下匹配每一行的结束
        *           匹配前一个元字符 0 到 多次
        +           匹配前一个元字符 1 到 多次
        ？          匹配一个元字符 0 到 1 次
        {m,n}       匹配前一个元字符 m 到 n 次
        \\          转移字符，跟在其后的字符将失去作为特殊元字符的含义，例如 \\。 只能匹配 .，不能再匹配任意字符
        []          字符集，一个字符的集合，可匹配其中任意一个字符
        |           逻辑表达式，或， 比如 a|b 代表可匹配 a 或者 b
        （...）     分组，默认为捕获，即被分组的内容可以被单独取出，默认每个分组有个索引，从 1 开始，按照”(“的顺序决定索引值
        \number     匹配和前面索引为 number 的分组捕获的内容一样的字符串
        \A          匹配字符串开始位置，忽略多行模式
        \Z          匹配字符串结束的位置，忽略多行模式
        \b          匹配位于单词开始或结束位置的空字符串
        \B          匹配不位于单词开始或结束位置的空字符串
        \d          匹配一个数字，相当于 [0 - 9]
        \D          匹配非数字，相当于[^0 - 9]
        \s          匹配任意空白字符，相当于[\t\n\r\f\v]
        \S          匹配非空白字符，相当于[^\t\n\r\f\v]
        \w          匹配数字/字母/下划线中任意一个字符，相当于[a-zA-Z0-9]
        \W          匹配非数字，字母，下划线中的任意字符，相当于[^a-zA-Z0-9]


    """
    link = "http://tuijian.hao123.com/finance"
    headers = {
        # 'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    }
    # 发起请求
    r = requests.get(link, headers=headers)
    # 获取返回页面的 html 文本
    html = r.text
    # 使用正则表达式提取html文本中的需要的内容
    title_list = re.findall("href='.*?'.<a>(.*?)</a>", html)
    print(title_list)


def lxml_paser():
    """pyhton 爬虫 lxml 解析实战

    xpath 常用规则
        /                   从当前节点选取直接子节点
        //                  从当前节点获取子孙节点
        .                   选取当前节点
        ..                  选取当前节点的父节点
        @                   选取属性
        *                   通配符，选择所有元素节点与元素名
        @*                  选取所有属性
        [@attrib]           选取具有给定属性的所有元素
        [@attrib='value']   选取给定属性具有给定值的所有元素
        [tag]               选取所有具有指定元素的直接子节点
        [tag='text']        选取所有指定元素并且文本内容是text节点

    """
    from lxml import etree

    # 请求头设置
    headers = {
        "User-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
        "Referer": "https://movie.douban.com",
    }

    url = "https://movie.douban.com/cinema/nowplaying/chongqing"

    # 发起请求
    req = requests.get(url, headers=headers)
    text = req.text

    # 转换成 html 格式
    html = etree.HTML(text)
    print("html", html)
    # 找到子孙节点 ul 标签
    ul = html.xpath("//ul[@class = 'lists']")[0]

    lis = ul.xpath('./li')

    movies = []
    # 循环每个 li 标签
    for li in lis:
        # 直接 @li 标签的属性获取值
        title = li.xpath('@data-title')
        score = li.xpath('@data-score')
        region = li.xpath('@data-region')
        director = li.xpath('@data-director')
        liimg = li.xpath('.//img/@src')
        movie = {
            'title': title,
            'score': score,
            'region': region,
            'director': director,
            'liimg': liimg,
        }
        movies.append(movie)
        print(movie)


if __name__ == '__main__':
    lxml_paser()
