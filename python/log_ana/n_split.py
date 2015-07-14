#!/usr/bin/env python
#coding: utf-8 
#-*-*-  Author: Wattshen       -*-*-
#-*-*-  Email:34665115@qq.com  -*-*-
#-*-*-  Filename:n_split.py  -*-*-
#-*-*-  Date:  2015年7月14日
import re

f = open(r'G:\watt\python\log_ana\20150707.csv','r+')

def split_line(file):
	'''将输入文件另存为指定格式键值对
		每行转化为一个字典，line_dict
		将多个单行字典，转化为一个大字典，lines_dict（后期可以考虑返回一个迭代器)
		字典的追加赋值要用Ｋ＝Ｖ的格式，而不是Ｄ＝{K:v}重新定义字典
		将所得新内容存盘
	'''
	keys = ["SESSION_ID","F_DATE","F_TIME","F_MOBILE","F_CITY","F_BRAND","F_KEYWORD","SYSTEM_ID","CATEGORY_ID","F_ID","F_USER_AGENT","F_TOTAL","F_OFFSET","F_URL","F_TITLE","F_DESC","F_BACK_KEYWORD"]
	line_dict = {}.fromkeys(keys)
	lines_dict = {}
	p = 0
	while True:
		j = 0
		line = file.readline()
		if not line: break
		pat = r'"(.*?)"'
		unit = re.findall(pat, line)
		lines_dict[p] = {}
		for k in keys:
			line_dict.update({ k : unit[j] })
			j += 1
		lines_dict[p].update(line_dict)
		p += 1
	f_out_1 = open(r'G:\watt\python\log_ana\f_out_1.txt', 'a+')
	for k, v in lines_dict.iteritems():
		f_out_1.write(str(k) + ',,' + str(v) + '\n')
	f.close()
	f_out_1.close()
	for x,y in lines_dict.iteritems():
		print str(x) + ',,' + str(y)
	return lines_dict
	
split_line(f)