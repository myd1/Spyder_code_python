# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 10:58:58 2018

@author: Administrator
"""

#coding:utf-8 
import urllib 
import re 
file = open("H:\\02py-code\\Spyder-code\\qqcom1.txt","w+") 
url = "http://tieba.baidu.com/p/5858458304?pn=" 
def get_ye(url): 
    html = urllib.request.urlopen(url).read() 
    html=html.decode('utf-8')#python3
    reyuan = r'<a href=".*?pn=(.*?)">尾页</a>' 
    recom = re.compile(reyuan) 
    refind = re.findall(recom,html) 
    return refind[0] 
def get_qq(): 
    i = 1 
    j = 1 
    while i<=int(get_ye(url)): 
        content = urllib.request.urlopen(url+str(i)).read() 
        content=content.decode('utf-8')#python3
        print("现在在下载第"+str(i)+"页，总共"+str(get_ye(url)) +"页") 
        i += 1 
        pattern = u'微信[\w,-]{1,20}'  #关于微信号正则表达式匹配
        items =re.findall(pattern,content) 
        print(items)
        for item in items: 
            file.write(item+ '\n') 
        j += 1 
    else: 
        print ("结束") 
        file.write(str(j)+ '\n') 
        print (j) 
        file.close() 
if __name__=="__main__": 
    get_qq()
