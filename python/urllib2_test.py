#!/usr/bin/env python
#coding=gbk
#coding=utf-8
#-*- coding: UTF-8 -*- 

#导入urllib2模块,并以之打开URL资源,再以read读取,并交之存到文件
import urllib2
response = urllib2.urlopen('http://www.baidu.com')
html = response.read()
print html
f = open(r'g:\watt\test\url_text.html','a')
f.write(html)
f.close()