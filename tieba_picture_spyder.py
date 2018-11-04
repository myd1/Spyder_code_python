# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 10:19:45 2018

@author: Administrator
"""
#coding:utf-8
import urllib #urllib提供了一系列用于操作URL的功能
import re

def get_html(url):
    page = urllib.request.urlopen('http://tieba.baidu.com/p/1753935195')
    html = page.read()
    html=html.decode('utf-8')#python3
    return html

reg = r'src="(.+?\.jpg)" width'#正则表达式
reg_img = re.compile(reg)#编译一下，运行更快
imglist = reg_img.findall(get_html('http://tieba.baidu.com/p/1753935195'))#进行匹配
x=0
for img in imglist:
   urllib.request.urlretrieve(img,'H:\\02py-code\\Spyder-code\\picture\\%s.jpg' %x)
   x+=1

