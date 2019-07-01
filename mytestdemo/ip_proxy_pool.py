import requests
from multiprocessing import Pool
import time
from lxml import etree

proxies = []
urls = ["https://www.xicidaili.com/nn/{}".format(i) for i in range(1, 1000)]


def test_ip(proxy):
    """检测 ip 的高可用 低延迟"""

    url = "http://www.baidu.com"
    try:
        res = requests.get(url, timeout=3, proxies={'http': proxy})
        if res.status_code != 200:
            print(proxy)
        else:
            print(proxy + "          ok")
            with open('ip_pool.csv', 'a', encoding='utf-8') as f:
                f.write(proxy + '\n')
    except BaseException:
        print(proxy + "     timeout")


def get_ip(url):
    print(url)
    """获取 ip"""
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"

    }
    # 获取 html 文本

    html = etree.HTML(requests.get(url, headers=header).text)
    print(html)
    ips = html.xpath('//tr[@class = "odd"]/td[2]/text()')
    ports = html.xpath('//tr[@class = "odd"]/td[3]/text()')
    for ip, port in zip(ips, ports):
        proxy = ip + ":" + port
        # print(ip + ":" + port)
        proxies.append(proxy)


if __name__ == '__main__':
    for url in urls:
        get_ip(url)
        pool = Pool(processes=8)
        pool.map(test_ip, proxies)
        time.sleep(3)
