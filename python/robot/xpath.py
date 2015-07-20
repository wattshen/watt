#!/usr/bin/env python
#coding: utf-8
#-*-*-  Author: Wattshen       -*-*-
#-*-*-  Email:34665115@qq.com  -*-*-
#-*-*-  Filename:xpath.py  -*-*-
#-*-*-  Date:
#Content:

from lxml import etree
import urllib2

url = 'http://www.sohu.com'

def getHtml(url):
	page = urllib2.urlopen(url)
	html = page.read()
	return html
html = getHtml(url)


'''
html =
<html>
<head><title>123<title></head>
<body>
<div id = "asd">
<ul>
<li>di yi hang</li>
<li>di er hang</li>
</ul>
</div>
</body>
</html>
'''

selector = etree.HTML(html)

content = selector.xpath('//div/li/a/@href')
for a in content:
	print a

print content