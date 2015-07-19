#!/usr/bin/env python
#coding: utf-8 
#-*-*-  Author: Wattshen       -*-*-
#-*-*-  Email:34665115@qq.com  -*-*-
#-*-*-  Filename:n_juhe.py  -*-*-
#-*-*-  Date:  2015年7月14日
import re
import sys
import copy
import datetime

__metaclass__ = type
class juhe():
	"""docstring for juhe


	"""
	def split_line(self, file):
		'''
			in:file
			out:dict_dict {int:{'str1':'str2'}}
			将文件划分为行列表
			每行转化为一个字典，并返回；注意：字典是无序的。
			将多个单行字典，合并为一个大字典，（后期可以考虑返回一个迭代器)
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
			for k in keys:
				content.update({k:unit[j]})#这里必须用update
				j += 1
			content_he[p].update(content)
			p += 1
		return content_he
		f.close()
	
	def cut(self, dict_dict, key):
		'''
			in:dict_dict  {int:{'str1':'str2'}}
			in:用户指定的key即str1
			out:a_list  [str2,str2]
			按str1对输入字典进行归类整理并去重，得到所有str1相同的str2的列表

		'''
		k = 0
		a_list = []
		for k in dict_dict:
			if dict_dict[k][key]:
				a_list.append(dict_dict[k][key])
		a_set = set(a_list)
		a_list = list(a_set)
		#print a_list
		return a_list

	def he (self, dict_dict={}, a_list=[], key=''):
		'''
			in:alist[]
			in:dict_dict {int:{str1:str2}}
			out:b_dict {{'':[]},{'':[]}}
		'''
		b_dict = {}
		for k in a_list:
			b_list = []
			for k1, v1 in dict_dict.iteritems():
				if k == v1[key]:
					b_list.append(k1)
			b_dict.update({k:b_list})
		#print b_dict
		return b_dict

	def ord_sid (self, b_dict, dict_dict):
		'''
			in:b_dict {str:[int]}
			out:order
		'''
		for k, v in b_dict.iteritems():
			print '用户%s：' % k
			dates = []
			times = []
			for i in v:
				if dict_dict[i]['F_DATE'] not in dates:
					dates.append(dict_dict[i]['F_DATE'])
					print dict_dict[i]['F_DATE']
				if dict_dict[i]['F_TIME'] not in times:
					times.append(dict_dict[i]['F_TIME'])
					print '手机号码：%s,　时间：%s， 搜索了***%s***，共得到%s条结果，点击了其中的第%s条，ＵＲＬ是：%s' % (dict_dict[i]['F_MOBILE'],dict_dict[i]['F_TIME'], dict_dict[i]['F_KEYWORD'], dict_dict[i]['F_TOTAL'], dict_dict[i]['F_OFFSET'], dict_dict[i]['F_URL'])
			print '------------------------------------------'







if __name__ == 'main':
	f = open(r'G:\watt\python\log_ana\20150707.csv','r+')
	n_juhe.split_line(f)
	print 'lineNo.:56 print content_he is ' + str(len(x))
	n_juhe.cut(x,'SESSION_ID')
	n_juhe.cut(x,'F_MOBILE')
	n_juhe.cut(x,'F_KEYWORD')




