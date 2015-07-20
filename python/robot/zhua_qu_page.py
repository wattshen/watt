#!/usr/bin/env python
#coding:utf-8
#filename:提取远程HTML页面包含的链出URL
#date:2015年5月16日
#content:
'''
	HTML类先提取HTML（无论是否压缩），再由所提取的内容中寻找全部的a标签和TDK标签内容。
	测试了函数多个返回结果的提取
	对所得内容作了打印和保存为本地文件两种操作
	通过for循环遍历元组
'''

#导入urllib2模块,并以之打开URL资源,再以read读取,并将之存到文件
import urllib2
import re
import gzip
import StringIO

pageurl = 'http://www.baidu.com'

class HTML(object):
	#获取页面内容
	def getHtml_gzip(self,url):
		page = urllib2.urlopen(url)
		html = page.read()
		#乱码处理（新浪,gzip压缩压缩乱码）
		#htmls = unicode(htmls, "gbk").encode("utf8")
		#htmls.decode('gb2312')
		data = html
		data = StringIO.StringIO(data)
		gzipper = gzip.GzipFile(fileobj=data)
		html = gzipper.read()
		return html

	def getHtml(self,url):
		page = urllib2.urlopen(url)
		html = page.read()
		return html

	#提取页面a标签内的链接地址
	def getA(self,html):
		#pat = '<a.*?href="([^"]*)".*?>([\S\s]*?)</a>'
		#pat = 'href=\"(.+?)\"'#https?一段加与不加意义不大
		pat = 'href\s*=\s*\"((https?://)?.+?)\"'
		a = re.findall(pat, html)
		return a

	#提取页面所有TDK的内容
	def getTDK(self,html):#缺少self时会提示多传了一个参数
		pat_t = "<title>(.+?)</title>"
		pat_d ='<meta name\s*=\s*\"\s*[Dd]escription\s*\"\s*content\s*=\s*\"(.*?)\"\s*/>'
		pat_k ='<meta name\s*=\s*\"\s*[Kk]eywords\s*\"\s*content\s*=\s*\"(.*?)\"\s*/>'

		title = re.findall(pat_t, html)
		description = re.findall(pat_d, html)
		keywords = re.findall(pat_k, html)

		return title, description, keywords

#开始使用类及其方法
html = HTML()
htmls = html.getHtml(pageurl)
if 'html' not in htmls:
	htmls = html.getHtml_gzip(pageurl)

a = html.getA(htmls)
#以下三种方法都可以调用多返回值的函数
T,D,K = html.getTDK(htmls)
(a1,a2,a3) = html.getTDK(htmls)
TDK = html.getTDK(htmls)

#print htmls
#print links
#多个返回值的输出方法一
for t in T:
	print '%s \'s title is %s ' %(re.findall('http://w{3}\.(.+?)\.com',pageurl),t)
	print '@@@@@@@@@'

for d in D:
	print '%s \'s description is %s '%(re.findall('http://w{3}\.(.+?)\.com',pageurl),d)
	print '@@@@@@@@@@@@@@'

for k in K:
	print '%s \'s keywords is %s'%(re.findall('http://w{3}\.(.+?)\.com',pageurl),k)
	print '@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
#多个返回值的输出方法二
for x in TDK:
	print len(x[0])
	print '%s'%x[0]

#多个返回值的输出方法三
for x in TDK:
	for y in x:
		print len(y)
		print y
print '(a1,a2,a3)'
#多个返回值的输出方法四，同三
for x in (a1,a2,a3):
	for y in x:
		print y



#将结果存储到文件，并按元素换行
f1 = open(r'G:\watt\python\robot\file1.txt','w')
f1.write(htmls)
f1.close()

f2 = open(r'G:\watt\python\robot\file2.txt','w')
for element in a:
	f2.write(str(element)+'\n')
#f2.write(str(links))
f2.close()