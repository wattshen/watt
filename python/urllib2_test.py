#!/usr/bin/env python
#coding=gbk
#coding=utf-8
#-*- coding: UTF-8 -*- 

#����urllib2ģ��,����֮��URL��Դ,����read��ȡ,����֮�浽�ļ�
import urllib2
response = urllib2.urlopen('http://www.baidu.com')
html = response.read()
print html
f = open(r'g:\watt\test\url_text.html','a')
f.write(html)
f.close()