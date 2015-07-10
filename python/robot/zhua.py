#!/usr/bin/env python
#coding: utf-8
#-*-*-  Author: Wattshen       -*-*-
#-*-*-  Email:34665115@qq.com  -*-*-
#-*-*-  Filename:zhua.py  -*-*-
#-*-*-  Date:
#Content:
import requests

url = 'http://tieba.baidu.com'
ua = 'User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36'

def get_html(url,ua):
	page = requests.get(url,ua)
	print page.text

get_html(url,ua)