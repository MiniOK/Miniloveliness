import requests
import re

# 摘自博客   https://blog.csdn.net/qq_27302597/article/details/79411808


def get_521_content():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    }

    req = requests.get(
        "https://www.seebug.org/vuldb/ssvid-92666",
        headers=headers)
    cookies = req.cookies
    print(cookies)

    cookies = ';'.join(['='.join(item) for item in cookies.items()])
    print(cookies)
    txt_521 = req.text
    txt_521 = ",".join(re.findall('<script>(,*?)</script>', txt_521))
    return (txt_521, cookies)


if __name__ == '__main__':
    get_521_content()
