#!/usr/bin/env python
<<<<<<< HEAD
#coding: utf-8 
#Author: Wattshen
#Email:34665115@qq.com
#Date:2015��5��16��
#Filename:tiquurl.py
#Content:��ȡԶ��HTMLҳ�����������URL

#����urllib2ģ��,����֮��URL��Դ,����read��ȡ,����֮�浽�ļ�

import urllib2
import re

page_url = 'http://www.qq.com'

#��ȡҳ������
=======
#coding:utf-8
#filename:提取远程HTML页面包含的链出URL
#date:2015年5月16日

#导入urllib2模块,并以之打开URL资源,再以read读取,并将之存到文件
import urllib2
import re

page_url = 'http://www.sina.com.cn'

#获取页面内容
>>>>>>> master
def getHtml(url):
	page = urllib2.urlopen(url)
	html = page.read()
	return html

<<<<<<< HEAD
#��ȡҳ��a��ǩ�ڵ����ӵ�ַ
=======

#提取页面a标签内的链接地址
>>>>>>> master
def getLink(html):
	link = []
	#pat = '<a.*?href="([^"]*)".*?>([\S\s]*?)</a>'
	pat = 'href\s*=\s*\"((https?://)?.+?)\"'
<<<<<<< HEAD
	#pat = 'href=\"(.+?)\"'#https?һ�μ��벻�����岻��
	link = re.findall(pat, html)
	return link

#��������
htmls = getHtml(page_url)
links = getLink(htmls)
#print htmls
#print links

#������洢���ļ�������Ԫ�ػ���
f1 = open(r'file1.txt','w')
f1.write(htmls)
f1.close()

f2 = open(r'file2.txt','w')
for element in links:
	f2.write(str(element)+'\n')#�洢Ϊһ��һ��
#f2.write(str(links))#�����д洢
f2.close()
=======
	#pat = 'href=\"(.+?)\"'#https?一段加与不加意义不大
	link = re.findall(pat, html)
	return link

#提取页面所有title的内容
def getTitle(html):
	title = []
	pat = "<title>(.+?)</title>"
	title = re.findall(pat, html)
	return title



#函数调用
htmls = getHtml(page_url)
links = getLink(htmls)
title = getTitle(htmls)
#print htmls
#print links
for x in title:
	print x


#将结果存储到文件，并按元素换行
f1 = open(r'G:\watt\python\robot\file1.txt','w')
f1.write(htmls)
f1.close()

f2 = open(r'G:\watt\python\robot\file2.txt','w')
for element in links:
	f2.write(str(element)+'\n')
#f2.write(str(links))
f2.close()
>>>>>>> master
