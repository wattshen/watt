#!/usr/bin/env python
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
def getHtml(url):
	page = urllib2.urlopen(url)
	html = page.read()
	return html

#��ȡҳ��a��ǩ�ڵ����ӵ�ַ
def getLink(html):
	link = []
	#pat = '<a.*?href="([^"]*)".*?>([\S\s]*?)</a>'
	pat = 'href\s*=\s*\"((https?://)?.+?)\"'
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