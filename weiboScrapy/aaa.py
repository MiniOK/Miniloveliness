import requests
import lxml.etree as etree

r = requests.get('https://weibo.cn/?tf=5_009')
# text = r.text
text = r.content
html = etree.HTML(text)
result = etree.tostring(html, encoding='utf-8')
print(type(html))
print(type(result))
print(result)
print(html.xpath('//body'))
