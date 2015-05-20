#!/usr/bin/env python
#coding: utf-8 
#Author: Wattshen
#Email:34665115@qq.com
#Date:2015年5月16日
#Filename:tiquurl.py
#Content:提取远程HTML页面包含的链出URL

#导入urllib2模块,并以之打开URL资源,再以read读取,并将之存到文件

import urllib2
import re

page_url = 'http://www.qq.com'

#获取页面内容
def getHtml(url):
	page = urllib2.urlopen(url)
	html = page.read()
	return html

#提取页面a标签内的链接地址
def getLink(html):
	link = []
	#pat = '<a.*?href="([^"]*)".*?>([\S\s]*?)</a>'
	pat = 'href\s*=\s*\"((https?://)?.+?)\"'
	#pat = 'href=\"(.+?)\"'#https?一段加与不加意义不大
	link = re.findall(pat, html)
	return link

#函数调用
htmls = getHtml(page_url)
links = getLink(htmls)
#print htmls
#print links

#将结果存储到文件，并按元素换行
f1 = open(r'file1.txt','w')
f1.write(htmls)
f1.close()

f2 = open(r'file2.txt','w')
for element in links:
	f2.write(str(element)+'\n')#存储为一行一个
#f2.write(str(links))#不换行存储
f2.close()