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

Content = [
	{"SESSION_ID":None},
	{"F_DATE":None},
	{"F_TIME":None},
	{"F_MOBILE":None},
	{"F_CITY":None},
	{"F_BRAND":None},
	{"F_KEYWORD":None},
	{"SYSTEM_ID":None},
	{"CATEGORY_ID":None},
	{"F_ID":None},
	{"F_USER_AGENT":None},
	{"F_TOTAL":None},
	{"F_OFFSET":None},
	{"F_URL":None},
	{"F_TITLE":None},
	{"F_DESC":None},
	{"F_BACK_KEYWORD":None}
]
i = 0

f = open(r'G:\watt\python\log_ana\20150707.csv','r+')
def process(line):
	line_items = line.split(",")
	j=0
	while j < len(keys):
		z = keys[j]
		Content[i][z] = line_items[j]
		j += 1
		print Content[i][z] 
	return Content

	

while True:
	line = f.readline()
	if not line: break
	process(line)
	i += 1
	print Content
f.close()