#!/usr/bin/env python
#coding:utf-8
#filename:��ȡԶ��HTMLҳ�����������URL
#date:2015��5��16��

#����urllib2ģ��,����֮��URL��Դ,����read��ȡ,����֮�浽�ļ�
import urllib2
import re

page_url = 'http://www.baidu.com'

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
f1 = open(r'C:\Users\Administrator\Desktop\robot\file1.txt','w')
f1.write(htmls)
f1.close()

f2 = open(r'C:\Users\Administrator\Desktop\robot\file2.txt','w')
for element in links:
	f2.write(str(element)+'\n')
#f2.write(str(links))
f2.close()