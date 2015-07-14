#!/usr/bin/env python
#coding: utf-8 
#-*-*-  Author: Wattshen       -*-*-
#-*-*-  Email:34665115@qq.com  -*-*-
#-*-*-  Filename:.py  -*-*-
#-*-*-  Date:  
#Content:
import re
import sys

keys = ["SESSION_ID","F_DATE","F_TIME","F_MOBILE","F_CITY","F_BRAND","F_KEYWORD","SYSTEM_ID","CATEGORY_ID","F_ID","F_USER_AGENT","F_TOTAL","F_OFFSET","F_URL","F_TITLE","F_DESC","F_BACK_KEYWORD"]

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
def process(line):
	line = line.strip('^"')
	line = line.strip('"\n')
	line_items = line.split('","')
	j=0
	while j < len(keys):
		z = keys[j]
		Content[z] = line_items[j]
		#print "%s is %s" % (keys[j], Content[z])
		j += 1
	return Content

	
def he_bing(Content, f):
	i = 0
	while True:
		line = f.readline()
		if not line: break
		process(line)
		print '\n'
		i += 1
		for k, v in Content.items():
			# print Content
			f_out = open(r'G:\watt\python\log_ana\f_out.txt', 'a+')
			f_out.write(str(k) + '   is   ' + str(v) + '\n')
			Content_he_bing ={}
			Content_he_bing = {'i':Content[keys[i]]}
		f_out.write('\n')
	f.close()
	f_out.close()
he_bing(Content, f)

'''
i = 0
Content_he_bing ={}
while i < 17:
	f_2 = open(r'G:\watt\python\log_ana\f_out.txt', 'r+')
	line_1 = f_2.readline()
	Content_he_bing = {'i':Content[keys[i]]}

for k,v in Content_he_bing.items():
	print "Content[%s]    is    %s"%(k,v)

'''