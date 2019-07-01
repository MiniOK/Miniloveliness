import json

# json.dumps()  # 将 python 对象编码成 json 字符串
# json.loads()  # 将 json 字符串解码为 Python 对象

# data = [{'a': 1, 'b': 2, 'c': 3, 'e': 4, 'f': 5}]

# json = json.dumps(data)
# print(json)

# dumps 将python解码为json
# json = json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))
# print(json)

# loads 将json 解码为 python

jsondata = "{'a':1}"
# jsondata = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
text = json.loads(jsondata)
print(text)
