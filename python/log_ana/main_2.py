#!/usr/bin/env python
#coding: utf-8 
#-*-*-  Author: Wattshen       -*-*-
#-*-*-  Email:34665115@qq.com  -*-*-
#-*-*-  Filename:.py  -*-*-
#-*-*-  Date:  
#Content:
import re
import sys

#创建字典的4种方法
#1
keys_a = [("name","tom"),("age",35)]
Content_a = dict(keys_a)
#2
Content_b = dict(a= 1,b=2)
#3 本例情况，此法最方便
keys = ["SESSION_ID","F_DATE","F_TIME","F_MOBILE","F_CITY","F_BRAND","F_KEYWORD","SYSTEM_ID","CATEGORY_ID","F_ID","F_USER_AGENT","F_TOTAL","F_OFFSET","F_URL","F_TITLE","F_DESC","F_BACK_KEYWORD"]
Content_c = {}.fromkeys(keys)
#4　此法最清晰
Content = {
	"SESSION_ID":None,
	"F_DATE":None,
	"F_TIME":None,
	"F_MOBILE":None,
	"F_CITY":None,
	"F_BRAND":None,
	"F_KEYWORD":None,
	"SYSTEM_ID":None,
	"CATEGORY_ID":None,
	"F_ID":None,
	"F_USER_AGENT":None,
	"F_TOTAL":None,
	"F_OFFSET":None,
	"F_URL":None,
	"F_TITLE":None,
	"F_DESC":None,
	"F_BACK_KEYWORD":None
}

f = open(r'G:\watt\python\log_ana\20150707.csv','r+')
def split_line(line):
	'''
		将每行转化为一个字典，并返回；注意：字典是无序的。
	'''
	line = line.strip('^"')
	line = line.strip('"\n')
	unit = line.split('","')
	j = 0
	for k in keys:#如果将keys换成content，生成的字典键值将是混乱的，因为字典无序
		Content[k] = unit[j]
		#print "%s is %s" % (keys[j], Content[k])
		j += 1
	return Content
	
def he_bing(dict_name, File_name):
	i = 0
	while True:
		line = f.readline()
		if not line: break
		split_line(line)
		print '\n'
		for k, v in Content.iteritems():
			# print Content
			f_out = open(r'G:\watt\python\log_ana\f_out.txt', 'a+')
			f_out.write(str(k) + '   is   ' + str(v) + '\n')
			Content_he_bing ={}
			Content_he_bing = {i:Content}
		f_out.write('\n')
		print Content_he_bing
		i += 1
	f.close()
	f_out.close()
he_bing(Content, f)

