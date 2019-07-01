"""
练习异常的执行

"""

html = None


# html.xpath() # 执行此句时出现以下异常

# Traceback (most recent call last):
#   File "D:/pyCharmProject/minidemo/error_test.py", line 7, in <module>
#     html.xpath()
# AttributeError: 'NoneType' object has no attribute 'xpath'



# 捕获异常 程序继续往下执行
try:
    html.xpath()
except AttributeError as e:
    print(e)


print('————————程序继续执行——————————')