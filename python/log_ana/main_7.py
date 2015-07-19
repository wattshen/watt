#!/usr/bin/env python
#coding: utf-8 
#-*-*-  Author: Wattshen       -*-*-
#-*-*-  Email:34665115@qq.com  -*-*-
#-*-*-  Filename:.py  -*-*-
#-*-*-  Date:  
#content:
import re
import sys
import copy
import datetime
#from n_juhe import split_line, cut
#sys.path.append(r'G:\watt\python\log_ana')
import n_juhe
'''
	新增对搜索关键字的处理
	编码过程中碰到了计数器导致的超出列表范围、仅返回最后一个值等问题
	遇到了将“返回值”作为参数传给其它函数，引发的“变量未定义”错误
'''
start_time = datetime.datetime.now()


f = open(r'G:\watt\python\log_ana\20150707.csv','r+')

def split_line(file):
	'''
	
		将文件划分为行列表
		每行转化为一个字典，并返回；注意：字典是无序的。
		将多个单行字典，转化为一个大字典，（后期可以考虑返回一个迭代器)
		字典的追加赋值要用Ｋ＝Ｖ的格式，而不是Ｄ＝{K:v}重新定义字典
	'''
	keys = ["SESSION_ID","F_DATE","F_TIME","F_MOBILE","F_CITY","F_BRAND","F_KEYWORD","SYSTEM_ID","CATEGORY_ID","F_ID","F_USER_AGENT","F_TOTAL","F_OFFSET","F_URL","F_TITLE","F_DESC","F_BACK_KEYWORD"]
	content = {}.fromkeys(keys)
	p = 0
	content_he = {}
	while True:
		j = 0
		line = file.readline()
		if not line: break
		pat = r'"(.*?)"'
		unit = re.findall(pat,line)
		content_he[p] = {}
		for k in keys:#如果将keys换成content，生成的字典键值将是混乱的，因为字典无序
			content.update({k:unit[j]})#这里必须用update
			j += 1
		content_he[p].update(content)
		p += 1
	return content_he
	f.close()

def cut(dict_dict, key):
	k = 0
	a_list = []
	for k in dict_dict:
		a_list.append(dict_dict[k][key])
	a_set = set(a_list)
	a_list = list(a_set)
	print a_list





def weidu(a_list, a_list_name, dict_dict, target_1):
	target_1_list = []
	for k in dict_dict:
		if a_list[i] == dict_dict[k][a_list_name]:
			target_1_list.append(dict_dict[k][target_1])

















end_time = datetime.datetime.now()
print "本次处理开始于%s，结束于%s" % (start_time, end_time)


