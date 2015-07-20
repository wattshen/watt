#!/usr/bin/env python
<<<<<<< HEAD
#coding: utf-8 
#Author: Wattshen
#Email:34665115@qq.com
#Date:2015Äê5ÔÂ16ÈÕ
#Filename:tiquurl.py
#Content:ÌáÈ¡Ô¶³ÌHTMLÒ³Ãæ°üº¬µÄÁ´³öURL

#µ¼Èëurllib2Ä£¿é,²¢ÒÔÖ®´ò¿ªURL×ÊÔ´,ÔÙÒÔread¶ÁÈ¡,²¢½«Ö®´æµ½ÎÄ¼ş

import urllib2
import re

page_url = 'http://www.qq.com'

#»ñÈ¡Ò³ÃæÄÚÈİ
=======
#coding:utf-8
#filename:æå–è¿œç¨‹HTMLé¡µé¢åŒ…å«çš„é“¾å‡ºURL
#date:2015å¹´5æœˆ16æ—¥

#å¯¼å…¥urllib2æ¨¡å—,å¹¶ä»¥ä¹‹æ‰“å¼€URLèµ„æº,å†ä»¥readè¯»å–,å¹¶å°†ä¹‹å­˜åˆ°æ–‡ä»¶
import urllib2
import re

page_url = 'http://www.sina.com.cn'

#è·å–é¡µé¢å†…å®¹
>>>>>>> master
def getHtml(url):
	page = urllib2.urlopen(url)
	html = page.read()
	return html

<<<<<<< HEAD
#ÌáÈ¡Ò³Ãæa±êÇ©ÄÚµÄÁ´½ÓµØÖ·
=======

#æå–é¡µé¢aæ ‡ç­¾å†…çš„é“¾æ¥åœ°å€
>>>>>>> master
def getLink(html):
	link = []
	#pat = '<a.*?href="([^"]*)".*?>([\S\s]*?)</a>'
	pat = 'href\s*=\s*\"((https?://)?.+?)\"'
<<<<<<< HEAD
	#pat = 'href=\"(.+?)\"'#https?Ò»¶Î¼ÓÓë²»¼ÓÒâÒå²»´ó
	link = re.findall(pat, html)
	return link

#º¯Êıµ÷ÓÃ
htmls = getHtml(page_url)
links = getLink(htmls)
#print htmls
#print links

#½«½á¹û´æ´¢µ½ÎÄ¼ş£¬²¢°´ÔªËØ»»ĞĞ
f1 = open(r'file1.txt','w')
f1.write(htmls)
f1.close()

f2 = open(r'file2.txt','w')
for element in links:
	f2.write(str(element)+'\n')#´æ´¢ÎªÒ»ĞĞÒ»¸ö
#f2.write(str(links))#²»»»ĞĞ´æ´¢
f2.close()
=======
	#pat = 'href=\"(.+?)\"'#https?ä¸€æ®µåŠ ä¸ä¸åŠ æ„ä¹‰ä¸å¤§
	link = re.findall(pat, html)
	return link

#æå–é¡µé¢æ‰€æœ‰titleçš„å†…å®¹
def getTitle(html):
	title = []
	pat = "<title>(.+?)</title>"
	title = re.findall(pat, html)
	return title



#å‡½æ•°è°ƒç”¨
htmls = getHtml(page_url)
links = getLink(htmls)
title = getTitle(htmls)
#print htmls
#print links
for x in title:
	print x


#å°†ç»“æœå­˜å‚¨åˆ°æ–‡ä»¶ï¼Œå¹¶æŒ‰å…ƒç´ æ¢è¡Œ
f1 = open(r'G:\watt\python\robot\file1.txt','w')
f1.write(htmls)
f1.close()

f2 = open(r'G:\watt\python\robot\file2.txt','w')
for element in links:
	f2.write(str(element)+'\n')
#f2.write(str(links))
f2.close()
>>>>>>> master
