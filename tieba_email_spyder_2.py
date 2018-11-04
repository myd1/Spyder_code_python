# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 13:53:16 2018

@author: Administrator
"""

import  requests
import datetime
import re
def get_email(url):
    content = requests.get(url).text
    pattern = r'[0-9a-zA-Z._]+@[0-9a-zA-Z._]+\.[0-9a-zA-Z._]+' #正则表达式判断邮箱
    p = re.compile(pattern)
    m = p.findall(content)
    email = list(set(m)) #去掉重复邮箱
    count = 0 #邮箱计数
    for mm in  email:
        count = count+1
        print(mm)
    return  count
n = 1  # 页数
amount = 0  # 邮箱计数
start_time = datetime.datetime.now()  # 开始时间
while n <= 10:
    amount = amount + get_email('https://tieba.baidu.com/p/3349997454?pn=' + str(n))
    n = n + 1
end_time = datetime.datetime.now()  # 结束时间
print('获取了' + str(amount) + '个邮箱')
print(str((end_time - start_time).seconds) + '秒')